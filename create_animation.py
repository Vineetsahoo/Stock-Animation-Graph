import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.animation import FuncAnimation

# Load and prepare data for all three stocks
def load_stock_data(filename, stock_name):
    """Load and clean stock data"""
    df = pd.read_csv(filename)
    df['Date'] = pd.to_datetime(df['Date'])
    df['Close'] = df['Close/Last'].str.replace('$', '').astype(float)
    df['Stock'] = stock_name
    return df[['Date', 'Close', 'Stock']].copy()

# Define all companies and their CSV files
companies = {
    'AMD': 'amd.csv',
    'NVIDIA': 'nvidia.csv', 
    'Intel': 'intel.csv',
    'Apple': 'apple.csv',
    'Microsoft': 'microsoft.csv',
    'Tesla': 'tesla.csv',
    'Qualcomm': 'qualcomm.csv'
}

# Load all datasets
print("Loading stock data...")
stock_data = {}
all_dataframes = []

for company, filename in companies.items():
    try:
        df = load_stock_data(filename, company)
        stock_data[company] = df.sort_values('Date').reset_index(drop=True)
        all_dataframes.append(df)
        print(f"[SUCCESS] {company} data loaded: {len(df)} records")
    except Exception as e:
        print(f"[ERROR] Error loading {company} data: {str(e)}")

# Combine all data and sort by date
all_data = pd.concat(all_dataframes, ignore_index=True)
all_data = all_data.sort_values('Date').reset_index(drop=True)

print(f"\nTotal companies loaded: {len(stock_data)}")
print(f"Date range: {all_data['Date'].min().strftime('%Y-%m-%d')} to {all_data['Date'].max().strftime('%Y-%m-%d')}")

# Get unique dates and create a complete timeline
date_range = pd.date_range(start=all_data['Date'].min(), 
                          end=all_data['Date'].max(), 
                          freq='D')

# Define professional color palette for all companies
colors = {
    'AMD': '#FF6B6B',       # Red
    'NVIDIA': '#4ECDC4',    # Teal
    'Intel': '#45B7D1',     # Blue
    'Apple': '#FF9F43',     # Orange
    'Microsoft': '#6C5CE7', # Purple
    'Tesla': '#00B894',     # Green
    'Qualcomm': '#E17055'   # Coral
}

# Set up the figure and axis
fig, ax = plt.subplots(figsize=(16, 10))  # Larger figure for more companies
ax.set_xlim(all_data['Date'].min(), all_data['Date'].max())
ax.set_ylim(all_data['Close'].min() * 0.85, all_data['Close'].max() * 1.15)  # More padding for better visibility
ax.set_xlabel('Date', fontsize=12, fontweight='bold')
ax.set_ylabel('Stock Price ($)', fontsize=12, fontweight='bold')
ax.set_title('Multi-Company Stock Prices Over Time (Animated)', fontsize=16, fontweight='bold', pad=20)
ax.grid(True, alpha=0.3)

# Initialize empty lines, tickers, and value labels for each stock
lines = {}
tickers = {}
value_texts = {}

for company in stock_data.keys():
    color = colors[company]
    
    # Initialize line plot
    line, = ax.plot([], [], color=color, linewidth=2.5, label=company, alpha=0.9)
    lines[company] = line
    
    # Initialize ticker mark
    ticker, = ax.plot([], [], 'o', color=color, markersize=8, 
                     markeredgecolor='white', markeredgewidth=2, zorder=5)
    tickers[company] = ticker
    
    # Initialize value label
    value_text = ax.text(0, 0, '', fontsize=9, fontweight='bold', color=color,
                        bbox=dict(boxstyle='round,pad=0.3', facecolor='white', 
                                alpha=0.8, edgecolor=color), zorder=6)
    value_texts[company] = value_text

# Add legend with better positioning
ax.legend(loc='upper left', frameon=True, fancybox=True, shadow=True, fontsize=10)

# Add text for current prices display
price_text = ax.text(0.98, 0.98, '', transform=ax.transAxes, 
                    fontsize=10, verticalalignment='top', horizontalalignment='right',
                    bbox=dict(boxstyle='round', facecolor='wheat', alpha=0.9))

def get_data_up_to_date(df, target_date):
    """Get all data up to and including the target date"""
    return df[df['Date'] <= target_date]

def animate(frame):
    """Animation function called for each frame"""
    # Calculate current date based on frame
    total_days = (all_data['Date'].max() - all_data['Date'].min()).days
    current_date = all_data['Date'].min() + pd.Timedelta(days=int(frame * total_days / 200))
    
    # Store all animated objects for blitting
    animated_objects = []
    
    # Get data up to current date for each stock and update visuals
    for company in stock_data.keys():
        current_data = get_data_up_to_date(stock_data[company], current_date)
        
        # Update line data
        lines[company].set_data(current_data['Date'], current_data['Close'])
        animated_objects.append(lines[company])
        
        # Update ticker marks and value labels
        if len(current_data) > 0:
            last_date = current_data['Date'].iloc[-1]
            last_price = current_data['Close'].iloc[-1]
            
            # Update ticker mark position
            tickers[company].set_data([last_date], [last_price])
            animated_objects.append(tickers[company])
            
            # Update value label position and text with offset to avoid overlap
            offset_x = pd.Timedelta(days=3)
            offset_y = (all_data['Close'].max() - all_data['Close'].min()) * 0.02
            value_texts[company].set_position((last_date + offset_x, last_price + offset_y))
            value_texts[company].set_text(f'${last_price:.2f}')
            animated_objects.append(value_texts[company])
        else:
            # Clear ticker and text if no data available
            tickers[company].set_data([], [])
            value_texts[company].set_text('')
            animated_objects.append(tickers[company])
            animated_objects.append(value_texts[company])
    
    # Update price information box
    text_lines = [f'Date: {current_date.strftime("%Y-%m-%d")}', '']
    
    # Add current prices for all companies
    for company in stock_data.keys():
        current_data = get_data_up_to_date(stock_data[company], current_date)
        if len(current_data) > 0:
            current_price = current_data['Close'].iloc[-1]
            text_lines.append(f'{company}: ${current_price:.2f}')
    
    price_text.set_text('\n'.join(text_lines))
    animated_objects.append(price_text)
    
    return tuple(animated_objects)

# Create animation
print("\nCreating animation...")
print(f"Animating {len(stock_data)} companies: {', '.join(stock_data.keys())}")

# Using 200 frames for smoother animation across the date range
anim = FuncAnimation(fig, animate, frames=200, interval=50, 
                    blit=True, repeat=True)

# Display the animation
print("Displaying animation...")
plt.tight_layout()
plt.show()

print("Animation completed!")

# Optional: Save as mp4 (uncomment if you want to save, requires ffmpeg)
# print("Saving animation as MP4...")
# anim.save('multi_company_stock_animation.mp4', writer='ffmpeg', fps=20, bitrate=1800)
# print("Animation saved as 'multi_company_stock_animation.mp4'")

# Optional: Save as GIF (uncomment if you want to save)
# print("Saving animation as GIF...")
# anim.save('multi_company_stock_animation.gif', writer='pillow', fps=10)
# print("Animation saved as 'multi_company_stock_animation.gif'")
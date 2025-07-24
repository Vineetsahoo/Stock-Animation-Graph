# Multi-Company Stock Price Animation Visualization 

An animated line graph visualization comparing multiple tech company stock prices over time using Python and matplotlib. This project demonstrates how to load and process stock data for AMD, Intel, Nvidia, Apple, Microsoft, Tesla, and Qualcomm, create dynamic visualizations with moving price labels, and export the final result as both MP4 and GIF formats. Whether you're interested in data visualization, financial analysis, or learning matplotlib animations, this project provides a comprehensive example with scalable architecture for any number of companies.

## Features

- **Multi-Company Comparison**: Visualize 7 major tech companies simultaneously (AMD, Intel, Nvidia, Apple, Microsoft, Tesla, Qualcomm)
- **Scalable Architecture**: Easily add or remove companies by modifying the companies dictionary
- **Animated Timeline**: Watch how stock prices evolve over time with smooth animations
- **Dynamic Price Labels**: Real-time price display with moving ticker marks
- **Interactive Display**: Live price information box showing current values for all companies
- **Export Options**: Save animations as MP4 or GIF files
- **Professional Color Palette**: Distinct colors for each company with excellent contrast
- **Error Handling**: Graceful handling of missing CSV files with clear status messages
- **Professional Styling**: Clean, modern visualization with grid and legends
- **Interactive Tutorial**: Comprehensive Jupyter notebook with step-by-step explanations
- **Educational Content**: Perfect for learning data visualization and matplotlib animations
- **Cross-Platform Compatible**: Works on Windows, macOS, and Linux

## Prerequisites

Before running this project, ensure you have Python installed with the following packages:

```bash
pip install pandas numpy matplotlib seaborn
```

For Jupyter notebook support:
```bash
pip install jupyter notebook
```

For MP4 export, you'll also need FFmpeg installed on your system.

### Installation Guide
1. **Python packages**: Run the pip install commands above
2. **FFmpeg** (optional): Download from [https://ffmpeg.org/](https://ffmpeg.org/)
3. **Jupyter** (optional): For interactive notebook experience

## Project Structure

```
line-animation/
├── create_animation.py              # Main animation script (supports 7 companies)
├── stock_animation.ipynb            # Interactive Jupyter notebook tutorial
├── amd.csv                         # AMD stock data
├── intel.csv                       # Intel stock data
├── nvidia.csv                      # Nvidia stock data
├── apple.csv                       # Apple stock data
├── microsoft.csv                   # Microsoft stock data
├── tesla.csv                       # Tesla stock data
├── qualcomm.csv                    # Qualcomm stock data
├── multi_company_stock_animation.mp4 # Generated MP4 output (optional)
├── multi_company_stock_animation.gif # Generated GIF output (optional)
└── README.md                       # This file
```

## Data Format

The CSV files should contain stock data with the following columns:
- `Date`: Date of the stock price
- `Close/Last`: Closing price (formatted as $XX.XX)

## How to Use

### Option 1: Python Script (Quick Start)
1. **Clone or download** this repository
2. **Place your CSV files** in the same directory as the script
3. **Run the animation**:
   ```bash
   python create_animation.py
   ```
4. **View the animation** in the matplotlib window
5. **Export options** are available at the bottom of the script

### Option 2: Jupyter Notebook (Interactive Learning)
1. **Open the notebook**:
   ```bash
   jupyter notebook stock_animation.ipynb
   ```
   Or open directly in VS Code with Jupyter extension
2. **Run cells step-by-step** to understand the process
3. **Experiment with parameters** and see immediate results
4. **Follow the comprehensive tutorial** with detailed explanations

### Recommended Approach
- **Beginners**: Start with the Jupyter notebook for learning
- **Quick deployment**: Use the Python script for immediate results
- **Customization**: Use the notebook to experiment, then adapt the script

## Customization Options

### Companies
The script currently supports 7 major tech companies:
- **AMD**: Red (#FF6B6B)
- **NVIDIA**: Teal (#4ECDC4)
- **Intel**: Blue (#45B7D1)
- **Apple**: Orange (#FF9F43)
- **Microsoft**: Purple (#6C5CE7)
- **Tesla**: Green (#00B894)
- **Qualcomm**: Coral (#E17055)

### Adding More Companies
To add more companies, simply:
1. Add the CSV file to your directory
2. Update the `companies` dictionary in the script:
```python
companies = {
    'AMD': 'amd.csv',
    'NVIDIA': 'nvidia.csv',
    # ... existing companies ...
    'NewCompany': 'newcompany.csv'
}
```
3. Add a color to the `colors` dictionary:
```python
colors = {
    # ... existing colors ...
    'NewCompany': '#HEX_COLOR'
}
```

### Animation Parameters
- **Frames**: 200 frames for smooth animation
- **Interval**: 50ms between frames (20 FPS)
- **Figure Size**: 16x10 inches for optimal viewing

### Chart Styling
- Grid opacity: 30%
- Line width: 2.5px
- Marker size: 8px with white edges
- Legend position: Upper left with shadow

## Features Explained

### Data Processing
- Loads and cleans CSV data from multiple company sources
- Converts date strings to datetime objects
- Removes currency symbols and converts to float
- Combines and sorts data chronologically
- Dynamic error handling for missing files

### Animation Logic
- Calculates current date based on frame number
- Filters data up to the current animation date for each company
- Updates line plots progressively for all companies
- Moves ticker marks and price labels dynamically
- Updates the information box with all current prices in real-time

### Visual Elements
- **Line Charts**: Show historical price trends for each company
- **Ticker Marks**: Highlight current prices with circular markers
- **Price Labels**: Display exact current values for each stock
- **Information Box**: Shows date and all current prices
- **Legend**: Identifies each company with colored labels
- **Professional Layout**: Optimized for 7+ companies with clear distinction

### Scalable Architecture
- **Dynamic Loading**: Automatically adapts to available CSV files
- **Flexible Colors**: Easy to add new color schemes
- **Modular Design**: Simple to extend with additional companies
- **Error Resilience**: Continues working even if some files are missing

## Jupyter Notebook Tutorial

The included `stock_animation.ipynb` provides a comprehensive, interactive learning experience:

### What's Included:
1. **Step-by-Step Guide**: Each concept explained in detail with markdown cells
2. **Interactive Code**: Run and modify code cells to see immediate results
3. **Visual Examples**: Live plots and animations within the notebook
4. **Error Handling**: Graceful error management with helpful messages
5. **Customization Examples**: Easy ways to modify colors, timing, and styles
6. **Export Instructions**: Detailed guidance for saving animations

### Notebook Sections:
- **Library Imports**: Understanding required packages
- **Data Loading**: CSV processing and cleaning techniques
- **Data Preparation**: Combining and sorting multiple datasets
- **Plot Setup**: Professional matplotlib configuration
- **Animation Elements**: Dynamic components and styling
- **Animation Logic**: Frame-by-frame update mechanisms
- **Display & Export**: Running and saving animations

### Perfect For:
- **Students**: Learning data visualization concepts
- **Educators**: Teaching matplotlib and pandas
- **Developers**: Understanding animation implementation
- **Analysts**: Exploring financial data visualization techniques

## Technical Details

### Key Functions
- `load_stock_data()`: Loads and preprocesses CSV files
- `get_data_up_to_date()`: Filters data for current animation frame
- `animate()`: Main animation function called for each frame
- `update_ticker()`: Updates ticker marks and price labels

### Performance Optimizations
- Uses blitting for smooth animation
- Efficient data filtering with pandas
- Minimal plot updates per frame

## Export Options

### MP4 Export
```python
anim.save('multi_stock_animation.mp4', writer='ffmpeg', fps=20)
```

### GIF Export
```python
anim.save('multi_stock_animation.gif', writer='pillow', fps=10)
```

### Export Tips
- **MP4**: Best for presentations and high-quality sharing
- **GIF**: Great for web usage and social media
- **File size**: GIF files are typically larger than MP4 for the same quality
- **Performance**: Export time depends on frame count and complexity
- **New filenames**: Files are saved as `multi_company_stock_animation.mp4/gif`

## Troubleshooting

### Common Issues
1. **Missing FFmpeg**: Install FFmpeg for MP4 export
2. **CSV Format**: Ensure your CSV files match the expected format
3. **Memory Issues**: Reduce frame count or data size for large datasets
4. **Performance**: Adjust interval parameter for smoother playback

### Error Solutions
- **Import errors**: Install required packages with pip
- **File not found**: Check CSV file paths and names
- **Animation not displaying**: Ensure matplotlib backend supports animation

## Future Enhancements

- Add volume data visualization
- Include more stocks for comparison
- Interactive controls for playback speed
- Real-time data fetching from APIs
- Additional chart types (candlestick, volume bars)
- Customizable time ranges and intervals
- Web-based interactive version
- Portfolio performance comparison features
- Technical indicators (moving averages, RSI, etc.)

## Learning Resources

### Tutorials
- **Jupyter Notebook**: `stock_animation.ipynb` - Complete step-by-step guide
- **Python Script**: `create_animation.py` - Ready-to-run implementation

### Documentation
- [Matplotlib Animation Documentation](https://matplotlib.org/stable/api/animation_api.html)
- [Pandas Documentation](https://pandas.pydata.org/docs/)
- [NumPy Documentation](https://numpy.org/doc/)
- [FFmpeg Installation Guide](https://ffmpeg.org/download.html)

### Example Outputs
- Sample animations are generated as `multi_company_stock_animation.mp4` and `multi_company_stock_animation.gif`
- View these files to see expected results before running your own data
- Console output shows loading status: `[SUCCESS]` or `[ERROR]` for each company

## License

This project is open source and available under the MIT License.

## Contributing

You can fix this project and submit pull requests for improvements or bug fixes.

## Contact

For questions or suggestions, please open an issue in the repository.

---

*Created for data visualization enthusiasts*

# Netflix Streamlit Visualization 🎬

A modular Streamlit web application for interactive data visualization and exploration using the Netflix Movies & TV Shows dataset from Kaggle.

## 📁 Project Structure

```
.
├── app.py                          # Main application entry point
├── requirements.txt                # Python dependencies
├── README.md                       # This file
└── utils/                          # Modular components package
    ├── __init__.py                # Package initialization
    ├── config.py                  # Page configuration and styling
    ├── data_loader.py            # Dataset loading functionality
    ├── filters.py                # Data filtering logic
    ├── visualizations.py         # Chart and plot generation
    └── statistics.py             # Statistical summaries
```

## ✨ Features

### ✅ All Assignment Requirements Met:

#### 1. **Dataset Loading**

- ✅ **Kaggle Dataset**: Netflix Movies & TV Shows dataset
- ✅ **CSV Upload**: Custom file upload functionality for any CSV

#### 2. **Interactive Sidebar Filters** (All Three Types)

- ✅ **Selectbox**: Dataset selection dropdown
- ✅ **Slider**: Release year range filter
- ✅ **Multiselect**: Content type and rating filters

#### 3. **Multiple Visualizations** (4 Chart Types)

- ✅ **Bar Chart**: Content distribution (Movies vs TV Shows)
- ✅ **Histogram**: Release year distribution by content type
- ✅ **Pie Chart**: Top 10 genres distribution
- ✅ **World Map**: Content distribution by country (choropleth map)

#### 4. **Data Summary Section** (Both Methods)

- ✅ **st.metric()**: Key performance indicators (Total titles, Movies, TV Shows)
- ✅ **st.dataframe()**: Interactive statistical tables and data preview

### 🎨 Bonus Features:

- ✅ **Netflix Theme**: Dark background with Netflix red (#E50914) accents
- ✅ **Modular Architecture**: Clean, maintainable code structure
- ✅ **Responsive Layout**: Multi-column design with tabs
- ✅ **Export Functionality**: Download filtered data as CSV
- ✅ **Real-time Updates**: Instant filter application
- ✅ **Dark Mode**: Netflix-inspired black and red color scheme

## 🚀 Installation & Setup

### Prerequisites

- Python 3.8 or higher
- pip package manager

### Installation Steps

1. **Download all project files** (including `netflix_titles.csv`)

2. **Install dependencies:**

   ```bash
   pip install -r requirements.txt
   ```

3. **Run the application:**

   ```bash
   streamlit run app.py
   ```

4. **Access the application:**
   - The app will automatically open in your browser
   - Default URL: `http://localhost:8501`
   - The Netflix dataset is already included and will load automatically!

### Note

The `netflix_titles.csv` file is included in the project folder and contains 8,807 real Netflix titles from Kaggle.

## 📖 Usage Guide

### 1. Select a Dataset

Use the sidebar dropdown to choose from:

- **Netflix Movies & TV Shows (Kaggle)**: Popular dataset with information about Netflix content
- **Upload Your Own**: Import custom CSV files for analysis

### 2. Apply Filters

For the Netflix dataset:

**Filters Available:**

- Content type selection (Movie/TV Show) - multiselect
- Rating selection (TV-MA, PG-13, etc.) - multiselect
- Release year range - slider

### 3. Explore Visualizations

Navigate through five tabs:

- **Bar Chart**: Movies vs TV Shows distribution
- **Histogram**: Release year trends
- **Pie Chart**: Top 10 genres (from listed_in column)
- **World Map**: Global content distribution by country
- **Data Table**: Filtered data preview with download option

### 4. Analyze Statistics

Review comprehensive summaries:

- Top metrics displayed as cards (Total titles, Movies count, TV Shows count)
- Numerical statistics (mean, std, quartiles)
- Categorical value distributions

## 🏗️ Modular Architecture

### Core Modules

#### `app.py` - Main Application

- Entry point for the application
- Orchestrates all components
- Manages application flow

#### `utils/config.py` - Configuration

- Page settings and layout
- Custom CSS styling
- Theme configuration

#### `utils/data_loader.py` - Data Loading

- **DataLoader class**: Handles Netflix dataset and custom CSV
- Methods for loading from Kaggle (via GitHub mirror)
- Error handling and validation

#### `utils/filters.py` - Filter Management

- **FilterManager class**: Applies dataset-specific filters
- Dynamic filter generation
- Filter state management

#### `utils/visualizations.py` - Visualizations

- **VisualizationManager class**: Creates all charts
- Plotly integration
- Dataset-specific chart logic

#### `utils/statistics.py` - Statistics

- **StatisticsManager class**: Calculates and displays metrics
- Numerical and categorical summaries
- Custom metrics per dataset

## 📊 Available Dataset

### Netflix Movies & TV Shows (Kaggle)

- **Source**: Kaggle dataset (included in project)
- **Records**: 8,807 titles
- **Content Breakdown**:
  - Movies: 6,131
  - TV Shows: 2,676
- **Features**:
  - show_id, type, title
  - director, cast
  - country, date_added
  - release_year, rating
  - duration, listed_in (genres)
  - description
- **Use Case**: Content analysis, trend visualization, rating distribution, genre analysis

### Custom CSV Upload

- **Format**: Standard CSV with headers
- **Flexibility**: Any structured tabular data
- **Auto-detection**: Automatic column type detection

## 🛠️ Technology Stack

| Component           | Technology | Version |
| ------------------- | ---------- | ------- |
| Framework           | Streamlit  | 1.29.0  |
| Data Processing     | Pandas     | 2.1.4   |
| Visualization       | Plotly     | 5.18.0  |
| Numerical Computing | NumPy      | 1.26.2  |

## 🎯 Key Benefits of Modular Design

### 1. **Maintainability**

- Each module has a single responsibility
- Easy to locate and fix bugs
- Clear separation of concerns

### 2. **Scalability**

- Add new datasets by extending DataLoader
- Add new visualizations by extending VisualizationManager
- Easy to add new filter types

### 3. **Reusability**

- Modules can be imported independently
- Classes can be instantiated with different parameters
- Methods can be reused across different contexts

### 4. **Testability**

- Each module can be tested independently
- Mock objects can be easily created
- Unit tests can focus on specific functionality

### 5. **Readability**

- Clear file structure
- Descriptive class and method names
- Comprehensive docstrings

## 🔧 Customization Guide

### Adding a New Dataset

1. **Edit `utils/data_loader.py`:**

```python
def _load_new_dataset(self):
    """Load your new dataset"""
    df = pd.read_csv('path/to/your/data.csv')
    info = "Description of your dataset"
    return df, info, "new_dataset"
```

2. **Add dataset option in `__init__` and `load_data()`**

### Adding New Filters

1. **Edit `utils/filters.py`:**

```python
def _apply_new_dataset_filters(self):
    """Apply filters for new dataset"""
    # Add your filter logic here
    return self.filtered_df
```

### Adding New Visualizations

1. **Edit `utils/visualizations.py`:**

```python
def _create_new_chart(self):
    """Create chart for new dataset"""
    fig = px.chart_type(self.df, ...)
    st.plotly_chart(fig, use_container_width=True)
```

### Modifying Styling

1. **Edit `utils/config.py`:**

```python
def apply_custom_styling():
    # Modify CSS in the markdown section
```

## 🐛 Troubleshooting

### Common Issues and Solutions

#### Issue: Module Import Errors

**Solution:** Ensure you're running from the project root directory

```bash
cd /path/to/project
streamlit run app.py
```

#### Issue: Dataset Loading Fails

**Solution:** Check internet connection for URL-based datasets

```bash
# Test internet connection
ping github.com
```

#### Issue: Port Already in Use

**Solution:** Specify a different port

```bash
streamlit run app.py --server.port 8502
```

#### Issue: CSV Upload Fails

**Solution:** Ensure CSV file has:

- Proper headers in first row
- Consistent delimiter (comma)
- UTF-8 encoding

## 📈 Performance Considerations

- **Data Caching**: Streamlit automatically caches data loading
- **Efficient Filtering**: Pandas operations optimized for speed
- **Responsive Visualizations**: Plotly renders efficiently
- **Memory Management**: Large datasets handled appropriately

## 🔒 Security Notes

- File uploads are processed in memory
- No data is stored permanently
- URL datasets fetched from trusted sources
- Input validation on all user inputs

## 📝 Code Quality Standards

✅ **Documentation**: Comprehensive docstrings for all classes and methods  
✅ **Type Hints**: Function signatures include type information  
✅ **Error Handling**: Try-except blocks for external data sources  
✅ **Code Style**: Following PEP 8 guidelines  
✅ **Modularity**: Single Responsibility Principle applied

## 🎓 Learning Outcomes

This project demonstrates:

- Web application development with Streamlit
- Object-oriented programming in Python
- Data manipulation with Pandas
- Interactive visualization with Plotly
- Modular software architecture
- User interface/experience design
- Working with real-world datasets from Kaggle

## 📄 License

This project is created for educational purposes.

## 🤝 Contributing

To extend this project:

1. Follow the modular structure
2. Add comprehensive docstrings
3. Test new features thoroughly
4. Update README with new functionality

## 📞 Support

For issues or questions:

1. Check the Troubleshooting section
2. Review the Customization Guide
3. Examine module docstrings
4. Refer to Streamlit documentation: https://docs.streamlit.io

## 🎉 Acknowledgments

- **Streamlit**: For the excellent framework
- **Plotly**: For interactive visualizations
- **Kaggle**: For the Netflix dataset
- **Netflix**: For making the data available

---

**Built with ❤️ using Streamlit | Modular Architecture for Scalability and Maintainability**

---

## 📋 Quick Reference

### Run Application

```bash
streamlit run app.py
```

### Install Dependencies

```bash
pip install -r requirements.txt
```

### Project Structure

```
app.py → utils/ → [config, data_loader, filters, visualizations, statistics]
```

### Key Classes

- `DataLoader`: Handles data loading
- `FilterManager`: Manages filters
- `VisualizationManager`: Creates charts
- `StatisticsManager`: Displays metrics

---

**Assignment Status: ✅ Complete with Modular Architecture**

# Netflix Streamlit Visualization 🎬

An interactive Streamlit web application for visualizing Netflix Movies & TV Shows data from Kaggle.

## 📁 Project Structure

```
netflix-streamlit-visualization/
├── app.py                    # Main application
├── requirements.txt          # Dependencies
├── README.md                # Documentation
├── data/
│   └── netflix_titles.csv   # Netflix dataset
└── utils/
    ├── __init__.py
    ├── config.py            # Page configuration
    ├── data_loader.py       # Data loading
    ├── filters.py           # Filter management
    ├── visualizations.py    # Chart creation
    └── statistics.py        # Statistics display
```

## ✨ Features

### Assignment Requirements Met:

- ✅ **Dataset**: Netflix Movies & TV Shows from [Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows) (loads automatically)
- ✅ **Filters**: Selectbox, Slider, and Multiselect filters
- ✅ **Visualizations**: Bar Chart, Histogram, Pie Chart, World Map
- ✅ **Data Summary**: st.metric() and st.dataframe()
- ✅ **Modular Code**: Clean architecture with separate modules

### Bonus Features:

- 🎨 Netflix-themed design (red and black color scheme)
- 🗺️ Interactive world map visualization
- 📊 4 different chart types
- 📥 CSV export functionality

## 🚀 Quick Start

### 1. Install Dependencies

```bash
pip install -r requirements.txt
```

### 2. Run the App

```bash
streamlit run app.py
```

### 3. Open in Browser

The app will automatically open at `http://localhost:8501`

## 📊 Dataset

**Source**: [Netflix Shows - Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)

**Statistics**:

- Total Records: 8,807 titles
- Movies: 6,131
- TV Shows: 2,676

**Columns**: show_id, type, title, director, cast, country, date_added, release_year, rating, duration, listed_in (genres), description

## 🎯 How to Use

1. **Dataset Loads Automatically**: Netflix dataset (8,807 titles) loads when app starts
2. **Apply Filters**: Use sidebar to filter by content type, rating, and release year
3. **Explore Visualizations**:
   - 📊 Bar Chart - Movies vs TV Shows
   - 📈 Histogram - Release year trends
   - 🥧 Pie Chart - Top 10 genres
   - 🗺️ Map - Content by country
4. **View Statistics**: Check metrics and data summaries
5. **Download Data**: Export filtered data as CSV

## 🛠️ Technology Stack

- **Streamlit** 1.29.0 - Web framework
- **Pandas** 2.1.4 - Data processing
- **Plotly** 5.18.0 - Interactive charts
- **NumPy** 1.26.2 - Numerical operations

## 📝 Modular Architecture

The application uses a modular design pattern:

- `app.py` - Main entry point, orchestrates all components
- `utils/config.py` - Page configuration and Netflix theme
- `utils/data_loader.py` - Loads dataset from CSV or uploads
- `utils/filters.py` - Handles all filtering logic
- `utils/visualizations.py` - Creates all charts and maps
- `utils/statistics.py` - Displays metrics and summaries

## 🎨 Customization

### Add New Dataset

Edit `utils/data_loader.py`:

```python
def _load_new_dataset(self):
    df = pd.read_csv('your_data.csv')
    return df, "Dataset info", "dataset_type"
```

### Add New Visualization

Edit `utils/visualizations.py`:

```python
def _create_new_chart(self):
    fig = px.chart_type(self.df, ...)
    st.plotly_chart(fig, use_container_width=True)
```

## 🐛 Troubleshooting

**Issue**: Module not found  
**Solution**: Run from project root directory

```bash
cd /path/to/project
streamlit run app.py
```

**Issue**: Port already in use  
**Solution**: Use different port

```bash
streamlit run app.py --server.port 8502
```

## 📄 License

Educational purposes only.

## 🙏 Credits

- Dataset: [Shivam Bansal on Kaggle](https://www.kaggle.com/datasets/shivamb/netflix-shows)
- Built with [Streamlit](https://streamlit.io/)
- Visualizations by [Plotly](https://plotly.com/)

---

**Built with ❤️ for data visualization | Modular & Scalable Architecture**

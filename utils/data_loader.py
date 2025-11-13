"""
Data loading module for handling Kaggle dataset
"""

import streamlit as st
import pandas as pd
import os


class DataLoader:
    """Handles loading Netflix dataset from Kaggle"""
    
    def __init__(self):
        self.dataset_options = [
            "Netflix Movies & TV Shows (Kaggle)"
        ]
    
    def load_data(self):
        """
        Load dataset based on user selection
        
        Returns:
            tuple: (dataframe, dataset_info, dataset_type)
        """
        dataset_option = st.sidebar.selectbox(
            "📁 Select Dataset:",
            self.dataset_options
        )
        
        return self._load_netflix_dataset()
    
    def _load_netflix_dataset(self):
        """Load Netflix dataset from uploaded CSV file"""
        try:
            # Try to find the dataset in common locations
            possible_paths = [
                '/mnt/user-data/uploads/netflix_titles.csv',  # Uploaded file location
                'netflix_titles.csv',
                'data/netflix_titles.csv',
                '../netflix_titles.csv',
                './netflix_titles.csv'
            ]
            
            df = None
            found_path = None
            
            for path in possible_paths:
                if os.path.exists(path):
                    df = pd.read_csv(path)
                    found_path = path
                    break
            
            if df is None:
                st.error("❌ Netflix dataset not found!")
                st.info("""
                📥 **How to get the dataset:**
                
                1. Download from Kaggle: https://www.kaggle.com/datasets/shivamb/netflix-shows
                2. Extract the `netflix_titles.csv` file
                3. Place it in the same folder as `app.py` or in `/mnt/user-data/uploads/`
                4. Refresh this page
                """)
                return None, None, None
            
            # Clean the data
            if 'date_added' in df.columns:
                df['date_added'] = pd.to_datetime(df['date_added'], errors='coerce')
                df['year_added'] = df['date_added'].dt.year
            
            if 'release_year' in df.columns:
                df['release_year'] = pd.to_numeric(df['release_year'], errors='coerce')
            
            # Remove rows with missing critical data
            original_count = len(df)
            df = df.dropna(subset=['type', 'title'])
            
            info = f"Netflix Movies & TV Shows dataset from Kaggle - Contains {len(df):,} titles (originally {original_count:,} records)"
            return df, info, "netflix"
            
        except Exception as e:
            st.error(f"Failed to load Netflix dataset: {str(e)}")
            st.info("💡 Please ensure the netflix_titles.csv file is in the correct location.")
            return None, None, None
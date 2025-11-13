"""
Data loading module for handling Kaggle dataset
"""

import streamlit as st
import pandas as pd
import os


class DataLoader:
    """Handles loading data from Kaggle dataset or custom CSV"""
    
    def __init__(self):
        self.dataset_options = [
            "Netflix Movies & TV Shows (Kaggle)",
            "Upload Your Own CSV"
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
        
        if dataset_option == "Netflix Movies & TV Shows (Kaggle)":
            return self._load_netflix_dataset()
        else:
            return self._load_custom_csv()
    
    def _load_netflix_dataset(self):
        """Load Netflix dataset from uploaded CSV file"""
        try:
            # Try to find the dataset in common locations
            possible_paths = ['data/netflix_titles.csv']

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
                
                **Option 1: Download from Kaggle**
                1. Go to Kaggle: https://www.kaggle.com/datasets/shivamb/netflix-shows
                2. Click "Download" button (you may need to sign in)
                3. Extract the `netflix_titles.csv` file
                4. Place it in the same folder as `app.py`
                5. Refresh this page
                
                **Option 2: Upload directly**
                Use the "Upload Your Own CSV" option in the sidebar!
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
            st.info("💡 Try using the 'Upload Your Own CSV' option instead!")
            return None, None, None
    
    def _load_custom_csv(self):
        """Load custom CSV file uploaded by user"""
        uploaded_file = st.sidebar.file_uploader("Choose a CSV file", type="csv")
        
        if uploaded_file is not None:
            try:
                df = pd.read_csv(uploaded_file)
                info = f"Uploaded dataset: {uploaded_file.name}"
                return df, info, "custom"
            except Exception as e:
                st.error(f"Error reading CSV file: {str(e)}")
                return None, None, None
        
        return None, None, None

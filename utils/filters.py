"""
Filter management module for applying interactive filters to datasets
"""

import streamlit as st
import numpy as np


class FilterManager:
    """Manages filters for different dataset types"""
    
    def __init__(self, df, dataset_type):
        self.df = df
        self.dataset_type = dataset_type
        self.filtered_df = df.copy()
    
    def apply_filters(self):
        """
        Apply dataset-specific filters
        
        Returns:
            DataFrame: Filtered dataset
        """
        st.sidebar.markdown("---")
        st.sidebar.subheader("🔧 Filters")
        
        if self.dataset_type == "netflix":
            return self._apply_netflix_filters()
        else:
            return self._apply_custom_filters()
    
    def _apply_netflix_filters(self):
        """Apply filters specific to Netflix dataset"""
        # Content type filter (Movie or TV Show)
        type_options = st.sidebar.multiselect(
            "Select Content Type:",
            options=self.df['type'].unique().tolist(),
            default=self.df['type'].unique().tolist()
        )
        self.filtered_df = self.filtered_df[self.filtered_df['type'].isin(type_options)]
        
        # Rating filter
        if 'rating' in self.df.columns:
            all_ratings = sorted(self.df['rating'].dropna().unique().tolist())
            rating_options = st.sidebar.multiselect(
                "Select Rating:",
                options=all_ratings,
                default=all_ratings  # Include ALL ratings by default
            )
            self.filtered_df = self.filtered_df[self.filtered_df['rating'].isin(rating_options)]
        
        # Release year range slider
        if 'release_year' in self.df.columns:
            min_year = int(self.df['release_year'].min())
            max_year = int(self.df['release_year'].max())
            year_range = st.sidebar.slider(
                "Release Year Range:",
                min_year,
                max_year,
                (min_year, max_year)
            )
            self.filtered_df = self.filtered_df[
                (self.filtered_df['release_year'] >= year_range[0]) &
                (self.filtered_df['release_year'] <= year_range[1])
            ]
        
        return self.filtered_df
    
    def _apply_custom_filters(self):
        """Apply generic filters for custom uploaded datasets"""
        numeric_cols = self.filtered_df.select_dtypes(include=[np.number]).columns.tolist()
        categorical_cols = self.filtered_df.select_dtypes(include=['object']).columns.tolist()
        
        if categorical_cols:
            selected_cat_col = st.sidebar.selectbox(
                "Select Categorical Column:",
                categorical_cols
            )
            cat_values = st.sidebar.multiselect(
                f"Filter {selected_cat_col}:",
                options=self.df[selected_cat_col].unique().tolist(),
                default=self.df[selected_cat_col].unique().tolist()
            )
            self.filtered_df = self.filtered_df[self.filtered_df[selected_cat_col].isin(cat_values)]
        
        return self.filtered_df
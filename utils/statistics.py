"""
Statistics module for displaying data summaries and metrics
"""

import streamlit as st
import numpy as np


class StatisticsManager:
    """Manages statistical summaries and metrics for datasets"""
    
    def __init__(self, df, dataset_type):
        self.df = df
        self.dataset_type = dataset_type
    
    def display_top_metrics(self):
        """Display key metrics based on dataset type"""
        col1, col2, col3 = st.columns(3)
        
        if self.dataset_type == "netflix":
            self._display_netflix_metrics(col1, col2, col3)
        else:
            self._display_generic_metrics(col1, col2, col3)
    
    def display_summary_statistics(self):
        """Display detailed statistical summaries"""
        col1, col2 = st.columns(2)
        
        with col1:
            self._display_numerical_summary()
        
        with col2:
            self._display_categorical_summary()
    
    def _display_netflix_metrics(self, col1, col2, col3):
        """Display metrics specific to Netflix dataset"""
        with col1:
            st.metric("🎬 Total Titles", len(self.df))
        with col2:
            movie_count = len(self.df[self.df['type'] == 'Movie'])
            st.metric("🎥 Movies", movie_count)
        with col3:
            tv_count = len(self.df[self.df['type'] == 'TV Show'])
            st.metric("📺 TV Shows", tv_count)
    
    def _display_generic_metrics(self, col1, col2, col3):
        """Display generic metrics for custom datasets"""
        with col1:
            st.metric("📊 Total Records", len(self.df))
        with col2:
            st.metric("📋 Total Columns", len(self.df.columns))
        with col3:
            numeric_cols = self.df.select_dtypes(include=[np.number]).columns
            st.metric("🔢 Numeric Columns", len(numeric_cols))
    
    def _display_numerical_summary(self):
        """Display numerical statistics summary"""
        st.subheader("📈 Numerical Summary")
        numeric_cols = self.df.select_dtypes(include=[np.number]).columns
        
        if len(numeric_cols) > 0:
            st.dataframe(self.df[numeric_cols].describe(), use_container_width=True)
        else:
            st.info("No numerical columns available")
    
    def _display_categorical_summary(self):
        """Display categorical statistics summary"""
        st.subheader("🏷️ Categorical Summary")
        categorical_cols = self.df.select_dtypes(include=['object']).columns
        
        if len(categorical_cols) > 0:
            for col in categorical_cols[:3]:  # Show first 3 categorical columns
                st.write(f"**{col}:**")
                value_counts = self.df[col].value_counts().head(10)
                st.dataframe(value_counts, use_container_width=True)
        else:
            st.info("No categorical columns available")

"""
Interactive Data Visualization Explorer
A modular Streamlit application for data analysis and visualization
"""

import streamlit as st
from utils.config import configure_page, apply_custom_styling
from utils.data_loader import DataLoader
from utils.filters import FilterManager
from utils.visualizations import VisualizationManager
from utils.statistics import StatisticsManager


def main():
    """Main application entry point"""
    
    # Configure page settings
    configure_page()
    
    # Apply custom styling
    apply_custom_styling()
    
    # Display header
    st.markdown("<h1>🍿 Netflix Streamlit Visualization</h1>", unsafe_allow_html=True)
    
    # Initialize sidebar
    st.sidebar.title("🎯 Control Panel")
    st.sidebar.markdown("---")
    
    # Load dataset
    data_loader = DataLoader()
    df, dataset_info, dataset_type = data_loader.load_data()
    
    if df is None:
        st.info("👆 Please upload a CSV file to begin exploring your data.")
        return
    
    # Display dataset info
    st.info(f"ℹ️ {dataset_info}")
    
    # Apply filters
    filter_manager = FilterManager(df, dataset_type)
    filtered_df = filter_manager.apply_filters()
    
    # Display sidebar metrics
    st.sidebar.markdown("---")
    st.sidebar.metric("Total Records", len(df))
    st.sidebar.metric("Filtered Records", len(filtered_df))
    
    # Display summary metrics
    stats_manager = StatisticsManager(filtered_df, dataset_type)
    stats_manager.display_top_metrics()
    
    st.markdown("---")
    
    # Display visualizations
    st.header("📈 Data Visualizations")
    viz_manager = VisualizationManager(filtered_df, dataset_type)
    viz_manager.display_visualizations()
    
    # Display data summary
    st.markdown("---")
    st.header("📊 Data Summary Statistics")
    stats_manager.display_summary_statistics()
    
    # Footer
    st.markdown("---")
    st.markdown(
        """
        <div style='text-align: center; color: #7f8c8d; padding: 20px;'>
            <p>Built with 🍿 using Streamlit | Netflix Streamlit Visualization</p>
        </div>
        """,
        unsafe_allow_html=True
    )


if __name__ == "__main__":
    main()
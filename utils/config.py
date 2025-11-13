"""
Configuration module for page settings and custom styling
"""

import streamlit as st


def configure_page():
    """Configure Streamlit page settings"""
    st.set_page_config(
        page_title="Netflix Streamlit Visualization",
        page_icon="🍿",
        layout="wide",
        initial_sidebar_state="expanded"
    )


def apply_custom_styling():
    """Apply custom CSS styling to the application"""
    st.markdown("""
        <style>
        .main {
            background-color: #141414;
        }
        .stApp {
            max-width: 100%;
            background-color: #141414;
        }
        h1 {
            color: white;
            text-align: center;
            padding: 20px;
            background: linear-gradient(90deg, #E50914 0%, #B20710 100%);
            color: white;
            border-radius: 10px;
            margin-bottom: 30px;
            box-shadow: 0 4px 6px rgba(229, 9, 20, 0.3);
        }
        h2 {
            color: #E50914;
            border-bottom: 2px solid #E50914;
            padding-bottom: 10px;
        }
        h3 {
            color: #E50914;
        }
        .metric-card {
            background-color: #1f1f1f;
            padding: 20px;
            border-radius: 10px;
            box-shadow: 0 2px 4px rgba(0,0,0,0.3);
            border: 1px solid #333;
        }
        .stMetric {
            background-color: #1f1f1f;
            padding: 15px;
            border-radius: 8px;
            border-left: 4px solid #E50914;
        }
        .stMetric label {
            color: #ffffff !important;
        }
        .stMetric .metric-value {
            color: #E50914 !important;
        }
        /* Sidebar styling */
        [data-testid="stSidebar"] {
            background-color: #000000;
        }
        [data-testid="stSidebar"] .stMarkdown {
            color: #ffffff;
        }
        /* Info box styling */
        .stAlert {
            background-color: #1f1f1f;
            border: 1px solid #E50914;
            color: #ffffff;
        }
        /* Tab styling */
        .stTabs [data-baseweb="tab-list"] {
            gap: 8px;
            background-color: #1f1f1f;
            padding: 10px;
            border-radius: 8px;
        }
        .stTabs [data-baseweb="tab"] {
            background-color: #000000;
            color: #ffffff;
            border-radius: 4px;
            padding: 8px 16px;
        }
        .stTabs [aria-selected="true"] {
            background-color: #E50914;
            color: white;
        }
        /* Dataframe styling */
        .stDataFrame {
            background-color: #1f1f1f;
        }
        /* Text color */
        .stMarkdown, p, label {
            color: #ffffff;
        }
        </style>
        """, unsafe_allow_html=True)
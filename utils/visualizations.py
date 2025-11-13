"""
Visualization module for creating interactive charts and plots
"""

import streamlit as st
import plotly.express as px


class VisualizationManager:
    """Manages visualizations for different dataset types"""
    
    def __init__(self, df, dataset_type):
        self.df = df
        self.dataset_type = dataset_type
    
    def display_visualizations(self):
        """Display visualizations in tabbed interface"""
        tab1, tab2, tab3, tab4, tab5 = st.tabs(["📊 Bar Chart", "📈 Histogram", "🥧 Pie Chart", "🗺️ Map", "📋 Data Table"])
        
        with tab1:
            self._display_primary_chart()
        
        with tab2:
            self._display_secondary_chart()
        
        with tab3:
            self._display_tertiary_chart()
        
        with tab4:
            self._display_map_chart()
        
        with tab5:
            self._display_data_table()
    
    def _display_primary_chart(self):
        """Display primary visualization based on dataset type"""
        if self.dataset_type == "netflix":
            self._create_netflix_type_chart()
        else:
            self._create_generic_chart()
    
    def _display_secondary_chart(self):
        """Display secondary visualization based on dataset type"""
        if self.dataset_type == "netflix":
            self._create_netflix_year_chart()
        else:
            self._create_generic_histogram()
    
    def _display_tertiary_chart(self):
        """Display tertiary visualization based on dataset type"""
        if self.dataset_type == "netflix":
            self._create_netflix_genre_pie()
        else:
            self._create_generic_pie()
    
    def _display_map_chart(self):
        """Display map visualization based on dataset type"""
        if self.dataset_type == "netflix":
            self._create_netflix_country_map()
        else:
            st.info("Map visualization is only available for Netflix dataset")
    
    def _display_data_table(self):
        """Display filtered data table with download option"""
        st.subheader("📋 Filtered Data Preview")
        st.dataframe(self.df.head(100), use_container_width=True)
        
        # Download button
        csv = self.df.to_csv(index=False)
        st.download_button(
            label="⬇️ Download Filtered Data as CSV",
            data=csv,
            file_name=f"filtered_data_{self.dataset_type}.csv",
            mime="text/csv"
        )
    
    # Netflix visualizations
    def _create_netflix_type_chart(self):
        """Create bar chart for Netflix content types"""
        type_counts = self.df['type'].value_counts().reset_index()
        type_counts.columns = ['type', 'count']
        
        fig = px.bar(
            type_counts,
            x='type',
            y='count',
            title="Netflix Content Distribution: Movies vs TV Shows",
            labels={'type': 'Content Type', 'count': 'Number of Titles'},
            template="plotly_dark",
            color='type',
            color_discrete_map={'Movie': '#E50914', 'TV Show': '#B20710'}
        )
        fig.update_layout(
            height=500,
            paper_bgcolor='#141414',
            plot_bgcolor='#1f1f1f',
            font=dict(color='white'),
            title_font=dict(size=20, color='#E50914')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    def _create_netflix_year_chart(self):
        """Create histogram for Netflix release years"""
        fig = px.histogram(
            self.df,
            x='release_year',
            color='type',
            title="Content Release Years Distribution",
            labels={'release_year': 'Release Year', 'count': 'Number of Titles'},
            template="plotly_dark",
            nbins=30,
            color_discrete_map={'Movie': '#E50914', 'TV Show': '#B20710'}
        )
        fig.update_layout(
            height=500,
            paper_bgcolor='#141414',
            plot_bgcolor='#1f1f1f',
            font=dict(color='white'),
            title_font=dict(size=20, color='#E50914')
        )
        st.plotly_chart(fig, use_container_width=True)
    
    def _create_netflix_genre_pie(self):
        """Create pie chart for Netflix genres distribution"""
        if 'listed_in' in self.df.columns:
            # Split genres (they're comma-separated) and count them
            import pandas as pd
            
            # Split the listed_in column and flatten into individual genres
            all_genres = []
            for genres in self.df['listed_in'].dropna():
                # Split by comma and strip whitespace
                genre_list = [g.strip() for g in str(genres).split(',')]
                all_genres.extend(genre_list)
            
            # Count genre occurrences
            genre_counts = pd.Series(all_genres).value_counts().head(10)
            
            fig = px.pie(
                values=genre_counts.values,
                names=genre_counts.index,
                title="Top 10 Netflix Genres Distribution",
                template="plotly_dark",
                color_discrete_sequence=px.colors.sequential.Reds_r
            )
            fig.update_layout(
                height=500,
                paper_bgcolor='#141414',
                font=dict(color='white'),
                title_font=dict(size=20, color='#E50914')
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Genre (listed_in) column not available for pie chart")
    
    def _create_netflix_country_map(self):
        """Create world map visualization for Netflix content by country"""
        if 'country' in self.df.columns:
            import pandas as pd
            
            # Count content by country (handling multiple countries per title)
            country_counts = {}
            
            for countries in self.df['country'].dropna():
                # Split by comma and strip whitespace
                country_list = [c.strip() for c in str(countries).split(',')]
                for country in country_list:
                    if country:
                        country_counts[country] = country_counts.get(country, 0) + 1
            
            # Create dataframe for map
            map_df = pd.DataFrame(list(country_counts.items()), columns=['country', 'count'])
            map_df = map_df.sort_values('count', ascending=False)
            
            # Create choropleth map
            fig = px.choropleth(
                map_df,
                locations='country',
                locationmode='country names',
                color='count',
                hover_name='country',
                hover_data={'count': True, 'country': False},
                title='Netflix Content Distribution by Country',
                color_continuous_scale='Reds',
                labels={'count': 'Number of Titles'}
            )
            
            fig.update_layout(
                height=600,
                paper_bgcolor='#141414',
                geo=dict(
                    bgcolor='#1f1f1f',
                    lakecolor='#141414',
                    landcolor='#2a2a2a',
                    showcountries=True,
                    countrycolor='#444444'
                ),
                font=dict(color='white'),
                title_font=dict(size=20, color='#E50914')
            )
            
            st.plotly_chart(fig, use_container_width=True)
            
            # Show top 10 countries table
            st.subheader("Top 10 Countries by Content Count")
            top_countries = map_df.head(10)
            st.dataframe(top_countries, use_container_width=True, hide_index=True)
        else:
            st.info("Country column not available for map visualization")
    
    # Generic visualizations for custom datasets
    def _create_generic_chart(self):
        """Create generic chart for custom datasets"""
        numeric_cols = self.df.select_dtypes(include=['number']).columns.tolist()
        
        if len(numeric_cols) >= 2:
            fig = px.scatter(
                self.df,
                x=numeric_cols[0],
                y=numeric_cols[1],
                title=f"{numeric_cols[1]} vs {numeric_cols[0]}",
                template="plotly_dark",
                color_discrete_sequence=['#E50914']
            )
            fig.update_layout(
                height=500,
                paper_bgcolor='#141414',
                plot_bgcolor='#1f1f1f',
                font=dict(color='white'),
                title_font=dict(size=20, color='#E50914')
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("Not enough numerical columns for visualization")
    
    def _create_generic_histogram(self):
        """Create generic histogram for custom datasets"""
        numeric_cols = self.df.select_dtypes(include=['number']).columns.tolist()
        
        if len(numeric_cols) >= 1:
            fig = px.histogram(
                self.df,
                x=numeric_cols[0],
                title=f"Distribution of {numeric_cols[0]}",
                template="plotly_dark",
                color_discrete_sequence=['#E50914']
            )
            fig.update_layout(
                height=500,
                paper_bgcolor='#141414',
                plot_bgcolor='#1f1f1f',
                font=dict(color='white'),
                title_font=dict(size=20, color='#E50914')
            )
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No numerical columns available for histogram")
    
    def _create_generic_pie(self):
        """Create generic pie chart for custom datasets"""
        categorical_cols = self.df.select_dtypes(include=['object']).columns.tolist()
        
        if len(categorical_cols) >= 1:
            col = categorical_cols[0]
            value_counts = self.df[col].value_counts().head(10)
            
            fig = px.pie(
                values=value_counts.values,
                names=value_counts.index,
                title=f"Distribution of {col} (Top 10)",
                template="plotly_dark",
                color_discrete_sequence=px.colors.sequential.Reds_r
            )
            fig.update_layout(
                height=500,
                paper_bgcolor='#141414',
                font=dict(color='white'),
                title_font=dict(size=20, color='#E50914')
            )
            fig.update_traces(textposition='inside', textinfo='percent+label')
            st.plotly_chart(fig, use_container_width=True)
        else:
            st.info("No categorical columns available for pie chart")
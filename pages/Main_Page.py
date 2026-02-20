import streamlit as st
from main_tabs import (
    numerical_insights,
    general_insights,
    final_recomds,
)
import pandas as pd
# Apply global style and logo
#  Page title
st.set_page_config(page_title="🏥 Bupa Datathon Challenge", layout="wide")
st.title("🏥 Bupa Datathon Challenge")

# Get filtered dataframe
df_filtered = pd.read_parquet("data/final_df.parquet")


# Create tabs
tab0, tab1, tab2 = st.tabs([
    "🌍 General Insights",
    "📊 Numerical Insights",
    "🗺️ Final Recommendations",
])

# Render each tab content
with tab0:
    general_insights.render(df_filtered)

with tab1:
    numerical_insights.render(df_filtered)

with tab2:
    final_recomds.render()



        # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>Bupa Datathon Challenge Dashboard | 2025</div>", 
        unsafe_allow_html=True
    )


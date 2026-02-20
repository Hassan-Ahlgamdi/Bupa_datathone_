import streamlit as st
import pandas as pd

# Set page config
st.set_page_config(
    page_title="Bupa Datathon Challenge",
    page_icon="🏥",
    layout="wide"
)

# Main title - centered
col1, col2, col3 = st.columns([1, 2, 1])
with col2:
    st.image("../Bupa_Arabia_logo.jpg", width=300)
    st.title("🏥 Bupa Datathon Challenge")

# Custom CSS for centered static image
st.markdown("""
<style>
.centered-image {
    display: flex;
    justify-content: center;
    align-items: center;
}
.centered-image img {
    max-width: 300px;
    height: auto;
    pointer-events: none;
    user-select: none;
}
</style>
""", unsafe_allow_html=True)

# Create tabs
tab1, tab2 = st.tabs(["Landing Page", "Dataset Overview"])

with tab1:
    # Subtitle and description
    st.markdown("""
    ### Welcome to Our Data Analysis Dashboard

    In this simple application, we will dive into the insights we found in our final cleaned dataset 
    as well as the recommendations derived from our comprehensive analysis of the Bupa health data.

    Explore our findings and discover actionable insights that can help improve healthcare outcomes 
    and operational efficiency.
    """)

    # Add some spacing
    st.markdown("<br>", unsafe_allow_html=True)

    # Launch Dashboard button
    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("🚀 Launch Dashboard"):
            st.switch_page("pages/Main_Page.py")

    # Additional information section
    st.markdown("---")
    st.markdown("""
    ### What You'll Find in the Dashboard:
    - **Data Insights**: Key findings from our cleaned dataset
    - **Visualizations**: Interactive charts and graphs
    - **Recommendations**: Actionable insights for healthcare improvement
    - **Analysis**: Comprehensive data exploration results
    """)

    # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>Bupa Datathon Challenge Dashboard | 2025</div>", 
        unsafe_allow_html=True
    )

with tab2:
    st.header("📌 Dataset Overview")
    
    # Load the dataset
    df_filtered = pd.read_parquet("data/final_df.parquet")
    
    # Three metrics
    col1, col2, col3 = st.columns(3)
    
    with col1:
        avg_claims = df_filtered['CLAIMS_AMOUNT'].mean()
        st.metric("💰 Avg Claims Amount", f"${avg_claims:,.2f}")
    
    with col2:
        total_records = df_filtered.shape[0]
        st.metric("📊 Total Records", f"{total_records:,}")
    
    with col3:
        unique_providers = df_filtered['PROV_CODE'].nunique()
        st.metric("🏥 Unique Providers", f"{unique_providers:,}")
    
    st.markdown("---")
    
    st.markdown("""
    This dataset represents our **final cleaned and preprocessed Bupa health data** after comprehensive data cleaning, preprocessing, and feature engineering processes.
    
    The dataset contains various healthcare claims and patient information that has been transformed and enhanced for analysis.
    """)
    
    st.subheader("📂 Dataset Preview")
    preview_df = df_filtered.head().reset_index(drop=True)
    preview_df.index = preview_df.index + 1
    preview_df.index.name = "Index"
    st.dataframe(preview_df)
    
    st.subheader("📈 Dataset Shape & Columns")
    st.markdown(f"""
    - 🔢 **Rows**: `{df_filtered.shape[0]:,}`
    - 📊 **Columns**: `{df_filtered.shape[1]}`
    
    **Note**: This is the final dataset after all cleaning, preprocessing, and feature engineering steps.
    """)
    
    st.subheader("📋 Column Information")
    col_info = pd.DataFrame({
        'Column': df_filtered.columns,
        'Data Type': df_filtered.dtypes,
        'Non-Null Count': df_filtered.count(),
        'Null Count': df_filtered.isnull().sum()
    })
    st.dataframe(col_info)
    
    st.subheader("📊 Descriptive Statistics")
    numeric_cols = df_filtered.select_dtypes(include=['number'])
    st.dataframe(numeric_cols.describe())

  
    st.header("🎯 Selected Features for Predictive Models")
    st.markdown("""
    The following features have been selected for our predictive modeling after thorough analysis and feature engineering:
    """)
      
    # Selected features organized by type
    st.markdown("""
    #### 🔄 Categorical Features (One-Hot Encoded)
    | **Feature** | **Description** |
    |-------------|-----------------|
    | `STATUS` | Patient/claim status |
    | `GENDER` | Patient gender |
    | `CLAIM_TYPE` | Type of medical claim |
    | `PROVIDER_REGION` | Healthcare provider region |
    
    
    
    #### 🔢 Numerical Features
    | **Feature** | **Description** |
    |-------------|-----------------|
    | `AGE` | Patient age |
    | `COUNT_DISTINCT_of_VOU_NO` | Count of distinct voucher numbers |
    | `PREAUTH_AMOUNT` | Pre-authorization amount |
    | `NUMBER_OF_PA_EPISODES` | Number of pre-auth episodes |
    | `DIAG_CODE_COUNT_LOG` | Log-transformed diagnosis code count |
    | `CLAIMS_AMOUNT_LOG` | Log-transformed claims amount |
    
                

    #### ✅ Binary Features
    | **Feature** | **Description** |
    |-------------|-----------------|
    | `HAS_PREAUTH` | Whether claim has pre-authorization (0/1) |
    | `IS_COMMON_DIAG` | Whether diagnosis is common (0/1) |
    

      
    #### 📍 Ranked Features
    | **Feature** | **Description** |
    |-------------|-----------------|
    | `PLAN_NETWORK_MAPPED` | The ranks of each plan based on the given order 1-10 |
                """)
    



        # Footer
    st.markdown("<br><br>", unsafe_allow_html=True)
    st.markdown("---")
    st.markdown(
        "<div style='text-align: center; color: gray;'>Bupa Datathon Challenge Dashboard | 2025</div>", 
        unsafe_allow_html=True
    )


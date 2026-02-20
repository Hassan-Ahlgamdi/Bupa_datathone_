import streamlit as st
import plotly.express as px
import pandas as pd

def render(df_filtered):
    """Render general insights with 5 different charts using plotly.express"""
    
    # Calculate key metrics
    avg_claims_amount = df_filtered["CLAIMS_AMOUNT"].mean()
    avg_age = df_filtered["AGE"].mean()
    total_claims = len(df_filtered)
    avg_preauth_amount = df_filtered["PREAUTH_AMOUNT"].mean()

    # Display metrics
    col1, col2, col3, col4 = st.columns(4)
    
    col1.metric("💰 Avg Claims Amount", f"${avg_claims_amount:,.2f}")
    col2.metric("👥 Avg Age", f"{avg_age:.1f} years")
    col3.metric("📋 Total Claims", f"{total_claims:,}")
    col4.metric("🏥 Avg Preauth Amount", f"${avg_preauth_amount:,.2f}")

    # Chart 1: Claims Amount Distribution by Nationality - Bar chart for top 10
    st.subheader("1: 🌍 Claims Amount Distribution by Nationality (Top 10)")
    
    # Calculate average claims amount by nationality and get top 10
    nationality_claims = (df_filtered.groupby('NATIONALITY')['CLAIMS_AMOUNT']
                         .mean()
                         .sort_values(ascending=True)
                         .reset_index()
                         .tail(10))
    
    fig1 = px.bar(
        nationality_claims,
        x='NATIONALITY',
        y='CLAIMS_AMOUNT',
        title="Average Claims Amount by Nationality (Top 10)",
        labels={'CLAIMS_AMOUNT': 'Average Claims Amount ($)', 'NATIONALITY': 'Nationality'},
        color='CLAIMS_AMOUNT',
        color_continuous_scale='Blues'
    )
    
    fig1.update_layout(
        xaxis_tickangle=-45,
        margin=dict(t=40, b=100)
    )
    
    st.plotly_chart(fig1, use_container_width=True)

    # Chart 2: Age Distribution and Claims Relationship - Scatter plot with trendline
    st.subheader("2: 👥 Age Distribution and Claims Relationship")
    
    fig2 = px.scatter(
        df_filtered,
        x='AGE',
        y='CLAIMS_AMOUNT',
        color='GENDER',
        title="Claims Amount vs Age with Gender Distribution",
        labels={'AGE': 'Age (Years)', 'CLAIMS_AMOUNT': 'Claims Amount ($)'},
        trendline="ols",  # Add trendline
        hover_data=['NATIONALITY', 'CLAIM_TYPE']
    )
    
    fig2.update_layout(margin=dict(t=40, b=40))
    
    st.plotly_chart(fig2, use_container_width=True)

    # Chart 3: Claims by Service Type - Pie chart
    st.subheader("3: 🏥 Claims Distribution by Service Type")
    
    service_type_counts = df_filtered['SERV_TYPE'].value_counts().reset_index()
    service_type_counts.columns = ['SERV_TYPE', 'Count']
    
    fig3 = px.pie(
        service_type_counts,
        values='Count',
        names='SERV_TYPE',
        title="Distribution of Claims by Service Type"
    )
    
    st.plotly_chart(fig3, use_container_width=True)

    # Chart 4: Claims Amount by Marital Status and Gender - Box plot
    st.subheader("4: 💑 Claims Amount Distribution by Marital Status and Gender")
    
    fig4 = px.box(
        df_filtered,
        x='MARITAL_STATUS',
        y='CLAIMS_AMOUNT',
        color='GENDER',
        title="Claims Amount Distribution by Marital Status and Gender",
        labels={'CLAIMS_AMOUNT': 'Claims Amount ($)', 'MARITAL_STATUS': 'Marital Status'}
    )
    
    fig4.update_layout(margin=dict(t=40, b=40))
    
    st.plotly_chart(fig4, use_container_width=True)
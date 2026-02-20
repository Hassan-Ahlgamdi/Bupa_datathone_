import streamlit as st
import plotly.express as px
import pandas as pd

def render(df_filtered):
    """Render categorical insights with numerical analysis."""
    
    # Calculate key metrics for this tab
    # Calculate key metrics for this tab
    common_diag_avg = int(df_filtered[df_filtered['IS_COMMON_DIAG'] == 1]['CLAIMS_AMOUNT'].count().astype(int)/1000)
    rare_diag_avg = int(df_filtered[df_filtered['IS_COMMON_DIAG'] == 0]['CLAIMS_AMOUNT'].count().astype(int)/1000)

    col1, col2 = st.columns(2)

    col1.metric("🔍 Common Diagnosis Count Claims", f"{common_diag_avg:}K")
    col2.metric("🔎 Rare Diagnosis Count Claims", f"{rare_diag_avg}K")

    st.markdown("---")

    # 1. IS_COMMON_DIAG vs Claims Average
    st.subheader("1: 🔍 Common vs Rare Diagnosis Claims Comparison")

    # Get actual counts for each category
    common_count = len(df_filtered[df_filtered['IS_COMMON_DIAG'] == 1])
    rare_count = len(df_filtered[df_filtered['IS_COMMON_DIAG'] == 0])

    diag_comparison = df_filtered.groupby('IS_COMMON_DIAG')['CLAIMS_AMOUNT'].mean().reset_index()
    diag_comparison['count'] = diag_comparison['IS_COMMON_DIAG'].map({0: rare_count, 1: common_count})
    diag_comparison['IS_COMMON_DIAG'] = diag_comparison['IS_COMMON_DIAG'].map({0: 'Rare Diagnosis', 1: 'Common Diagnosis'})

    fig1 = px.bar(
        diag_comparison,
        x='IS_COMMON_DIAG',
        y='CLAIMS_AMOUNT',
        title="Average Claims Amount: Common vs Rare Diagnoses",
        labels={'CLAIMS_AMOUNT': 'Average Claims Amount ($)', 'IS_COMMON_DIAG': 'Diagnosis Type'},
        color='IS_COMMON_DIAG',
        color_discrete_map={'Common Diagnosis': '#1f77b4', 'Rare Diagnosis': '#ff7f0e'}
    )



    st.plotly_chart(fig1, use_container_width=True)
    
    # 2. Age Groups vs Claims Amount
    st.subheader("2: 👥 Claims Analysis by Age Groups")
    
    # Create age groups
    df_age_groups = df_filtered.copy()
    df_age_groups['Age_Group'] = pd.cut(
        df_age_groups['AGE'], 
        bins=[0, 20, 40, 60, 100], 
        labels=['0-20', '21-40', '41-60', '60+'],
        include_lowest=True
    )
    
    age_analysis = df_age_groups.groupby('Age_Group')['CLAIMS_AMOUNT'].agg(['mean', 'median', 'count']).reset_index()
    
    fig2 = px.box(
        df_age_groups,
        x='Age_Group',
        y='CLAIMS_AMOUNT',
        title="Claims Amount Distribution by Age Groups",
        labels={'CLAIMS_AMOUNT': 'Claims Amount ($)', 'Age_Group': 'Age Group'},
        color='Age_Group',
        color_discrete_sequence=px.colors.qualitative.Set2
    )
    
    fig2.update_layout(margin=dict(t=40, b=40))
    
    st.plotly_chart(fig2, use_container_width=True)
    
    # Show summary table
    st.write("**Age Group Statistics:**")
    st.dataframe(age_analysis.round(2), use_container_width=True)
    
    # 3. Provider Practice Type Analysis
    st.subheader("3: 🏥 Provider Practice Type Claims Distribution")

    practice_analysis = (df_filtered.groupby('PROVIDER_PRACTICE')
                        .agg({
                            'CLAIMS_AMOUNT': ['mean', 'sum', 'count']
                        }).round(2))

    practice_analysis.columns = ['avg_claims', 'total_claims', 'claim_count']
    practice_analysis = practice_analysis.reset_index().sort_values('claim_count', ascending=True)  # Sort by count, ascending for bottom to top

    fig3 = px.bar(
        practice_analysis.tail(10),  # Top 10 by count
        x='claim_count',
        y='PROVIDER_PRACTICE',
        orientation='h',
        title="Provider Practice Types by Claim Count (Top 10)",
        labels={'claim_count': 'Number of Claims', 'PROVIDER_PRACTICE': 'Provider Practice'},
        color='avg_claims',
        color_continuous_scale='Blues',
        hover_data={'avg_claims': ':.2f', 'claim_count': True}
    )

    # Add count values on the right of bars
    fig3.update_traces(text=practice_analysis.tail(10)['claim_count'], textposition='outside')

    fig3.update_layout(
        height=600,
        margin=dict(t=40, b=40, l=200)
    )

    st.plotly_chart(fig3, use_container_width=True)
    

# Bupa Datathon Challenge Dashboard

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.50.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

An interactive data analysis dashboard built with Streamlit for the Bupa Datathon Challenge. This application provides comprehensive insights into healthcare claims data, enabling better understanding of patient demographics, claim patterns, and operational trends.

## Overview

This dashboard analyzes healthcare claims data from Bupa Arabia, presenting key insights through interactive visualizations and actionable recommendations. The application is designed to help identify patterns in healthcare utilization, analyze claim distributions, and provide data-driven recommendations for improving predictions and operational efficiency.

## Features

### General Insights

- **Key Metrics Dashboard**: Track average claims amount, patient age, total claims, and pre-authorization amounts
- **Nationality Analysis**: Visualize claims distribution across different nationalities (Top 10)
- **Age vs Claims Relationship**: Scatter plots showing correlation between patient age and claim amounts
- **Trend Analysis**: Identify patterns in healthcare utilization across different demographic groups

### Numerical Insights

- **Diagnosis Type Analysis**: Compare common vs rare diagnosis claim patterns
- **Age Group Segmentation**: Analyze claims distribution across different age brackets
- **Statistical Comparisons**: Deep dive into numerical patterns and correlations
- **Volume Metrics**: Track claim counts and averages for different diagnosis categories

### Final Recommendations

- **Data Quality Enhancement**: Recommendations for improving data collection and preprocessing
- **Feature Engineering**: Suggestions for additional data points to improve predictive modeling
- **Strategic Insights**: Actionable recommendations based on comprehensive data analysis

## Getting Started

### Prerequisites

- Python 3.8 or higher
- UV package manager (recommended) or pip

### Installation

1. Clone the repository:

```bash
git clone https://github.com/Hassan-Ahlgamdi/Bupa_datathone_.git
cd Bupa_datathone_
```

2. Install dependencies using UV:

```bash
uv pip install -r requirements.txt
```

Or using pip:

```bash
pip install -r requirements.txt
```

### Running the Dashboard

Launch the Streamlit application:

```bash
streamlit run pages/Main_Page.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

## Project Structure

```
Bupa_Dash/
│
├── data/                          # Data directory
│   └── final_df.parquet          # Processed healthcare claims dataset
│
├── main_tabs/                     # Tab modules for the dashboard
│   ├── general_insights.py       # General analytics and visualizations
│   ├── numerical_insights.py     # Numerical analysis and statistics
│   └── final_recomds.py          # Recommendations and insights
│
├── pages/                         # Streamlit pages
│   └── Main_Page.py              # Main dashboard page
│
├── Landing_Page.py               # Landing page with project overview
├── main.py                       # Core application logic
├── requirements.txt              # Project dependencies
├── pyproject.toml               # Project configuration
└── README.md                    # Project documentation
```

## Data

The dashboard uses processed healthcare claims data (`final_df.parquet`) containing:

- **Patient Demographics**: Age, nationality, and other demographic information
- **Claims Information**: Claim amounts, pre-authorization amounts, and claim types
- **Diagnosis Data**: Common vs rare diagnosis classifications
- **Temporal Data**: Claim timing and patterns

## Technologies Used

- **Streamlit**: Interactive web application framework
- **Plotly**: Interactive data visualizations
- **Pandas**: Data manipulation and analysis
- **PyArrow**: Efficient parquet file handling
- **NumPy**: Numerical computing
- **Scikit-learn**: Statistical analysis and modeling

## Key Metrics Tracked

- **Average Claims Amount**: Mean claim value across all records
- **Average Patient Age**: Demographic age distribution
- **Total Claims**: Overall volume of claims processed
- **Average Pre-auth Amount**: Mean pre-authorization values
- **Common Diagnosis Claims**: Volume of common diagnosis cases
- **Rare Diagnosis Claims**: Volume of rare diagnosis cases

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

## License

This project was developed for the Bupa Datathon Challenge 2025.

## Authors

**Hassan Alghamdi**

**Yasser Albogami**

Developed for the Bupa Datathon Challenge

## Links

- [GitHub Repository](https://github.com/Hassan-Ahlgamdi/Bupa_datathone_)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)

---

**Bupa Datathon Challenge Dashboard | 2025**

# Bupa Arabia Datathon: Predicting Health Insurance Claims

![Python](https://img.shields.io/badge/python-v3.8+-blue.svg)
![Streamlit](https://img.shields.io/badge/streamlit-1.50.0-red.svg)
![License](https://img.shields.io/badge/license-MIT-green.svg)
![Status](https://img.shields.io/badge/status-active-success.svg)

## Project Overview

This repository contains the complete solution for the Bupa Arabia Datathon. The primary objective of this project was to develop a machine learning model to accurately predict monthly health insurance claim amounts for financial reserving purposes. The project involved a comprehensive workflow, including data cleaning, exploratory data analysis, feature engineering, and the evaluation of multiple predictive models. The final XGBoost model demonstrates a measurable improvement over baseline methods and provides key insights into the main drivers of claim costs.

Additionally, this project includes an interactive Streamlit dashboard that provides comprehensive insights into healthcare claims data, enabling better understanding of patient demographics, claim patterns, and operational trends.

---

## The Data

The analysis was based on three primary data sources provided by Bupa Arabia:

1.  **Claims Data:** Detailed records of individual claims.
2.  **Pre-authorization Data:** Information on pre-approved amounts for treatments.
3.  **Provider Information:** Details about the healthcare providers.

---

## Methodology

#### 1. Data Cleaning and Preprocessing

The initial datasets were cleaned to handle outliers, logical inconsistencies (such as batch periods preceding treatment periods), and missing values. The target variable, `CLAIMS_AMOUNT`, was log-transformed to normalize its distribution for more stable model training.

#### 2. Exploratory Data Analysis (EDA)

A thorough EDA was conducted to uncover key patterns. Major insights included the "Volume vs. Value" story, where overseas claims had a much higher average cost, and the identification of inpatient services and claim volume as significant cost drivers.

#### 3. Feature Engineering

Based on EDA insights, several new features were engineered to enhance the model's predictive power. This included creating binary flags like `IS_OVERSEAS` and `HAS_PREAUTH`. A key step was handling the high-cardinality `DIAG_CODE` feature by grouping rare categories and applying frequency encoding.

#### 4. Modeling and Evaluation

We evaluated several models, starting with a Linear Regression baseline and progressing to a more advanced XGBoost Regressor. A 5-fold cross-validation strategy was used to ensure the robustness of our results, with R-squared and RMSE as the primary evaluation metrics.

---

## Results

The final XGBoost model achieved an **R-squared of 0.48**, a substantial improvement over the 0.28 from our linear baseline. The model identified the following as the most important features for predicting claim costs:

- **CLAIM_TYPE_I (Inpatient Claims)**
- **COUNT_DISTINCT_of_VOU_NO (Volume of Services)**
- **PREAUTH_AMOUNT**

---

## Interactive Dashboard

This project includes a comprehensive Streamlit dashboard for visualizing and exploring the healthcare claims data.

### Dashboard Features

#### General Insights

- **Key Metrics Dashboard**: Track average claims amount, patient age, total claims, and pre-authorization amounts
- **Nationality Analysis**: Visualize claims distribution across different nationalities (Top 10)
- **Age vs Claims Relationship**: Scatter plots showing correlation between patient age and claim amounts
- **Trend Analysis**: Identify patterns in healthcare utilization across different demographic groups

#### Numerical Insights

- **Diagnosis Type Analysis**: Compare common vs rare diagnosis claim patterns
- **Age Group Segmentation**: Analyze claims distribution across different age brackets
- **Statistical Comparisons**: Deep dive into numerical patterns and correlations
- **Volume Metrics**: Track claim counts and averages for different diagnosis categories

#### Final Recommendations

- **Data Quality Enhancement**: Recommendations for improving data collection and preprocessing
- **Feature Engineering**: Suggestions for additional data points to improve predictive modeling
- **Strategic Insights**: Actionable recommendations based on comprehensive data analysis

---

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

Launch the Streamlit application from the Bupa_Dash directory:

```bash
streamlit run pages/Main_Page.py
```

The dashboard will open in your default web browser at `http://localhost:8501`

---

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
├── check.ipynb                    # Notebook for testing and validation
├── Landing_Page.py                # Landing page with project overview
├── main.py                        # Core application logic
├── requirements.txt               # Project dependencies
├── pyproject.toml                 # Project configuration
└── README.md                      # Project documentation
```

---

## Data Details

The dashboard uses processed healthcare claims data (`final_df.parquet`) containing:

- **Patient Demographics**: Age, nationality, and other demographic information
- **Claims Information**: Claim amounts, pre-authorization amounts, and claim types
- **Diagnosis Data**: Common vs rare diagnosis classifications
- **Temporal Data**: Claim timing and patterns

---

## Technologies Used

- **Python**: Core programming language
- **XGBoost**: Advanced machine learning model
- **Streamlit**: Interactive web application framework
- **Plotly**: Interactive data visualizations
- **Pandas**: Data manipulation and analysis
- **PyArrow**: Efficient parquet file handling
- **NumPy**: Numerical computing
- **Scikit-learn**: Statistical analysis and modeling
- **Jupyter Notebook**: Interactive analysis environment

---

## Key Metrics Tracked

- **Average Claims Amount**: Mean claim value across all records
- **Average Patient Age**: Demographic age distribution
- **Total Claims**: Overall volume of claims processed
- **Average Pre-auth Amount**: Mean pre-authorization values
- **Common Diagnosis Claims**: Volume of common diagnosis cases
- **Rare Diagnosis Claims**: Volume of rare diagnosis cases

---

## Contributing

Contributions are welcome! Please feel free to submit a Pull Request.

---

## License

This project was developed for the Bupa Datathon Challenge 2025.

---

## Authors

**Hassan Alghamdi**

**Yasser Albogami**

Developed for the Bupa Datathon Challenge

---

## Links

- [GitHub Repository](https://github.com/Hassan-Ahlgamdi/Bupa_datathone_)
- [Streamlit Documentation](https://docs.streamlit.io/)
- [Plotly Documentation](https://plotly.com/python/)

---

**Bupa Datathon Challenge | 2025**

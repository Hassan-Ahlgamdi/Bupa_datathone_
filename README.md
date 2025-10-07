# Bupa Arabia Datathon: Predicting Health Insurance Claims

## Project Overview

This repository contains the complete solution for the Bupa Arabia Datathon. The primary objective of this project was to develop a machine learning model to accurately predict monthly health insurance claim amounts for financial reserving purposes. The project involved a comprehensive workflow, including data cleaning, exploratory data analysis, feature engineering, and the evaluation of multiple predictive models. The final XGBoost model demonstrates a measurable improvement over baseline methods and provides key insights into the main drivers of claim costs.

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

## Getting Started

### Prerequisites
This project uses Python 3.9+. You will need to install the necessary libraries.

### Installation
1.  Clone the repository:
    ```bash
    git clone [https://github.com/your-username/your-repo-name.git](https://github.com/your-username/your-repo-name.git)
    ```
2.  Navigate to the project directory:
    ```bash
    cd your-repo-name
    ```
3.  Install the required packages:
    ```bash
    pip install -r requirements.txt
    ```

---

## Usage

To run the main analysis and model training pipeline, you can execute the primary Jupyter Notebook or Python script:
```bash
jupyter notebook Main_Analysis.ipynb

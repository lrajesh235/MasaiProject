# Analytics Module README

# Analytics Module Overview

The Analytics module of the Zepto AI/ML Capstone project focuses on performing exploratory data analysis (EDA) and building predictive models using the Titanic dataset. This module is structured into two main Jupyter notebooks: `01_eda.ipynb` for EDA and `02_modeling.ipynb` for modeling.

## Setup Instructions

To set up the Analytics module, follow these steps:

1. **Install Dependencies**: Ensure you have the required libraries installed. You can install them using pip:

   ```
   pip install -r requirements.txt
   ```

2. **Load the Titanic Dataset**: The Titanic dataset is loaded from Seaborn's built-in loader in the `01_eda.ipynb` notebook. The first time you run this notebook, it will fetch the dataset from the internet. Subsequent runs will use the cached version.

3. **Run the Notebooks**: Open the Jupyter notebooks in your preferred environment and execute the cells in order:
   - Start with `01_eda.ipynb` to perform data profiling, cleaning, and visualization.
   - Continue with `02_modeling.ipynb` to build and evaluate predictive models.

## Design Decisions

- **Data Cleaning**: Missing values were handled based on a percentage threshold. Columns with less than 5% missing values had rows dropped, while those with 5% to 30% missing values were imputed. Columns with over 30% missing values were either dropped or encoded as a separate category based on their context.

- **Exploratory Data Analysis**: Various visualizations were created to understand the distribution of key features such as age and fare, as well as the survival rates based on different categories (e.g., sex, passenger class).

- **Modeling Approach**: Three classifiers (Logistic Regression, Decision Tree, and Random Forest) were trained and evaluated. Hyperparameter tuning was performed on the Random Forest model using GridSearchCV to optimize its performance.

- **Output**: The results of the analysis and modeling are documented within the notebooks, with key insights and recommendations provided at the end of the modeling notebook.

## Conclusion

This module provides a comprehensive analysis of the Titanic dataset, showcasing the process of data exploration, cleaning, and predictive modeling. The insights gained can be valuable for understanding factors that influence survival rates and for developing data-driven strategies in similar contexts.
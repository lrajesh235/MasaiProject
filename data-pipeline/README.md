# Data Pipeline Module README

## Overview

The Data Pipeline module is designed to scrape, clean, and load product data from a public website into a SQLite database. This module serves as the foundation for Zepto's analytics and reporting needs, providing clean and structured data for further analysis.

## Setup Instructions

1. **Clone the Repository**
   Clone the repository to your local machine using:
   ```
   git clone <repository_url>
   cd zepto-ai-ml-capstone
   ```

2. **Install Dependencies**
   Navigate to the `data_pipeline` directory and install the required dependencies. You can use either the provided `requirements.txt` or create a virtual environment.

   To install using `requirements.txt`, run:
   ```
   pip install -r requirements.txt
   ```

3. **Run the Data Pipeline**
   Execute the `scrape_and_load.py` script to scrape data, clean it, and load it into the SQLite database. Run the following command:
   ```
   python scrape_and_load.py
   ```

## Design Decisions

- **Data Source**: The data is scraped from `books.toscrape.com`, a website specifically designed for scraping practice. This allows for a controlled environment to test the data pipeline.
  
- **Data Cleaning**: The scraped data is cleaned to ensure proper data types and handle missing values. The cleaning process includes:
  - Stripping currency symbols from prices.
  - Converting star ratings from text to integers.
  - Parsing availability into boolean values.
  
- **Database Schema**: A normalized SQLite schema is designed with two tables: `categories` and `books`, establishing a primary/foreign key relationship to maintain data integrity.

- **SQL Queries**: A set of predefined SQL queries is included to interact with the database, allowing for data retrieval and analysis.

## Conclusion

This module is essential for providing Zepto's analysts with reliable and structured data for further analytics and decision-making processes. Ensure to follow the setup instructions carefully to successfully run the data pipeline.
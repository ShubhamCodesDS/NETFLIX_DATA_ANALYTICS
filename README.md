# NETFLIX_DATA_ANALYTICS

## Project Overview

This repository contains a comprehensive data analysis project focused on understanding trends, patterns, and insights within a movie dataset (likely sourced from TMDb or a similar database, as indicated by `mymoviedb.csv`). The analysis covers key areas such as genre popularity, voting trends, and release year distributions.

The primary goal of this project is to demonstrate proficiency in data cleaning, feature engineering, and data visualization using Python's core data science libraries.

## Key Features and Analysis

The analysis script performs the following steps:

1.  **Data Cleaning and Preprocessing:** Handles missing values and removes unnecessary columns (`Overview`, `Original_Language`, `Poster_Url`) to streamline the dataset.
2.  **Date and Time Transformation:** Converts the raw release dates into year format to analyze movie output over time.
3.  **Feature Engineering:**
    * The continuous `Vote_Average` is categorized into descriptive bins (`not_popular`, `below_avg`, `average`, `popular`) using quartile-based cutting for easier analysis.
4.  **Data Transformation:** The multi-genre entries are **exploded** into separate rows, allowing for accurate counting and distribution analysis of individual genres.
5.  **Visualization:** Uses `matplotlib` and `seaborn` to generate insights, including:
    * Distribution of movie genres.
    * Distribution of categorized vote averages.
    * Identification and visualization of the Top 5 and Least 5 Popular Movies.
    * A histogram showing the trend of movie releases over the years.

## Technologies and Libraries

* **Language:** Python
* **Data Manipulation:** Pandas, NumPy
* **Data Visualization:** Matplotlib, Seaborn

## How to Run the Code

1.  **Clone the repository:**
    ```bash
    git clone [YOUR-REPO-URL]
    ```
2.  **Ensure you have the data file:**
    * The script expects a CSV file named `mymoviedb.csv` in the same directory.
3.  **Install dependencies:**
    ```bash
    pip install pandas numpy matplotlib seaborn
    ```
4.  **Execute the script:**
    ```bash
    python your_script_name.py
    ```
    *(Note: If you run the code in a Jupyter environment, you can execute the cells sequentially.)*

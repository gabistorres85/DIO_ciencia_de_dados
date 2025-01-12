# Project DIO - Covid Analysis

This project is part of a DIO course about Python models and Machine Learning.

The dataset used was taken from Kaggle on January 8, 2025. You can find it at the following link: [Kaggle Dataset](https://www.kaggle.com/datasets/imdevskp/corona-virus-report?resource=download).

## Step-by-Step:

### Fetching the Data

I followed the instructions on Kaggle's site to download the data directly in Python.

```python
import kagglehub

# Download the latest version
path = kagglehub.dataset_download("imdevskp/corona-virus-report")

print("Path to dataset files:", path)
Cleaning the Dataset
Renamed all column names using a custom function:

python
Copiar código
df.columns = [corrige_colunas(col) for col in df.columns]
Changed the data type of the "date" column.

## Exploratory Analysis
- Investigated information related to Brazil.

- Created a new dataset with Brazil's confirmed cases.

- Plotted: Cumulative Confirmed Cases of Covid-19 in Brazil.

- Added a new column to calculate the daily count of new confirmed cases using a function to subtract the previous day's confirmed cases.

- Plotted: Daily Confirmed Cases of Covid-19 in Brazil.

- Plotted: Covid-19 Deaths in Brazil.

## Growth Rate

> growth_rate = (present / past) ** (n) - 1

The first step to calculate the growth rate was to identify the first date (representing the past) and the last date (representing the present).  
In the function, it is possible not to declare the first and last dates. In this case:
- The first date will be the first day with at least one case.
- The last date will be the last date in the array.

The second step is to define the present and past values using the last and the first dates, respectively.  
The third step is to apply the mathematical expression.

### Daily Growth Rate

The daily growth rate is similar to the overall growth rate. However, it is not necessary to specify the last date, as the mathematical expression will calculate the growth within a range of dates.

This graphic was plotted using `plotly.graph_objects`.


# Predictive Statistics

First, it is necessary to identify the **trend**, **seasonality**, and **noise** in the data. For this, I used the `statsmodels.tsa.seasonal` library.  
Next, I created a new series with the date as the index.  
I applied the `seasonal_decompose` method and created a graph using Matplotlib, displaying three components: **Observed**, **Trend**, and **Seasonal**.

---

# Prophet Library

I initially tried to install Prophet following the course instructions, but it didn't work due to a Python version conflict. So, I asked ChatGPT for help.  
I solved the issue by creating a new Conda environment with Python 3.8:

```bash
conda create -n fbprophet_env python=3.8 -y
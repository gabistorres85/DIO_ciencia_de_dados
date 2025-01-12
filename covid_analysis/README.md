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

Firts is necessary know the trend, rationality and noise, for this used the statsmodels.tsa.seasonal library.
Then, I create a new serie with date like index.
Aplied method seasonal_decompose and creat a graphic with MatPlotlib with three lines (Observed, Trend and Seasonal).


# Prophet Library

I tried install with the instruction from the course, but doesn't work, because a conflit of version Python. So, I asked hetp to chatGPT.  
I solved the problem making a new ambiente Conda with Python 3.8

>conda create -n fbprophet_env python=3.8 -y

Actived the venv, but still hand't worked. 

So i tried another ways, like changing the backend of Prophet, unfortanetly i couldn't solve the problem on this way. 
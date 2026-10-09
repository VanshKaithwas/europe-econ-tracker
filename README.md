# Europe Economic Indicators Tracker

A small Streamlit web app that shows basic economic indicators (GDP growth, inflation, unemployment, tech investment) for several European countries from 2018 to 2025.

> **Important:** the data in `europe_econ_data.csv` is **synthetic**. I generated it myself with `generate_data.py` so the project runs without API keys. The numbers follow rough real-world patterns (a dip in 2020, an inflation spike in 2022), but they are not official statistics.

## Why I built this

I'm applying to study Business Informatics at a university in Poland. I wanted a project that mixes the two things I'm interested in: business and programming. Companies and governments make decisions using data, and I wanted to learn how to turn a table of numbers into something people can understand quickly.

I picked European economic indicators because I'm interested in how Poland compares with bigger economies like Germany and France, and how fast tech investment is growing across the region. This is my first full Python project with a web interface, so I kept it simple on purpose.

## What it does

- Choose a country from the sidebar dropdown
- See key numbers (total GDP growth, average inflation, average unemployment, tech investment)
- See a line chart of inflation vs GDP growth over time
- Compare all countries in one table

## Tech used

- Python
- Streamlit (the web app)
- Pandas (loading and filtering data)
- Plotly Express (charts)

## How to run it

```bash
pip install -r requirements.txt
python generate_data.py      # only needed if the csv is missing
streamlit run app.py
```

Then open the link Streamlit prints in your terminal (usually http://localhost:8501).

## Files

- `app.py` - the Streamlit app
- `generate_data.py` - creates the synthetic dataset
- `europe_econ_data.csv` - the dataset
- `requirements.txt` - Python packages

## What I learned

- How to filter and group data with Pandas
- Why Plotly needs "long" format data to draw several lines (`melt`)
- How Streamlit reruns the script from the top every time you click something

## Ideas for next time

- Replace the synthetic data with real data from Eurostat or the World Bank
- Add more countries and more indicators
- Add a scatter plot of unemployment vs inflation
- Deploy it online with Streamlit Community Cloud

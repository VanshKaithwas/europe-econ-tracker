# generate_data.py
# Makes a made-up (synthetic) dataset so the app works without any API keys.
# The numbers are NOT real statistics - they just follow rough, believable trends.

import random
import pandas as pd

random.seed(42)  # same data every time

countries = ["Poland", "Germany", "France", "Netherlands", "Spain", "Italy", "Sweden", "Czechia"]
years = list(range(2018, 2026))

# rough starting values for each country:
# (typical GDP growth, typical inflation, tech investment in M EUR, unemployment)
base = {
    "Poland":      (4.0, 2.0, 900, 3.8),
    "Germany":     (1.5, 1.6, 4200, 3.4),
    "France":      (1.7, 1.5, 3100, 8.5),
    "Netherlands": (2.2, 1.7, 1900, 3.9),
    "Spain":       (2.3, 1.2, 1500, 15.0),
    "Italy":       (0.9, 1.0, 1300, 10.0),
    "Sweden":      (2.0, 1.8, 1700, 6.5),
    "Czechia":     (3.0, 2.2, 600, 2.4),
}

# year effects: covid dip in 2020, inflation spike in 2022
gdp_shift = {2018: 0, 2019: -0.3, 2020: -6.0, 2021: 4.5, 2022: 1.5, 2023: -0.8, 2024: -0.3, 2025: 0.2}
infl_shift = {2018: 0, 2019: 0.2, 2020: -0.8, 2021: 2.0, 2022: 7.5, 2023: 4.5, 2024: 1.5, 2025: 0.6}
unemp_shift = {2018: 0, 2019: -0.3, 2020: 0.8, 2021: 0.3, 2022: -0.4, 2023: -0.3, 2024: -0.1, 2025: 0.0}

rows = []
for country in countries:
    gdp0, infl0, tech0, unemp0 = base[country]
    tech = tech0
    for year in years:
        gdp = gdp0 + gdp_shift[year] + random.uniform(-0.5, 0.5)
        infl = infl0 + infl_shift[year] + random.uniform(-0.4, 0.4)
        unemp = max(1.5, unemp0 + unemp_shift[year] + random.uniform(-0.2, 0.2))
        # tech investment grows a bit each year, with a small dip in 2020
        tech = tech * (1.07 + random.uniform(-0.02, 0.04))
        if year == 2020:
            tech = tech * 0.95
        rows.append([country, year, round(gdp, 2), round(infl, 2), round(tech, 1), round(unemp, 2)])

df = pd.DataFrame(rows, columns=[
    "Country", "Year", "GDP_Growth_Percent", "Inflation_Rate_Percent",
    "Tech_Sector_Investment_M_EUR", "Unemployment_Rate_Percent",
])

df.to_csv("europe_econ_data.csv", index=False)
print("Saved europe_econ_data.csv with", len(df), "rows")

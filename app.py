import streamlit as st
import pandas as pd
import plotly.express as px

# streamlit UI layout setup
st.title("Europe Economic Indicators Tracker")
st.write("Note: this data is made up (synthetic), not real official stats.")

data = pd.read_csv("europe_econ_data.csv")

# sidebar dropdown, i set Poland as the default one
country_list = sorted(data["Country"].unique())
poland_spot = country_list.index("Poland")
country_choice = st.sidebar.selectbox("Choose a country", country_list, index=poland_spot)

# filtering data by selected country
df1 = data[data["Country"] == country_choice]

# calculating basic average here
avg_inflation = df1["Inflation_Rate_Percent"].mean()
avg_unemployment = df1["Unemployment_Rate_Percent"].mean()
total_tech = df1["Tech_Sector_Investment_M_EUR"].sum()

# total gdp growth over all the years (multiplying each year together)
total_val = 1
for g in df1["GDP_Growth_Percent"]:
    total_val = total_val * (1 + g / 100)
total_val = (total_val - 1) * 100

st.subheader(country_choice + " (2018-2025)")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total GDP growth", str(round(total_val, 1)) + "%")
col2.metric("Avg inflation", str(round(avg_inflation, 1)) + "%")
col3.metric("Avg unemployment", str(round(avg_unemployment, 1)) + "%")
col4.metric("Tech investment (sum)", str(round(total_tech)) + " M EUR")

# plotly needs the data in long format for 2 lines so i used melt
df2 = df1.melt(id_vars=["Year"],
               value_vars=["GDP_Growth_Percent", "Inflation_Rate_Percent"],
               var_name="Indicator", value_name="Percent")

st.subheader("Inflation vs GDP growth")
my_chart = px.line(df2, x="Year", y="Percent", color="Indicator", markers=True)
st.plotly_chart(my_chart, use_container_width=True)

# comparing all the countries (averages)
st.subheader("Compare all countries")
df3 = data.groupby("Country")[["GDP_Growth_Percent", "Inflation_Rate_Percent",
                               "Unemployment_Rate_Percent", "Tech_Sector_Investment_M_EUR"]].mean()
df3 = df3.round(2)
st.dataframe(df3)

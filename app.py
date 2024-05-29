# import libraries
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import plotly.express as px
import plotly.graph_objects as go
from urllib.request import urlopen
import json
from copy import deepcopy

@st.cache_data
def load_data(path):
    df = pd.read_csv(path)
    return df

@st.cache_data
def load_json_data(path):
    with open(path, 'r') as file:
        geojson_df = json.load(file)
    return geojson_df

# load data
population_df_raw = load_data(path="./data/share-of-individuals-using-the-internet.csv")
population_df = deepcopy(population_df_raw)

#rename column 
population_df.rename(columns={"Individuals using the Internet (% of population)": "Population in %"},inplace=True)

geojson_raw = load_json_data(path="./data/countries.geojson")
geojson = deepcopy(geojson_raw)


# Add title and header
st.title("Internet usage across contries")
st.header("By Axel.F")

#st.table(data=mpg_df)
if st.checkbox("Show Dataframe"):

    st.subheader("This is my dataset:")
    st.dataframe(data=population_df)

left_column, middle_column, right_column = st.columns([2, 1, 1])


countries = ["All"]+sorted(pd.unique(population_df['Entity']))
country = left_column.selectbox("Choose a Country", countries)

years = ["All"]+sorted(pd.unique(population_df['Year']))
year = left_column.selectbox("Choose a Year", years)

if country == "All":
    reduced_df = population_df
else:
    reduced_df = population_df[population_df["Entity"] == country]

if year == "All":
    reduced_df = population_df
else:
    reduced_df = population_df[population_df["Year"] == year]
    

fig1 = px.choropleth_mapbox(
    reduced_df, 
    geojson=geojson, 
    locations='Code', 
    color="Population in %",
    featureidkey="properties.ISO_A3",  # Match with GeoJSON key
    color_continuous_scale="electric",
    range_color=(0, reduced_df["Population in %"].max()),
    mapbox_style="carto-darkmatter",
    zoom=1,
    center={"lat": 0, "lon": 0},
    opacity=0.5,
    hover_name="Entity"  # Column which contains the country names
)

fig1.update_layout(
    title="Share of Individuals Using the Internet (% of Population)",
    margin={"r":0,"t":0,"l":0,"b":0}
)

st.plotly_chart(fig1)

#===========================================================================================
#
# Lets do a secon plot where we can compare the countries and there change over the years
#
#
#===========================================================================================

# since there is some countries that we do not hava any data for 2018 or 2019 
# lets tage the 5 year average and then get the top 10 countries

reslut = []

grouped = population_df.groupby('Entity')
for country, data in grouped:
    # Sort data by year in descending order
    sorted_data = data.sort_values('Year', ascending=False)
    # Take the first 5 rows (last 5 years)
    last_5_years = sorted_data.head(5)
    # Calculate mean population for the last 5 years
    mean_population = last_5_years['Population in %'].mean()
    # Append country and mean population to results
    reslut.append([country, mean_population])

# Convert results to DataFrame
result_df = pd.DataFrame(reslut, columns=['Country', 'Mean Population for Last 5 Years'])
result_df.sort_values("Mean Population for Last 5 Years",ascending=False,inplace=True)


fig2 = go.Figure()

for cc in result_df.head(10)["Country"]:
    fig2.add_trace(
        go.Scatter(
            x = population_df[population_df["Entity"]==cc]["Year"], y = population_df[population_df["Entity"]==cc]["Population in %"],
            mode ="lines",
            name = f"{cc}",
            hovertemplate="Year: %{x}<br>Population: %{y}"))


fig2.update_layout(title="Top 10 Countries using internet in %",
                   xaxis_title="Years",
                   yaxis_title="Population in %",
                   template = "plotly_dark",
                   colorway=px.colors.sequential.YlOrRd_r)

st.plotly_chart(fig2)
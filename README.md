# Internet Usage Across Countries Dashboard

## Overview

This project is a Streamlit-based dashboard that visualizes the internet usage across different countries. The dashboard displays a choropleth map showing the internet usage percentage of each country, and a line graph comparing the top 10 countries with the highest average internet usage over the last 5 years.

## Features

- **Choropleth Map**: Visualizes the internet usage of each country using a color-coded map.
- **Line Graph**: Shows the average internet usage of the top 10 countries over the last 5 years.
- **Interactive Selectors**: Allows users to choose a specific country and year to view more detailed data.


## Dependencies

- Streamlit
- Pandas
- Matplotlib
- Plotly
- Python's `json` module

## Usage

To run this project, follow these steps:

1. Ensure all the dependencies are installed. You can install them using `pip`:

```bash

pip install streamlit pandas matplotlib plotly

Download the required data files (countries.geojson and share-of-individuals-using-the-internet.csv) and place them in the data/ directory.
Run the Streamlit app by executing the Python script:

streamlit run app.py

Replace app.py with the actual name of your Python script.

## Data

The dashboard uses two datasets:

- `share-of-individuals-using-the-internet.csv`: Contains internet usage data for each country and year, sourced from [World Bank Data](https://data.worldbank.org/indicator/IT.NET.USER.ZS).
- `countries.geojson`: Provides the geographic shapes for the choropleth map.

Ensure that your code adheres to the project's style guidelines.
Include tests for any new features or changes.
Document any new features or changes in the README.md.
License
This project is licensed under the MIT License. ```

Remember to replace https://example.com/path/to/dashboard-preview.png with the actual URL of your dashboard's preview image. The image should be a snapshot that showcases the dashboard's interface, such as a screenshot of the choropleth map and line graph side by side.

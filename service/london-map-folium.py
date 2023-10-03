import datetime
import random

import folium
import matplotlib.pyplot as plt
import matplotlib.colors as mcolors
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static


def get_data(date: datetime.date) -> pd.DataFrame:
    return pd.DataFrame({
        "borough": get_borough_list(),
        "crime_prediction": [random.uniform(0, 1) for _ in range(len(get_borough_list()))]
    })


def get_borough_list() -> list:
    return [
        "City of London",
        "Westminster",
        "Kensington and Chelsea",
        "Hammersmith and Fulham",
        "Wandsworth",
        "Lambeth",
        "Southwark",
        "Tower Hamlets",
        "Hackney",
        "Islington",
        "Camden",
        "Brent",
        "Ealing",
        "Hounslow",
        "Richmond",
        "Kingston",
        "Merton",
        "Sutton",
        "Croydon",
        "Bromley",
        "Lewisham",
        "Greenwich",
        "Bexley",
        "Havering",
        "Barking and Dagenham",
        "Redbridge",
        "Newham",
        "Waltham Forest",
        "Haringey",
        "Enfield",
        "Barnet",
        "Harrow",
        "Hillingdon",
        "Kingston upon Thames",
        "Richmond upon Thames"
    ]


def insert_map_1() -> None:
    # Create a map centered around London
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

    geo_data = r'data/london-map/london_boroughs.json'

    folium.Choropleth(
        geo_data=geo_data,
        data=get_data(),
        columns=['borough', 'crime_prediction'],
        key_on='feature.properties.name',
        fill_color='RdYlGn_r',
        fill_opacity=0.7,
        line_opacity=0.2,
        legend_name='London Boroughs'
    ).add_to(m)

    # Render the map
    folium_static(m, width=1000, height=800)


def insert_map(date: datetime.date) -> None:
    # Create a map centered around London
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)

    geo_data = r'data/london-map/london_boroughs.json'

    # Load your data into a DataFrame
    data = get_data(date)
    data_dict = data.set_index('borough')['crime_prediction'].to_dict()

    # Create a function to color each borough based on crime prediction
    def color(feature):
        key = feature['properties']['name']
        value = data_dict[key]
        cmap = plt.get_cmap('RdYlGn_r')
        norm = mcolors.Normalize(vmin=0, vmax=1)  # assuming your values range from 0 to 1
        return mcolors.to_hex(cmap(norm(value)))

    # Create a function to add a popup to each borough
    def add_popup(feature):
        borough = feature['properties']['name']
        crime_prediction = data_dict[borough]
        html = f'''
            <h4>{borough}</h4><hr>
            <h5>Crime prediction: {crime_prediction}</h5>
        '''
        return folium.Popup(html, max_width=200)

    # Add the GeoJson layer
    folium.GeoJson(
        geo_data,
        style_function=lambda feature: {
            'fillColor': color(feature),
            'color': 'black',
            'weight': 2,
            'dashArray': '5, 5',
            'fillOpacity': 0.7,
        },
        highlight_function=lambda x: {'weight': 1, 'color': 'black'},
        popup=add_popup
    ).add_to(m)

    # Render the map
    folium_static(m, width=1000, height=800)


def make_layout() -> None:
    st.set_page_config(
        page_title="London safety analysis",
        layout="wide"  # This sets the layout to wide mode
    )
    # Add a title to the application
    st.title("London safety analysis")
    # Choose date
    col1, col2 = st.columns([10, 90])
    chosen_date = col1.date_input(
        label="Choose date",
        value=datetime.date.today(),
        min_value=datetime.date.today(),
        max_value=datetime.date.today() + datetime.timedelta(days=7)
    )
    col2.write("")

    insert_map(chosen_date)

    st.write(
        "This is a Streamlit application that displays a Folium map of London. The different boroughs of London are colored differently.")


if __name__ == "__main__":
    make_layout()

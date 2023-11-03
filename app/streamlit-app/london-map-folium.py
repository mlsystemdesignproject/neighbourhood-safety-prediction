import datetime
import json
from typing import Dict

import folium
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import pandas as pd
import streamlit as st
from streamlit_folium import folium_static

PREDICTIONS_FILE = "data/predictions/roman_3_predictions.csv"
GEO_FILE = "data/london-map/london_boroughs.json"


@st.cache_data
def get_data() -> pd.DataFrame:
    df = pd.read_csv(PREDICTIONS_FILE)
    df["month"] = pd.to_datetime(df.month)
    df["month"] = df["month"].to_numpy().astype("datetime64[M]")
    df["month"] = pd.to_datetime(df.month)
    return df


@st.cache_data
def get_map_base() -> Dict:
    return json.load(open(GEO_FILE, "r"))


@st.cache_data
def get_map_data(df: pd.DataFrame, date: datetime.date, variable: str) -> Dict:
    base = get_map_base()
    df = df.loc[
        ((df.month.dt.date == date.replace(day=1)) & (df.variable == variable)),
    ]
    data_dict = df.set_index("borough")["value"].to_dict()

    if data_dict and variable != "Rating":
        norm = mcolors.Normalize(vmin=0, vmax=1 * max(data_dict.values()))
    else:
        norm = mcolors.Normalize(vmin=0, vmax=1)

    for feature in base["features"]:
        borough_name = feature["properties"]["name"]
        value = data_dict.get(borough_name, 0)
        cmap = plt.get_cmap("RdYlGn_r")

        feature["properties"]["value"] = value
        if variable == "Rating":
            feature["properties"]["value_round"] = round(value * 100)
        else:
            feature["properties"]["value_round"] = round(value)
        feature["properties"]["style"] = {
            "color": "black",
            "weight": 1,
            "fillColor": mcolors.to_hex(cmap(norm(value))),
            "fillOpacity": 0.7,
        }

    return base


@st.cache_data
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
        "Richmond upon Thames",
    ]


def insert_map(df: pd.DataFrame, date: datetime.date, variable: str) -> None:
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)
    map_data = get_map_data(df, date, variable)

    popup = folium.GeoJsonPopup(
        fields=["name", "value_round"],
        aliases=["Borough", variable],
        localize=True,
        labels=True,
    )

    folium.GeoJson(
        map_data,
        style_function=lambda x: x["properties"]["style"],
        highlight_function=lambda x: {"weight": 3, "color": "black"},
        popup=popup,
    ).add_to(m)

    folium_static(m, width=1000, height=800)


def make_layout() -> None:
    st.set_page_config(
        page_title="London safety analysis",
        layout="wide",  # This sets the layout to wide mode
    )
    st.title("London safety analysis")

    df = get_data()

    col1, col2, col3 = st.columns([10, 30, 60])
    chosen_date = col1.date_input(
        label="Choose date",
        value=datetime.date.today(),
        min_value=datetime.date.today(),
        max_value=datetime.date.today() + datetime.timedelta(days=365),
    )

    variables = list(df.variable.unique())
    variables.remove("Rating")
    variables.insert(0, "Rating")

    chosen_variable = col2.selectbox(
        label="Choose Variable",
        options=variables,
    )

    col3.write("")

    insert_map(df, chosen_date, chosen_variable)

    st.write(
        "This is a Streamlit application that displays a Folium map of London. \
        The different boroughs of London are colored differently."
    )


if __name__ == "__main__":
    make_layout()

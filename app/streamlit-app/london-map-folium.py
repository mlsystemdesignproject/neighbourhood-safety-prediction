import datetime
import json
import os
from typing import Dict, List

import folium
import matplotlib.colors as mcolors
import matplotlib.pyplot as plt
import pandas as pd
import requests
import streamlit as st
from streamlit_folium import folium_static
from streamlit_tree_select import tree_select

PREDICTIONS_FILE = os.environ.get(
    "PREDICTIONS_FILE", "data/predictions/predictions.csv"
)
GEO_FILE = os.environ.get("GEO_FILE", "data/london-map/london_boroughs.json")


@st.cache_data
def get_data() -> pd.DataFrame:
    df = pd.read_csv(PREDICTIONS_FILE)
    df["month"] = pd.to_datetime(df.month)
    df["month"] = df["month"].to_numpy().astype("datetime64[M]")
    df["month"] = pd.to_datetime(df.month)
    return df


@st.cache_data
def get_crime_type_tree(df: pd.DataFrame) -> List[Dict]:
    crime_types = df.crime_type.unique()
    return [
        {
            "label": crime_type,
            "value": f"group {crime_type}",
            "children": [
                {
                    "label": crime_subtype,
                    "value": crime_subtype,
                }
                for crime_subtype in df.loc[
                    df.crime_type == crime_type
                ].crime_subtype.unique()
            ],
        }
        for crime_type in crime_types
    ]


@st.cache_data
def get_map_base() -> Dict:
    if GEO_FILE.startswith("http"):
        response = requests.get(GEO_FILE)
        return response.json()
    else:
        return json.load(open(GEO_FILE, "r"))


@st.cache_data
def get_map_data(
    df: pd.DataFrame,
    date: datetime.date,
    crime_types: List[str],
    crime_subtypes: List[str],
) -> Dict:
    base = get_map_base()

    if not crime_subtypes:
        crime_types = df.crime_type.unique()
        crime_subtypes = df.crime_subtype.unique()

    df_selected_month = df.loc[
        (
            (df.month.dt.date == date.replace(day=1))
            & (df.crime_subtype.isin(crime_subtypes))
        ),
    ]
    df_previous_period = df.loc[
        ((df.month.dt.date < date) & (df.crime_subtype.isin(crime_subtypes))),
    ]

    df_sum = df_selected_month.groupby("borough").value.sum().reset_index()
    data_dict = df_sum.set_index("borough")["value"].to_dict()

    norm = mcolors.Normalize(vmin=0, vmax=1 * max(data_dict.values()))

    for feature in base["features"]:
        borough_name = feature["properties"]["name"]
        value = data_dict.get(borough_name, 0)
        cmap = plt.get_cmap("RdYlGn_r")

        feature["properties"]["value"] = value
        for crime_type in crime_types:
            selected_month_value = (
                df_selected_month.loc[
                    (df.borough == borough_name) & (df.crime_type == crime_type),
                    "value",
                ]
                .sum()
                .round(0)
            )
            previous_period_value = (
                df_previous_period.loc[
                    (df.borough == borough_name) & (df.crime_type == crime_type),
                    "value",
                ].sum()
                / len(df_previous_period.month.unique())
            ).round(0)

            if selected_month_value / previous_period_value > 1.2:
                suffix = "📈"
            elif selected_month_value / previous_period_value < 0.8:
                suffix = "📉"
            else:
                suffix = ""
            feature["properties"][
                crime_type
            ] = f"{selected_month_value} {suffix} ({previous_period_value})"

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


def insert_map(
    df: pd.DataFrame, date: datetime.date, crime_subtypes: List[str]
) -> None:
    m = folium.Map(location=[51.5074, -0.1278], zoom_start=10)
    crime_types = list(df[df.crime_subtype.isin(crime_subtypes)].crime_type.unique())
    map_data = get_map_data(df, date, crime_types, crime_subtypes)

    popup = folium.GeoJsonPopup(
        fields=["name"] + crime_types,
        aliases=["Borough"] + crime_types,
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
        page_icon="🚨",
    )
    st.title("London safety analysis")

    df = get_data()

    current_year = datetime.date.today().year
    current_month = datetime.date.today().month

    years = [current_year - 1, current_year, current_year + 1]
    months = [
        "January",
        "February",
        "March",
        "April",
        "May",
        "June",
        "July",
        "August",
        "September",
        "October",
        "November",
        "December",
    ]

    col1, col2 = st.columns(2)
    selected_year = col1.selectbox("Select Year", years, years.index(current_year))
    selected_month = col2.selectbox("Select Month", months, current_month - 1)

    chosen_tree = tree_select(
        get_crime_type_tree(df),
        check_model="leaf",
        checked=list(df.crime_subtype.unique()),
    )

    chosen_date = datetime.date(selected_year, months.index(selected_month) + 1, 1)

    if (df.month.dt.date == chosen_date).sum() == 0:
        st.write("No data for this month")
        return

    insert_map(df, chosen_date, chosen_tree.get("checked", []))

    st.write(
        "This is a Streamlit application that displays a Folium map of London. \
        The different boroughs of London are colored differently."
    )


if __name__ == "__main__":
    make_layout()

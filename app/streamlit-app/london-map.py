# from .boroughs import list_of_london_boroughs as borough_list
import random

# import pandas as pd
import geopandas as gdp
import matplotlib.pyplot as plt
import streamlit as st


@st.cache_data
def load_data():
    df = gdp.read_file("data/london-map/London_Borough_Excluding_MHW.shp")
    df["crime_prediction"] = [random.uniform(0, 1) for _ in range(df.shape[0])]
    return df


map_df = load_data()
borough_list = [
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
]

st.sidebar.title("Model Input")
st.title("Model output")

start_date = st.sidebar.date_input("Start date")
end_date = st.sidebar.date_input("End date")

st.write(f"Start date = {start_date}")
st.write(f"End date = {end_date}")

# Вопрос: можно ли раскрасить район на карте в streamlit?

sbox = st.sidebar.multiselect("Pick London Boroughs", borough_list)
st.title("Model results are:")

# Create a color map from green to red
cmap = plt.get_cmap("RdYlGn_r")

if len(sbox) > 0:
    # data = [borough_list.index(item) for item in sbox]
    fig, ax = plt.subplots(1, 1)
    map_df.plot(
        ax=ax,
        color=cmap(map_df.crime_prediction),
        edgecolor="grey",
        alpha=0.5,
    )
    # make it a bit darker for the text to pop
    map_df[map_df["NAME"].isin(sbox)].plot(
        ax=ax,
        color="grey",
        edgecolor="black",
        alpha=0.3,
    )
    ax.set_axis_off()
    st.pyplot(fig)
    st.write(
        """Contains National Statistics data © Crown copyright and database right [2015]"""
    )
    st.write(
        """Contains Ordnance Survey data © Crown copyright and database right [2015]"""
    )
    for bor in sbox:
        st.write(f"For {bor} borough result is {borough_list.index(bor)+1}")
else:
    st.write("Please, enter boroughs")

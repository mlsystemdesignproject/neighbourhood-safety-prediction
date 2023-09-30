# from .boroughs import list_of_london_boroughs as borough_list
import os
import streamlit as st
import joblib
import pandas as pd
import datetime
import numpy as np


@st.cache_data
def load_data():
    filepath = os.path.join("models", "dummy_prophet_model_01.joblib")
    df = joblib.load(filepath)
    return df


prediction_df = load_data()
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

search_date = st.sidebar.date_input("Search date", datetime.date(2022, 9, 30))

min_data = prediction_df["ds"].min()
max_date = prediction_df["ds"].max()


# st.write(f"Start date = {min_data}, date type = {type(min_data)}")
# st.write(f"End date = {max_date}, date type = {type(max_date)}")
# st.write(f"Search date = {search_date}, date type = {type(search_date)}")
#
# st.write(f"TS search date = {ts_search_date}, date type = {type(ts_search_date)}")

ts_search_date = pd.Timestamp(search_date)
st.write(f"Start date = {min_data}")
st.write(f"End date = {max_date}")
st.write(f"Search date = {search_date}")


sbox = st.sidebar.multiselect("Pick London Boroughs", borough_list)
st.title("Model results are:")
if min_data <= ts_search_date <= max_date:
    for borough in sbox:
        val = np.around(
            prediction_df.loc[prediction_df["ds"] == ts_search_date][
                [borough, f"{borough}_lower", f"{borough}_upper"]
            ].values[0],
            1,
        )
        st.text(
            f"For {borough}, prediction = {val[0]}, lower_bound = {val[1]}, upper_bound = {val[2]}"
        )
else:
    st.text("Search date out of prediction range")

# st.text(f"{prediction_df.loc[0, :]}")

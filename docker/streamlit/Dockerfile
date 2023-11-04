FROM python:3.8-slim-buster
WORKDIR /app
COPY ["./docker/streamlit/streamlit-requirements.txt", "requirements.txt"]
COPY ["./data/london-map/london_boroughs.json", "london_boroughs.json"]
COPY ["./app/streamlit-app/", "app"]
RUN pip3 install -r requirements.txt

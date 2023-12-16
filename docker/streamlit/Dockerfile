FROM python:3.8-slim-buster
WORKDIR /app
EXPOSE 8501
HEALTHCHECK CMD curl --fail http://localhost:8501/_stcore/health
COPY ["./docker/streamlit/streamlit-requirements.txt", "requirements.txt"]
RUN pip3 install -r requirements.txt
COPY ["./data/london-map/london_boroughs.json", "london_boroughs.json"]
COPY ["./app/streamlit-app/", "app"]

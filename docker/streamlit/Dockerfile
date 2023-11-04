FROM python:3.8-slim-buster
WORKDIR /app
COPY ["streamlit-requirements.txt", "requirements.txt"]
COPY ["london_boroughs.json", "london_boroughs.json"]
RUN pip3 install -r requirements.txt

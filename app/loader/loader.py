import requests
from bs4 import BeautifulSoup
from dotenv import load_dotenv

MPS_MAIN_PAGE = "https://data.london.gov.uk/dataset/mps-monthly-crime-dahboard-data"
load_dotenv()


def parse_main_page():
    text = requests.get(MPS_MAIN_PAGE).text
    soup = BeautifulSoup(text, "html.parser")

    a_tags = soup.find_all("a", class_="dp-resource__link")

    return {"resources": a_tags}


def main():
    parsed = parse_main_page()
    for a in parsed["resources"]:
        print(a.get("href"))


main()

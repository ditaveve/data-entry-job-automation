from bs4 import BeautifulSoup
import os
import requests
from dotenv import load_dotenv
class ScrapeListings:

    def __init__(self):
        load_dotenv()
        response = requests.get(os.getenv("URL"))
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.links = []

    def get_listings(self):
        self.links = self.soup.select("a[class='StyledPropertyCardDataArea-anchor']")
        for link in self.links:
            print(link.getText())
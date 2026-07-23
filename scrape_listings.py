from bs4 import BeautifulSoup
import os
import requests
from dotenv import load_dotenv
import re

class ScrapeListings:

    def __init__(self):
        load_dotenv()
        response = requests.get(os.getenv("URL"))
        self.soup = BeautifulSoup(response.text, "html.parser")
        self.links = []
        self.prices = []
        self.addresses = []

    def scrape(self):
        properties = self.soup.select("li[class='ListItem-c11n-8-84-3-StyledListCardWrapper']")
        for property in properties:
            link = property.select_one("a[class='StyledPropertyCardDataArea-anchor']")
            self.links.append(link.get("href"))

            price = property.select_one("span[data-test='property-card-price']")
            edited_price = re.split(r"[/+ ]", price.getText())[0]
            self.prices.append(edited_price)

            address = property.select_one("address[data-test='property-card-addr']")
            edited_address = address.getText().strip().replace("|", "")
            self.addresses.append(edited_address)
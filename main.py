from scrape_listings import ScrapeListings
from fill_form import FillForm

scrape_listings = ScrapeListings()
scrape_listings.scrape()

fill_form = FillForm()
fill_form.fill(scrape_listings)


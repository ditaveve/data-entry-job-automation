# Data Entry Job Automation

Day 53 of my 100 Days of Python challenge. This bot scrapes property listings off a Zillow clone page, cleans up the price/address text, then automatically fills out and submits a Google Form for each listing — one entry per property, with no manual typing.

Basically simulating the kind of repetitive data-entry job where someone copies listings from one site into a form or spreadsheet, all day, every day. This automates that away.

## What it does

1. `scrape_listings.py` fetches the listings page and pulls out each property's link, price, and address
2. Cleans the scraped text — strips trailing `/mo`, `+`, and extra spaces off prices, and removes stray `|` characters from addresses
3. `fill_form.py` opens a Google Form in Chrome and, for every listing, fills in the address/price/link fields and submits, then moves on to the next entry

## Proof it works

Every submission lands in the connected response sheet — [here's the live result](https://docs.google.com/spreadsheets/d/1sMJgS5HJ59frIslBgug1rywsE506h7GHucRmi3lHzgw/edit?usp=sharing) after running the bot against a batch of listings.

## Setup

You'll need Python 3 and:

```bash
pip install selenium beautifulsoup4 requests python-dotenv
```

Chrome needs to be installed — Selenium handles the driver itself.

Create a `.env` file in this folder with:

```
URL=
FORM_LINK=
```

- `URL` — the listings page to scrape
- `FORM_LINK` — the Google Form to submit each listing to

## Running it

```bash
python3 main.py
```

A Chrome window opens and submits one form entry per scraped listing. It stays open after the script finishes so you can see the last submission.
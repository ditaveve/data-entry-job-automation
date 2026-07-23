from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
import os
from dotenv import load_dotenv

class FillForm:

    def __init__(self):
        load_dotenv()
        chrome_options = webdriver.ChromeOptions()
        chrome_options.add_experimental_option("detach", True)
        self.driver = webdriver.Chrome(options=chrome_options)

    def open_form(self):
        self.driver.get(os.getenv("FORM_LINK"))

    def complete_form(self, address, price, link):
        queries = WebDriverWait(self.driver, 10).until(EC.presence_of_all_elements_located((By.CSS_SELECTOR, "input[type='text'][data-initial-value]")))
        
        queries[0].click()
        queries[0].send_keys(address)
        queries[1].click()
        queries[1].send_keys(price)
        queries[2].click()
        queries[2].send_keys(link)

        submit_button = self.driver.find_element(By.CSS_SELECTOR, "div[role='button'][tabindex='0']")
        submit_button.click()

        new_form = WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable((By.XPATH, "/html/body/div[1]/div[2]/div[1]/div/div[4]/a")))
        new_form.click()


    def fill(self, listings):
        self.open_form()
        counter = len(listings.addresses)
        for i in range(1, counter):
            self.complete_form(listings.addresses[i], listings.prices[i], listings.links[i])

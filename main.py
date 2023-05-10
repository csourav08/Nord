import time
from selenium.webdriver.support import expected_conditions as EC
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import Select
from selenium.webdriver.support.wait import WebDriverWait


from mock import credentials


class Browser:
    browser, service = None, None

    def __init__(self, driver: str):
        self.service = Service(driver)
        self.browser = webdriver.Chrome(service=self.service)

    def open_page(self, url: str):
        self.browser.get(url)

    def close_browser(self):
        self.browser.close()

    def add_input(self, by: By, value: str, text: str):
        field = self.browser.find_element(by=by, value=value)
        field.send_keys(text)
        time.sleep(2)

    def click_button(self, by: By, value: str):
        button = self.browser.find_element(by=by, value=value)
        button.click()
        time.sleep(2)

    def select_dropdown(self, by: By, value: str, option: str):
        select = Select(self.browser.find_element(by=by, value=value))
        select.select_by_visible_text(option)
        time.sleep(2)

    def login(self, firstName: str, lastName: str, company: str, email: str, phone: str, jobTitle: str, country: str):
        self.add_input(by=By.ID, value='firstname-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261', text=firstName)
        self.add_input(by=By.ID, value='lastname-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261', text=lastName)
        self.add_input(by=By.ID, value='company-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261', text=company)
        self.add_input(by=By.ID, value='email-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261', text=email)
        self.add_input(by=By.ID, value='phone-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261', text=phone)
        self.add_input(by=By.ID, value='jobtitle-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261', text=jobTitle)
        select = Select(
            self.browser.find_element(by=By.ID, value='country__dropdown_-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261'))
        select.select_by_visible_text(country)

        checkbox = self.browser.find_element(by=By.ID,
                                             value='LEGAL_CONSENT.subscription_type_6801572-026d3da1-3ad3-4492-9470-1d4274bcae4c_6261')
        checkbox.click()
        time.sleep(3)
        self.click_button(by=By.CLASS_NAME, value='hs-button.primary.large')


if __name__ == '__main__':
    firstName, lastName, company, email, phone, jobTitle, country = credentials['firstName'], credentials['lastName'], \
                                                                    credentials['company'], credentials['email'], \
                                                                    credentials['phone'], credentials[
                                                                        'jobTitle'], "Estonia"

    browser = Browser('drivers/chromedriver')
    browser.open_page('https://www.provet.cloud/provet-cloud-request-a-demo')
    book_demo_button = WebDriverWait(browser.browser, 10).until(
        EC.element_to_be_clickable(
            (By.XPATH, '//*[@id="cta_button_5923252_5fc25f4f-8d28-4224-8de3-66ec41604683"]/div/strong/span/span')))
    book_demo_button.click()

    browser.login(firstName, lastName, company, email, phone, jobTitle, country)
    time.sleep(5)
    browser.close_browser()


from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
from Utilities.ExcelUtils import ExcelUtils


class Home_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)

    cookies_accept_xpath = "//*[@id='CybotCookiebotDialogBodyLevelButtonLevelOptinAllowAll']"
    search_option_xpath = "//button[@aria-label='Search button']"
    search_field_xpath = "//input[@type='search']"
    results_xpath = "//div[@class='header--search__results']"

    def accept_cookies_element(self):
        self.click_element('cookies_accept_xpath',self.cookies_accept_xpath)
    def click_on_search_button(self):
        self.click_element('search_option_xpath',self.search_option_xpath)
    def enter_text_in_the_search_box(self, file_path, sheet_name, row, column):
        search_text = ExcelUtils(file_path).get_cell_data(sheet_name, row, column)
        self.type_in_the_element('search_field_xpath',self.search_field_xpath, search_text)
    def displayed_results(self):
        return self.get_elements('results_xpath',self.results_xpath)
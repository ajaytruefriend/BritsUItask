import time
from _ast import Assert

import pytest

from selenium.webdriver.common.by import By

from PageObjects.HomePage import Home_Page


@pytest.mark.usefixtures("setup_and_teardown")
class TestSearch:
    def test_validate_search_page(self):
        home_page = Home_Page(self.driver)
        home_page.accept_cookies_element()
        time.sleep(3)
        home_page.click_on_search_button()
        time.sleep(1)
        home_page.enter_text_in_the_search_box("C:/Python selenium/BritsUIandAPI/testdata.xlsx", "data1", 2,1)
        time.sleep(3)
        text_results = home_page.displayed_results()
        self.assert_search_results(*self.defining_and_extracting_ExpectedList_and_ActualList(text_results))

    def defining_and_extracting_ExpectedList_and_ActualList(self, text_results):
        expected_List = ['Interim results for the six months ended 30 June 2022',
                         'Results for the year ended 31 December 2023',
                         'Interim Report 2023',
                         'Kirstin Simon',
                         'Gavin Wilkinsons']
        # extracting the  actual results
        actual_List = []
        for text_result in text_results:
            text = text_result.get_attribute('innerText').strip()
            actual_List.extend(text.split('\n'))
        return expected_List, actual_List

    def assert_search_results(self, actual_List, expected_List):
        assert actual_List == expected_List, f"TC Failed: Actual List is {actual_List} But Expected List is {expected_List}"
        print("TC Passed: Search results are correctly displayed")
        # Compare lengths of the lists
        actuallength = len(actual_List)
        expectedlength = len(expected_List)
        assert actuallength == expectedlength, f"TC Failed: Actual List length is {actuallength} But Expected List length is {expectedlength}"
        print(f"{expectedlength} search results are correctly displayed")
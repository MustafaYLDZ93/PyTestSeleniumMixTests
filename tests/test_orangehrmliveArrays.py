import unittest
from selenium import webdriver
from selenium.webdriver.common.by import By
from time import sleep


class OrangeHRMTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://opensource-demo.orangehrmlive.com/')
        sleep(1)

    def login(self):
        self.driver.find_element(By.CSS_SELECTOR, ':nth-child(2) > .oxd-input-group > :nth-child(2) > .oxd-input').send_keys('Admin')
        self.driver.find_element(By.CSS_SELECTOR, ':nth-child(3) > .oxd-input-group > :nth-child(2) > .oxd-input').send_keys('admin123')
        self.driver.find_element(By.CSS_SELECTOR, '.oxd-button').click()
        sleep(1)

    def test_date_selection(self):
        self.login()

        tarih_dizisi = ['August', '2019']
        month, year = tarih_dizisi

        self.driver.find_element(By.CSS_SELECTOR, '.oxd-sidepanel').is_displayed()
        sleep(1)

        left_menu = self.driver.find_element(By.XPATH, '//*[@id="app"]/div[1]/div[1]/aside/nav/div[2]/ul/li[3]/a')
        sleep(1)
        left_menu.click()
        sleep(1)

        text_dogrulama = self.driver.find_element(By.CSS_SELECTOR, '.oxd-table-filter-header-title > .oxd-text')
        self.assertEqual(text_dogrulama.text, 'Leave List')

        calendar = self.driver.find_element(By.CSS_SELECTOR, 'div#app div:nth-child(1) > div > div:nth-child(2) > div > div > i')
        calendar.click()

        self.driver.execute_script('window.scrollTo(0, 0);')

        self.driver.find_element(By.CSS_SELECTOR, 'div#app div:nth-child(1) > div > div:nth-child(2) > div > div > i').click()

        year_dropdown = self.driver.find_element(By.CSS_SELECTOR, 'div#app li.oxd-calendar-selector-year > div > p')
        year_dropdown.click()
        self.driver.find_element(By.XPATH, f'//*[contains(text(), "{year}")]').click()
        sleep(1)

        month_dropdown = self.driver.find_element(By.CSS_SELECTOR, 'div#app li.oxd-calendar-selector-month > div > p')
        month_dropdown.click()
        sleep(1)
        self.driver.find_element(By.XPATH, f'//*[contains(text(), "{month}")]').click()
        sleep(2)

        self.driver.find_element(By.CSS_SELECTOR, 'div#app div:nth-child(6) > div').click()
        sleep(1)
        date = 'div#app div:nth-child(1) > div > div:nth-child(1) > div > div:nth-child(2) > div > div > input'
        date_verify = self.driver.find_element(By.CSS_SELECTOR, date)

        button_value = date_verify.get_attribute("value")
        sleep(1)
        assert button_value == '2019-06-08'
        sleep(1)

    def tearDown(self):
        self.driver.quit()

if __name__ == '__main__':
    unittest.main()

import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from time import sleep


@pytest.fixture
def driver():
    options = Options()
    options.add_argument("--headless")
    driver = webdriver.Chrome(options=options)
    driver.maximize_window()
    yield driver
    driver.quit()


def test_login(driver):
    # variables
    url_site = 'https://random-asin-new.vercel.app'
    email_testid = '//input[@data-testid="login-email"]'
    email = 'mustafa.yldz093@gmail.com'
    password_testid = '//input[@data-testid="login-password"]'
    password_valid = 'e95f621'
    close_button = '/html/body/div[5]/div[3]/div[1]/button'

    # COMMANDS
    driver.get(url_site)
    wait = WebDriverWait(driver, 1)
    driver.find_element(By.XPATH, "//*[contains(text(), 'Giriş Yap')]").click()
    wait.until(EC.visibility_of_element_located((By.CSS_SELECTOR, ".auth-container")))
    driver.find_element(By.XPATH, email_testid).send_keys(email)
    driver.find_element(By.XPATH, password_testid).send_keys(password_valid)

    driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[3]/div[3]/div').click()
    sleep(1)
    verify_button = "/html/body/div[5]/div[2]/div[2]/div[3]/div[3]/div"
    verify = driver.find_element(By.XPATH, verify_button)
    button_value = verify.get_attribute("data-checked")
    sleep(1)
    assert button_value == 'true'
    sleep(1)
    driver.find_element(By.XPATH, "//input[@data-testid='login-remember-me']").click()
    sleep(1)
    forgot_password_button = driver.find_element(By.XPATH, "//*[contains(text(), 'Şifremi Unuttum')]")
    driver.execute_script("arguments[0].click();", forgot_password_button)
    sleep(1)

    verify2 = driver.find_element(By.XPATH, '/html/body/div[5]/div[2]/div[2]/div[2]/div/label')
    value2 = verify2.get_attribute("innerText")
    sleep(1)
    assert value2 == 'Kullanıcı Adı:'
    sleep(1)

    driver.find_element(By.XPATH, close_button).click()
    sleep(1)

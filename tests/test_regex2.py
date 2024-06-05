import re
from selenium import webdriver
from selenium.webdriver.common.by import By
import time

# Desenler
username_pattern = r'^[a-z0-9_-]{4,}$'  # Kullanıcı adının en az 4 karakter uzunluğunda olması, küçük harfler, rakamlar, alt tire ve tire işaretlerinden oluşması
password_pattern = r'^[a-zA-Z0-9_-]{8,}$'  # Şifrenin en az 8 karakter uzunluğunda olması, harfler, sayılar, alt tire ve tire karakterlerinden oluşması


# Test senaryosu
def test_login():
    # WebDriver'ı başlat
    driver = webdriver.Chrome()
    driver.maximize_window()

    try:
        # Test edilecek web sitesini aç
        driver.get("https://www.saucedemo.com/v1/index.html")

        # Kullanıcı adı ve şifre alanlarını bul
        username_field = driver.find_element(By.ID, "user-name")
        password_field = driver.find_element(By.ID, "passwords")

        # Test dizesi
        test_username = "standard_user"  # kullanıcı adı
        test_password = "secret_sauce"   # şifre deseni

        # Desenle eşleşme kontrolü
        username_match = re.match(username_pattern, test_username)
        password_match = re.match(password_pattern, test_password)

        # Kullanıcı adı ve şifre belirtilen desenlere uymuyorsa testi başarısız yap
        assert username_match, f"Kullanıcı adı belirtilen desene uymuyor: {test_username}"
        assert password_match, f"Şifre belirtilen desene uymuyor: {test_password}"

        # Kullanıcı adı ve şifre alanlarına değerleri gönder
        username_field.send_keys(test_username)
        password_field.send_keys(test_password)

        # Giriş butonuna tıkla
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        time.sleep(2)

        # Test başarılı ise
        assert "inventory.html" in driver.current_url, "Giriş başarısız."

        print("Test başarılı: Kullanıcı adı ve şifre belirtilen desene uyuyor ve giriş başarılı.")

    except AssertionError as e:
        print(f"Test başarısız: {e}")
        raise  # AssertionError'u yeniden fırlat

    except Exception as e:
        print(f"Beklenmeyen bir hata oluştu: {e}")

    finally:
        # WebDriver'ı kapat
        driver.quit()

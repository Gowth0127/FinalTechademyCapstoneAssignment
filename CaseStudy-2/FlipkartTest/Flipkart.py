import time
from selenium.webdriver.common.by import By
from browser import browser


def test_verify_popup(browser):
    browser.get("https://www.flipkart.com/")
    time.sleep(3)
    pop_up = browser.find_element(By.CSS_SELECTOR, "div._3wFoIb.row")
    popup_close_button = browser.find_element(By.CSS_SELECTOR, "button._2KpZ6l._2doB4z")
    time.sleep(5)
    if pop_up.is_displayed():
        print(" Pop-Up found ")
        popup_close_button.click()
    else:
        print("No Pop-Up found")


def test_verify_login(browser):
    loginButton = browser.find_element(By.CSS_SELECTOR, "a._1_3w1N")
    loginButton.click()
    time.sleep(3)
    phone_Number_text_box = browser.find_element(By.CSS_SELECTOR, "input._2IX_2-.VJZDxU")
    phone_Number_text_box.send_keys("8096979401")
    time.sleep(3)
    request_otp_button = browser.find_element(By.XPATH, "//button[text()='Request OTP']")
    request_otp_button.click()
    time.sleep(3)
    message_alert = browser.find_element(By.XPATH, "//div[text()='Please enter the OTP sent to']")
    assert message_alert.is_displayed()


import time
from selenium.webdriver.common.by import By
from browser import browser

# Verifying the Home Browser Title


def test_verify_title(browser):
    browser.get("https://automationpanda.com/2021/12/29/want-to-practice-test-automation-try-these-demo-sites/")
    assert browser.title == "Want to practice test automation? Try these demo sites! | Automation Panda"
    print("Home browser Title is "+browser.title)


# Verifying Speaking page Title


def test_verify_speaking_page(browser):
    browser.get("https://automationpanda.com/2021/12/29/want-to-practice-test-automation-try-these-demo-sites/")
    speaking_Button = browser.find_element(By.CSS_SELECTOR, "div.menu-primary-container>ul>li:nth-of-type(4)")
    speaking_Button.click()
    assert browser.title == "Speaking | Automation Panda"
    print("Speaking browser Title is "+browser.title)

# Verifying KeyNote Address
    browser.execute_script('window.scrollTo(0,600)', '')
    time.sleep(3)
    keynote = browser.find_element(By.CSS_SELECTOR, "div.entry-content>h2:first-of-type")
    assert keynote.is_displayed()
    keynote_text = browser.find_element(By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes").text
    if keynote_text:
        print("The KeyNote Text is : "+keynote_text)
    else:
        print("Keynote address Doesn't contain any text")
        browser.execute_script('window.scrollTo(1000,1500)')
        time.sleep(3)
# Verifying Conference Talks
        conferenceTalks = browser.find_element(By.CSS_SELECTOR, "div.entry-content>h2:nth-of-type(2)")
        assert conferenceTalks.is_displayed()
        conferenceText = browser.find_element(By.CSS_SELECTOR, "figure.wp-block-table.is-style-stripes").text
        if conferenceText:
            print("The Conference Talk Text is : "+conferenceText)
        else:
            print("Conference talks Doesn't contain any text")

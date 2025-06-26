from selenium import webdriver
from selenium.webdriver.chrome.options import Options

def test_first_flsk_app_home_page():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get("https://my-first-flsk-app.azurewebsites.net/")
    print("Title: ", driver.title)
    driver.quit()


def test_first_flask_app_about_page():
    options = Options()
    options.add_argument("--headless")
    options.add_argument("--no-sandbox")
    options.add_argument("--disable-dev-shm-usage")
    driver = webdriver.Chrome(options=options)
    driver.get("https://my-first-flsk-app.azurewebsites.net/about")
    print("Title: ", driver.title)
    driver.quit()
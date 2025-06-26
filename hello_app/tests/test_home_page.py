from selenium import webdriver

def test_first_flsk_app_home_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://my-first-flsk-app.azurewebsites.net/")
    print("Title: ", driver.title)


def test_first_flask_app_about_page():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get("https://my-first-flsk-app.azurewebsites.net/about")
    print("Title: ", driver.title)
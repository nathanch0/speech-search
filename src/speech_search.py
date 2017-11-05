import selenium
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from speechtest import speech

def search():
    keyword = speech()
    driver_path = '/Users/nathancho/selenium_drivers/chromedriver'
    driver = webdriver.Chrome(executable_path=driver_path)
    driver.implicitly_wait(30)
    driver.maximize_window()

    driver.get('https://google.com')
    search_bar = driver.find_element_by_id("lst-ib")
    search_bar.clear()
    search_bar.send_keys(keyword)
    search_bar.submit()



if "__main__" == __name__:
    search()

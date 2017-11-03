from selenium import webdriver
from selenium.webdriver.common.keys import Keys


def main():
    q = input("Enter the search query: ")
    q = q.replace(' ', '')
    browser = webdriver.Firefox()
    body = browser.find_element_by_tag_name("body")
    body.send_keys(Keys.CONTROL + 't')
    counter = 0
    for i in range(0,20):
        browser.get("https://www.google.com/search?q=" + q + "&start=" + str(counter))
        body = browser.find_element_by_tag_name("body")
        if "thetaranights" in body.text:
            browser.find_element_by_xpath('//a[starts-with(@href,"http://www.thetaranights.com")]').click()
            break
        counter += 10


if "__main__" == __name__:
    main()

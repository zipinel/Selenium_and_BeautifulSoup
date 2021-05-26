from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import os


def seleniumAction(source):
    print("Phase 1: Selenium scroll down started (estimated a minimum of 10 seconds)")
    cwd = os.getcwd()
    pathToChromeDriver = os.path.join(cwd, "Drivers\\chromedriver.exe")
    driver = webdriver.Chrome(executable_path=pathToChromeDriver)
    driver.get(source)
    driver.maximize_window()
    driver.find_element_by_name("agree").click()
    driver.get(source)

    #### Page Down key is used to scroll down due to restrictions on executing automatic js entries
    #### on page. Range for the forloop is set to cover all items. Ideally total number of items
    #### to load via lazy loading to be known in advance. I have put 5 here just for functionality purposes
    #### but replace with the number needed to scroll all the way down
    for stretch in range(1, 5):
        driver.find_element_by_tag_name('body').send_keys(Keys.PAGE_DOWN)
        time.sleep(1)
    time.sleep(3)
    stretchedPage = driver.page_source
    driver.close()
    print("Phase 2: Selenium scroll down completed successfully")
    print("Phase 3: Sending extended html content")
    return stretchedPage

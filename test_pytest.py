import test_pytest
from selenium import webdriver

from selenium.webdriver.common.by import By

from selenium.webdriver.support.ui import Select
import time

from selenium.webdriver.chrome.options import Options

option = Options()
option.add_argument('--disable-notifications')


def test_head():
    driver = webdriver.Chrome(executable_path="D:\chromedriver.exe",
                              chrome_options=option)
    driver.get("https://www.air.irctc.co.in/")
    title1 = driver.title
    assert "Air Ticket Booking | Book Flight Tickets | Cheap Air Fare - IRCTC Air" in title1
    driver.close()
def test_search():
    driver = webdriver.Chrome(executable_path="D:\chromedriver.exe",
                              chrome_options=option)
    driver.get("https://www.air.irctc.co.in/")

    driver.maximize_window()
    driver.implicitly_wait(10)
    # ---------------oneway-----------

    driver.find_element(by=By.XPATH,
                        value="/html/body/app-root/app-index/div[2]/div/div[1]/div/div/div[1]/div[1]/div[1]/label").click()

    # -------------origin-------------

    driver.find_element(by=By.XPATH,
                        value="/html/body/app-root/app-index/div[2]/div/div[1]/div/div/div[2]/form/div[1]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/ul[1]/li[2]/div").click()

    # ------------destination----------------------------

    driver.find_element(by=By.XPATH,
                        value="/html/body/app-root/app-index/div[2]/div/div[1]/div/div/div[2]/form/div[2]/input").click()
    driver.find_element(by=By.XPATH, value="/html/body/ul[2]/li[7]/div").click()

    # ---------------departure----------------------------
    driver.find_element(by=By.XPATH,
                        value="/html/body/app-root/app-index/div[2]/div/div[1]/div/div/div[2]/form/div[3]/datepickermodifi/div/div[1]/input").click()
    driver.find_element(by=By.XPATH,
                        value="/html/body/app-root/app-index/div[2]/div/div[1]/div/div/div[2]/form/div[3]/datepickermodifi/div/div[2]/div[2]/table/tbody/tr[5]/td[4]/span").click()

    # -------------------class------------------------------
    driver.find_element(by=By.XPATH,
                        value="/html/body/app-root/app-index/div[2]/div/div[1]/div/div/div[2]/form/div[5]/input").click()
    select = Select(driver.find_element(by=By.XPATH,
                                        value="/html/body/app-root/app-index/div[2]/div/div[1]/div/div/div[2]/form/div[5]/div/div[2]/div[1]/select"))
    select.select_by_index(2)

    # --------------------------search------------------------------------------
    driver.find_element(by=By.XPATH,
                        value="/html/body/app-root/app-index/div[2]/div/div[1]/div/div/div[2]/form/div[6]/button").click()
    time.sleep(30)
    driver.find_element(by=By.XPATH,
                        value="/html/body/app-root/app-oneway/div[1]/main/div/div/div[1]/app-filter-search/div/div/div[2]/div[2]/div[2]/div[4]/img").click()
    driver.get_screenshot_as_file('flight2.png')
    flight_names = driver.find_elements(By.XPATH, '//div[@class="right-searchbarbtm"]')
    print("the no. of flights available are:", len(flight_names))
    for flight in flight_names:
        print(flight.text)
        print("-------------------------------------------------------------------")
    driver.close()
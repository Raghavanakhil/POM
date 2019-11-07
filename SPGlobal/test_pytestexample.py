from selenium import webdriver
import pytest

@pytest.fixture()
def Setup():
    global driver
    driver = webdriver.Chrome("D://python-3.6.5//chrome.exe//chromedriver.exe")
    driver.implicitly_wait(5)
    driver.maximize_window()


    print("test completed")

def test_scenario1(Setup):
    driver.get("https://www.facebook.com/")
    driver.find_element_by_xpath("//input[@name='email']").send_keys("sraghavan43@gmail.com")
    driver.find_element_by_xpath("//input[@name='pass']").send_keys("Akhil@007")
    driver.find_element_by_xpath("//input[@id='loginbutton']").click()

"""
driver.close()
driver.quit()
print("test completed")
"""


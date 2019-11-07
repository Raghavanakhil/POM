from selenium import webdriver
import pytest
import pyodbc

driver = webdriver.Chrome("D://python-3.6.5//chrome.exe//chromedriver.exe")
driver.get("https://www.lmax.com/global/demo-login")
driver.implicitly_wait(5)
driver.maximize_window()
driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
driver.find_element_by_xpath("//input[@name='username']").send_keys("admin")
driver.find_element_by_xpath("//button[@type='submit']").click()




'''conn = pyodbc.connect("Driver={SQL Server Native Client 11.0};"
                      "Server=INHYDLSSRIVATHS;"
                      "Database=spglobal;"
                      "Trusted_Connection=yes;")
'''



   #


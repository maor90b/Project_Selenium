from selenium import webdriver
from time import sleep
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.common.exceptions import NoSuchElementException

'''Ex 3'''


driver = webdriver.Chrome \
    (executable_path=r"C:\Users\Student\Desktop\Selenium\chromedriver.exe")

driver.implicitly_wait(5)

driver.get("https://www.phptravels.net/admin")

driver.find_element_by_xpath("//input[@name='email'][1]").send_keys("admin@phptravels.com")

#driver.find_element_by_xpath("//input[@name='password']")
driver.find_element_by_css_selector("input[type='password']").send_keys("demoadmin")

driver.find_element_by_xpath("//button[@type='submit']").click()

driver.find_element_by_css_selector("button[data-target='#quickbook']").click()

driver.find_element_by_id("apply").click()






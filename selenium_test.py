from selenium import webdriver
import time

driver = webdriver.Chrome()
time.sleep(5)
driver.get("https://www.amazon.com/")
breakpoint()

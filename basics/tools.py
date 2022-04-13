from selenium import webdriver
from selenium.webdriver.support.select import Select
from selenium.webdriver.common.by import By

browser = webdriver.Chrome()
browser.get("http://techstepacademy.com/training-ground")


sel = browser.find_element(By.ID, 'sel1')
my_select = Select(sel)
my_select.select_by_index(2)
my_select.select_by_value('third')
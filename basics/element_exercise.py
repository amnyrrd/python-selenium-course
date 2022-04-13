# enter into demo environment
# source ~/venvs/demoenv39/bin/activate

from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()

browser.get("http://techstepacademy.com/training-ground")

css_input2_locator = "input[id='ipt2']"
xpath_button4_locator = "//button[@id='b4']"

input2_element = browser.find_element(By.ID, 'ipt2')
btn4_element = browser.find_element(By.XPATH, (xpath_button4_locator))

input2_element.send_keys('hey there bud')
btn4_element.click()






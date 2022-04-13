from selenium import webdriver
from selenium.webdriver.common.by import By

# get an element from within an iframe
browser = webdriver.Chrome()
browser.get('http://techstepacademy.com/iframe-training')

iframe = browser.find_element(By.CSS_SELECTOR, "iframe")
browser.switch_to.frame(iframe)
welcome_text = browser.find_element(By.CSS_SELECTOR, "div#block-ec928cee802cf918d26c div p")
print(welcome_text.text)

#leave iframe and find another element
browser.switch_to.default_content()
title = browser.find_element(By.CSS_SELECTOR, 'div#block-5d3de848045889000188d389 div p')
title_text = title.text
print(title_text)

from selenium import webdriver
from selenium.webdriver.common.by import By
from lxml import etree

browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')

# find merchants by xpath
divs = browser.find_element(By.XPATH, '//div/span/..')

# find merchants using etree
tree = etree.HTML(browser.page_source)
merchant_divs = tree.findall('.//div/span/..')
first_merchant = merchant_divs[0]
second_merchant = merchant_divs[1]
print(first_merchant.find('./span/b').text)
print(second_merchant.find('./span/b').text)

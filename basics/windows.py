from selenium import webdriver
from selenium.webdriver.common.by import By

# opens two seperate browser windows
# browser1 = webdriver.Chrome()
# browser2 = webdriver.Chrome()

# browser1.get("http://techstepacademy.com/training-ground")
# browser2.get("https://google.com")

# tabs
browser3 = webdriver.Chrome()
browser3.get('http://techstackacademy.com/training-ground"')
browser3.execute_script('window.open("http://techstackacademy.com/training-ground","_blank");')
browser3.execute_script('window.open("http://techstackacademy.com/training-ground","_blank");')
browser3.execute_script('window.open("http://techstackacademy.com/training-ground","_blank");')
browser3.execute_script('window.open("http://techstackacademy.com/training-ground","_blank");')
browser3.execute_script('window.open("http://google.com","_blank");')

print(len(browser3.window_handles))
from selenium import webdriver
from selenium.webdriver.common.by import By
browser = webdriver.Chrome()
browser.get('https://techstepacademy.com/trial-of-the-stones')

# rock
rock_input = browser.find_element(By.ID, 'r1Input')
rock_button = browser.find_element(By.ID, 'r1Btn')
rock_input.send_keys('ROCK')
rock_button.click()


# riddle
# //button[@id='b4']
riddle_input = browser.find_element(By.ID, 'r2Input')
riddle_button = browser.find_element(By.ID, 'r2Butn')
riddle_answer = browser.find_element(By.XPATH, '//div[@id="passwordBanner"]/h4[text()]')
riddle_input.send_keys(riddle_answer.text)
riddle_button.click()

# richest
richest_input = browser.find_element(By.ID, 'r3Input')
richest_button = browser.find_element(By.ID, 'r3Butn')
richest_answer = browser.find_element(By.XPATH, '//b[text()="Jessica"]')
richest_input.send_keys(richest_answer.text)
richest_button.click()

# check answers
check_answers_button = browser.find_element(By.ID, 'checkButn')
complete_msg = browser.find_element(By.ID, 'trialCompleteBanner')
check_answers_button.click()

# assert
assert complete_msg.text == 'Trial Complete'
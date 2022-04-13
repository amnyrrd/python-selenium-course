from selenium import webdriver
from webdriver_manager.chrome import ChromeDriverManager

from pages.training_ground import TrainingGroundPage
from pages.trial_page import TrialPage

# test setup
browser = webdriver.Chrome(ChromeDriverManager().install())

# trial page
trial_page = TrialPage(driver=browser)
trial_page.go()
trial_page.stone_input.input_text('ROCK')
trial_page.stone_button.click()
input()

# training ground page
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
assert trng_page.button1.text == 'Button1'
input()

browser.quit()
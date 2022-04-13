from selenium import webdriver
from selenium.webdriver.common.by import By
from webdriver_manager.chrome import ChromeDriverManager


# the class the test relies on
class TrainingGroundPage:
  def __init__(self, driver):
    self.driver = driver
    self.url = 'https://techstepacademy.com/training-ground'

  def go(self):
    self.driver.get(self.url)

  def type_input_field(self, text):
    inpt = self.driver.find_element(By.ID, 'ipt1')
    inpt.clear()
    inpt.send_keys(text)
    return None

  def get_input_text(self):
    input = self.driver.find_element(By.ID, 'ipt1')
    elem_text = input.get_attribute('value')
    return elem_text

  def click_button_1(self):
    button = self.driver.find_element(By.ID, 'b1')
    button.click()
    return None

# test setup
browser = webdriver.Chrome(ChromeDriverManager().install())
test_value = 'testing testing 1 2' 

# the test
trng_page = TrainingGroundPage(driver=browser)
trng_page.go()
trng_page.type_input_field(test_value)
txt_from_input = trng_page.get_input_text()
print(txt_from_input)
assert txt_from_input == test_value
trng_page.click_button_1()
print('YA BABY')
from selenium.webdriver.common.by import By
from .base_page import BasePage
from .base_element import BaseElement
from .locator import Locator

class TrainingGroundPage(BasePage):
  
  url = 'https://techstepacademy.com/training-ground/'

  @property
  def button1(self):
    locator = Locator(By.ID, 'b1')
    return BaseElement(driver=self.driver, locator=locator)
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import data
import configuration

class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

class OrderFormPage(BasePage):

    nameField = (By.XPATH, "//input[@placeholder='* First name']" )
    lastNameField = (By.XPATH, "//input[@placeholder='* Last name'" )
    addressField = (By.XPATH, "//input[@placeholder='* Address']" )
    #este campo de abajo es una lista desplegable, se puede usar asi?
    metroStateField = (By.XPATH, "//input[@placeholder='* Estación de metro']")
    phoneField = (By.XPATH, "//input[@placeholder='* Phone']" )
    rentTime = (By.ID, )
    deliveryDate = (By.ID, )
    commentField = (By.ID, )
    colorField = (By.ID, )
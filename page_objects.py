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

    pedirButton = (By.XPATH, "//button[contains(@class, 'Button_Button__ra12g'")
    nameField = (By.XPATH, "//input[@placeholder='* First name']" )
    lastNameField = (By.XPATH, "//input[@placeholder='* Last name'" )
    addressField = (By.XPATH, "//input[@placeholder='* Address']" )
    #este campo de abajo es una lista desplegable, se puede usar asi?
    metroStationOption = lambda self, station_name: (By.XPATH, f"//div[contains(@class, 'select-search__option') and text()='{station_name}']")
    phoneField = (By.XPATH, "//input[@placeholder='* Phone']" )
    rentTime = (By.XPATH, "//input[@placeholder='* Fecha de entrega']" )
    deliveryDate = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and text()='* Periodo de alquiler']")
    rentTimeOption = lambda self, days: (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{days} días']")
    commentField = (By.XPATH, "//input[contains(@class, 'Input_Input__1in_Z']"
    colorField = (By.ID, ))
    nextButton = (By.XPATH)

    def select_scooter_color(self, color):
        if color == 'black':
            self.driver.find_element(*self.blackColor).click()
        elif color == 'gray':
            self.driver.find_element(*self.grayColor).click()
        else:
            raise ValueError("Invalid color. Choose 'black' or 'gray'.")


    def select_metro_station(self, station_name):
        try:
            # 1. Hacer clic en el campo para desplegar la lista
            self.wait.until(EC.element_to_be_clickable(self.metroStateField)).click()

            # 2. Esperar a que la opción de la estación sea visible y hacer clic en ella
            station_locator = self.metroStationOption(station_name)
            self.wait.until(EC.element_to_be_clickable(station_locator)).click()

        except TimeoutException:
            print(f"La estación '{station_name}' no se pudo seleccionar o no se encontró en el tiempo de espera.")
        except NoSuchElementException:
            print(f"El locator para la estación '{station_name}' no es correcto.")

    # Nuevo método para seleccionar el período de alquiler
    def select_rental_period(self, days):
        """
        Hace clic en el campo de período de alquiler y selecciona la opción deseada.
        :param days: El número de días de alquiler (ej. "dos" o "cinco").
        """
        try:
            # 1. Hacer clic en el campo para desplegar la lista
            self.wait.until(EC.element_to_be_clickable(self.rentTimeField)).click()

            # 2. Esperar a que la opción de días sea visible y hacer clic en ella
            option_locator = self.rentTimeOption(days)
            self.wait.until(EC.element_to_be_clickable(option_locator)).click()

        except TimeoutException:
            print(
                f"El período de alquiler '{days} días' no se pudo seleccionar o no se encontró en el tiempo de espera.")
        except NoSuchElementException:
            print(f"El locator para el período de alquiler '{days} días' no es correcto.")


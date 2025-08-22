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

    # Localizadores para los campos del formulario de la primera página
    nameField = (By.XPATH, "//input[@placeholder='* First name']")
    lastNameField = (By.XPATH, "//input[@placeholder='* Last name']")
    addressField = (By.XPATH, "//input[@placeholder='* Address']")
    metroStateField = (By.XPATH, "//input[@placeholder='* Estación de metro']")
    metroStationOption = lambda self, station_name: (By.XPATH,
                                                     f"//div[contains(@class, 'select-search__option') and text()='{station_name}']")
    phoneField = (By.XPATH, "//input[@placeholder='* Phone']")
    nextButton = (By.XPATH, "//button[contains(text(),'Siguiente')]")

    # Localizadores para los campos de la segunda página del formulario
    deliveryDateField = (By.XPATH, "//input[@placeholder='* Fecha de entrega']")
    rentTimeField = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and text()='* Periodo de alquiler']")
    rentTimeOption = lambda self, days: (By.XPATH,
                                         f"//div[contains(@class, 'Dropdown-option') and text()='{days} días']")
    commentField = (By.XPATH, "//input[@placeholder='Comentario para el mensajero']")

    # Localizadores para los botones y campos de radio
    pedirButton = (By.XPATH, "//button[text()='Pedir']")
    blackColor = (By.ID, "black")
    grayColor = (By.ID, "grey")

    def click_order_button(self):
        self.driver.find_element(*self.pedirButton).click()

    def fill_name_field(self, name):
        self.driver.find_element(*self.nameField).send_keys(name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.lastNameField).send_keys(last_name)

    def fill_address(self, address):
        self.driver.find_element(*self.addressField).send_keys(address)

    def fill_phone_number(self, phone):
        self.driver.find_element(*self.phoneField).send_keys(phone)

    def select_scooter_color(self, color):
        if color == 'black':
            self.driver.find_element(*self.blackColor).click()
        elif color == 'gray':
            self.driver.find_element(*self.grayColor).click()
        else:
            raise ValueError("Invalid color. Choose 'black' or 'gray'.")

    def select_metro_station(self, station_name):
        try:
            self.wait.until(EC.element_to_be_clickable(self.metroStateField)).click()
            station_locator = self.metroStationOption(station_name)
            self.wait.until(EC.element_to_be_clickable(station_locator)).click()
        except TimeoutException:
            print(f"La estación '{station_name}' no se pudo seleccionar o no se encontró en el tiempo de espera.")
        except NoSuchElementException:
            print(f"El locator para la estación '{station_name}' no es correcto.")

    def select_rental_period(self, days):
        try:
            self.wait.until(EC.element_to_be_clickable(self.rentTimeField)).click()
            option_locator = self.rentTimeOption(days)
            self.wait.until(EC.element_to_be_clickable(option_locator)).click()
        except TimeoutException:
            print(
                f"El período de alquiler '{days} días' no se pudo seleccionar o no se encontró en el tiempo de espera.")
        except NoSuchElementException:
            print(f"El locator para el período de alquiler '{days} días' no es correcto.")

    def fill_comment(self, comment):
        self.driver.find_element(*self.commentField).send_keys(comment)



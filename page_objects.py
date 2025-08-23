from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
import data
import configuration
from data import deliveryDate


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


class OrderFormPage(BasePage):

    # Localizadores para los campos del formulario de la primera página
    cookie_button = (By.CSS_SELECTOR, 'button[class="App_CookieButton__3cvqF"]')
    nameField = (By.CSS_SELECTOR, 'input[placeholder="* Nombre"]')
    lastNameField = (By.CSS_SELECTOR, 'input[placeholder="* Apellido"]')
    addressField = (By.CSS_SELECTOR, 'input[placeholder="* Dirección: a dónde llevar el scooter"]')
    metroStateField = (By.CSS_SELECTOR, 'input[placeholder="* Estación de metro"]')
    metroStationOption = lambda self, station_name: (By.XPATH,
                                                     f"//div[contains(@class, 'select-search__option') and text()='{station_name}']")
    phoneField = (By.CSS_SELECTOR, 'input[placeholder="* Teléfono: el repartidor o repartidora te llamará"]')
    next_pedir_Button = (By.CSS_SELECTOR, 'button[class="Button_Button__ra12g Button_Middle__1CSJM"]')

    # Localizadores para los campos de la segunda página del formulario
    deliveryDateField = (By.CSS_SELECTOR, 'input[placeholder= "* Fecha de entrega"]')
    rentTimeField = (By.XPATH, "//div[contains(@class, 'Dropdown-placeholder') and text()='* Periodo de alquiler']")
    rentTimeOption = lambda self, days: (By.XPATH,
                                         f"//div[contains(@class, 'Dropdown-option') and text()='{days} días']")
    commentField = (By.CSS_SELECTOR, 'input[placeholder="Comentario"]')

    # Localizadores para los botones y campos de radio
    pedirButton = (By.CSS_SELECTOR, 'button[class="Button_Button__ra12g"]')
    blackColor = (By.CSS_SELECTOR, 'input[id="black"]')
    grayColor = (By.CSS_SELECTOR, 'input[id="grey"]')

    def click_order_button(self):
        self.driver.find_element(*self.pedirButton).click()

    def fill_name_field(self, name):
        self.driver.find_element(*self.nameField).send_keys(name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.lastNameField).send_keys(last_name)

    def fill_address(self, address):
        self.driver.find_element(*self.addressField).send_keys(address)

    def select_metro_station(self, station_name):
        try:
            self.wait.until(EC.element_to_be_clickable(self.metroStateField)).click()
            station_locator = self.metroStationOption(station_name)
            self.wait.until(EC.element_to_be_clickable(station_locator)).click()
        except TimeoutException:
            print(f"La estación '{station_name}' no se pudo seleccionar o no se encontró en el tiempo de espera.")
        except NoSuchElementException:
            print(f"El locator para la estación '{station_name}' no es correcto.")

    def fill_phone_number(self, phone):
        self.driver.find_element(*self.phoneField).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.next_pedir_Button).click()

    def set_delivery_date(self, date):
        self.driver.find_element(self.deliveryDateField).send_keys(date)

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

    def select_scooter_color(self, color):
        if color == 'black':
            self.driver.find_element(*self.blackColor).click()
        elif color == 'gray':
            self.driver.find_element(*self.grayColor).click()
        else:
            raise ValueError("Invalid color. Choose 'black' or 'gray'.")

    def fill_comment(self, comment):
        self.driver.find_element(*self.commentField).send_keys(comment)

    def click_finish_button(self):
        self.driver.find_element(*self.next_pedir_Button).click()


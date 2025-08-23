from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException
from selenium.webdriver import Keys
import data
import configuration
from data import deliveryDate


class BasePage:

    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)


class OrderFormPage(BasePage):

    cookie_button = (By.CSS_SELECTOR, 'button[class="App_CookieButton__3cvqF"]')
    order_button_top = (By.CSS_SELECTOR, 'button[class="Button_Button__ra12g"]')
    # Localizadores para los campos de texto
    nameField = (By.CSS_SELECTOR, 'input[placeholder="* Nombre"]')
    lastNameField = (By.CSS_SELECTOR, 'input[placeholder="* Apellido"]')
    addressField = (By.CSS_SELECTOR, 'input[placeholder="* Dirección: a dónde llevar el scooter"]')
    metroStateField = (By.CSS_SELECTOR, 'input[placeholder="* Estación de metro"]')
    phoneField = (By.CSS_SELECTOR, 'input[placeholder="* Teléfono: el repartidor o repartidora te llamará"]')
    next_button = (By.XPATH, "//button[text()='Siguiente']")

    # --- Localizadores de la segunda página del formulario ---
    deliveryDateField = (By.CSS_SELECTOR, 'input[placeholder="* Fecha de entrega"]')
    rentTimeField = (By.CSS_SELECTOR, '.Dropdown-placeholder')
    rentTimeSelection = (By.XPATH, "//div[text()='un día']")
    commentField = (By.CSS_SELECTOR, 'input[placeholder="Comentario"]')
    finish_order_button = (By.XPATH, "//div[contains(@class, 'Order_Buttons')]/button[text()='Pedir']")

    # Localizadores para los colores
    blackColor = (By.CSS_SELECTOR, 'input[id="black"]')
    grayColor = (By.ID, 'grey')

    # --- Localizadores dinámicos (creados como métodos para mayor claridad) ---
    def metro_station_option(self, station_name):
        return (By.XPATH, f"//div[contains(@class, 'select-search__option') and text()='{station_name}']")

    def rent_time_option(self, days):
        return (By.XPATH, f"//div[contains(@class, 'Dropdown-option') and text()='{days} días']")

    # --- Localizador para el mensaje de éxito y el número de seguimiento ---
    order_success_message = (By.XPATH, "//div[text()='¡Pedido está registrado!']")
    track_number_element = (By.CSS_SELECTOR, '.Order_Text__2tQ9u')

    def __init__(self, driver):
        super().__init__(driver)

    def click_cookie_button(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.cookie_button)).click()
            print("Cookies aceptadas.")
        except TimeoutException:
            print("El botón de cookies no se encontró. Continuando con la prueba.")

    def click_order_button_top(self):
        self.wait.until(EC.element_to_be_clickable(self.order_button_top)).click()

    def fill_name_field(self, name):
        self.driver.find_element(*self.nameField).send_keys(name)

    def fill_last_name(self, last_name):
        self.driver.find_element(*self.lastNameField).send_keys(last_name)

    def fill_address(self, address):
        self.driver.find_element(*self.addressField).send_keys(address)

    def select_metro_station(self, station_name):
            self.wait.until(EC.element_to_be_clickable(self.metroStateField)).click()
            self.driver.find_element(*self.metroStateField).send_keys(station_name + Keys.DOWN + Keys.ENTER)

    def fill_phone_number(self, phone):
        self.driver.find_element(*self.phoneField).send_keys(phone)

    def click_next_button(self):
        self.driver.find_element(*self.next_button).click()

    def set_delivery_date(self, date):
        self.driver.find_element(*self.deliveryDateField).send_keys(date + Keys.ENTER)

    def select_rental_period(self, days):
            self.wait.until(EC.element_to_be_clickable(self.rentTimeField)).click()
            self.wait.until(EC.element_to_be_clickable(self.rentTimeSelection)).click()

    def select_scooter_color(self):
        self.driver.find_element(*self.blackColor).click()

    def fill_comment(self, comment):
        self.driver.find_element(*self.commentField).send_keys(comment)

    def click_finish_button(self):
        self.driver.find_element(*self.finish_order_button).click()

    def get_track_number(self):
            self.wait.until(EC.visibility_of_element_located(self.order_success_message))
            track_element = self.wait.until(EC.visibility_of_element_located(self.track_number_element))
            track_number = track_element.text
            print(f"Número de seguimiento encontrado: {track_number}")
            return track_number

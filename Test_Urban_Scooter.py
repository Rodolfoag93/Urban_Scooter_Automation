import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import random
import time
import page_objects
import data
from page_objects import OrderFormPage
from API_URBAN_SCOOTER import CourierApi


url_test_ui = data.Urban_routes_URl
url_test_api = data.API_Url_Urban_Routes

@pytest.fixture(scope="function")
def driver():
    options = webdriver.ChromeOptions()
    options.add_argument("--window-size={width},{height}")

    driver = webdriver.Chrome(options=options)
    yield driver
    driver.quit()

@pytest.mark.parametrize("driver", [(1920, 1080), (1280, 720)], indirect=True)
def test_successfull_order_creation(driver: webdriver.Chrome):
    order_page =OrderFormPage(driver)
    driver.get(url_test_ui)
    order_page.click_cookie_button()
    window_size = driver.get_window_size
    print(f"Inicio de prueba de reacion de orden en resolucion {
    window_size()['width']}x{window_size()['height']}")

    order_page.click_order_button()
    order_page.fill_name_field(data.firstName)
    order_page.fill_last_name(data.lastName)
    order_page.fill_address(data.address)
    order_page.select_metro_station(data.metroStation)
    order_page.fill_phone_number(data.phone)

    order_page.click_next_button()

    order_page.set_delivery_date(data.deliveryDate)
    order_page.select_rental_period(data.rentTime)
    order_page.select_scooter_color(data.color)
    order_page.fill_comment(data.comment)

    order_page.click_finish_button()
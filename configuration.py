import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.expected_conditions import visibility_of_element_located
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException, NoSuchElementException, WebDriverException

import data


def setup_driver():
    try:
        options = webdriver.ChromeOptions()
        options.add_argument('--headless')
        return webdriver.Chrome(options=options)
    except WebDriverException as e:
        print(f"Error al iniciar el driver de chrome: {e}")
        return None

def run_tests_with_different_sizes(sizes):
    for width, height in sizes:
        print(f"\nProbando con el tamaño de la ventana: {width}x{height}")
        driver = setup_driver()
        if driver:
            try:
                driver.set_window_size(width, height)
                print("¡El driver se ah iniciado correctamente")
                driver.get(data.Urban_routes_URl)
                wait = WebDriverWait(driver, 10)
                wait.until(EC.visibility_of_element_located((By.TAG_NAME, "body")))
                print("Pagina cargada y lista para interacción")

            finally:
                driver.quit()
        else:
            print("El script no pudo continuar debido a un error al inciar el driver.")

if __name__ == '__main__':
    window_sizes_to_test = [
        (1280, 720),
        (1920, 720)
    ]
    run_tests_with_different_sizes(window_sizes_to_test)
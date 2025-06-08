from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
service = Service("webscraper\msedgedriver.exe")
driver = webdriver.Edge(service=service)

try:

    driver.get('https://retorika.es/tabbycats/list')
    driver.implicitly_wait(0.5)
    """  button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-target="#info_38081"]'))
    )
    button.click()
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.modal-body.lead'))
    )
    print(modal.text) """
finally:
    driver.quit()


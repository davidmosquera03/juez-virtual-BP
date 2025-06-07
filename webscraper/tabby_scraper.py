from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
service = Service("webscraper\msedgedriver.exe")
driver = webdriver.Edge(service=service)

try:

    driver.get('https://cmude2024.calicotab.com/open/motions/')
    driver.get('https://ixtrd.calicotab.com/ixtrdunis/motions/')
    driver.implicitly_wait(0.5)
    """  button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.CSS_SELECTOR, 'button[data-target="#info_38081"]'))
    )
    button.click()
    modal = WebDriverWait(driver, 10).until(
        EC.visibility_of_element_located((By.CSS_SELECTOR, 'div.modal-body.lead'))
    )
    print(modal.text) """
    cards = driver.find_elements(By.CSS_SELECTOR, "div.card.mt-3")

    for card in cards:
        # Get main lead text
        lead = card.find_element(By.CSS_SELECTOR, "div.mr-auto.pr-3.lead")
        print("Main text:", lead.text)
        
        # Get modal text (directly from DOM, no click needed)
        modal = card.find_element(By.CSS_SELECTOR, "div.modal-body.lead")
        modal_txt =  modal.get_attribute("innerHTML").strip()  # Gets raw HTML
        print()
finally:
    driver.quit()


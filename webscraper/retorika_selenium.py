from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip  # pip install pyperclip
service = Service("webscraper\\msedgedriver.exe")
driver = webdriver.Edge(service=service)
links = []
try:
    driver.get("https://retorika.es/tabbycats/list")
    time.sleep(4)

    # Wait for the search input to appear
    search_input = driver.find_element(By.CLASS_NAME, "searchbar-input")
    search_input.send_keys("WUDC")

    time.sleep(2)
    # Send search and trigger Angular's input handle
    search_results = driver.find_elements(By.CSS_SELECTOR, "ion-item.ret-item")
    print(len(search_results))
    
    for result in search_results:
        result.click()
        text = result.text
        print("clicked",text)
        time.sleep(1)  # Wait for clipboard copy
        
        # Get clipboard content
        link = pyperclip.paste()
        links.append(link)
        
        time.sleep(0.5)
finally:
    driver.quit()
    print(links)

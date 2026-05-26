# Extract Tabbycat links from Retorika and save them as .txt
from selenium import webdriver
from selenium.webdriver.edge.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
import pyperclip  # instalar pyperclip
service = Service("webscraper\\msedgedriver.exe")
driver = webdriver.Edge(service=service)
links = []

search_word = "WUDC"
try:
    driver.get("https://retorika.es/tabbycats/list")
    time.sleep(4)

    # Esperar a barra de busqueda
    search_input = driver.find_element(By.CLASS_NAME, "searchbar-input")
    search_input.send_keys(search_word)

    time.sleep(2)
    # Escribir en barra
    search_results = driver.find_elements(By.CSS_SELECTOR, "ion-item.ret-item")
    print(len(search_results))
    
    for result in search_results:
        result.click()
        text = result.text
        print("clicked",text)
        time.sleep(1)  # Esperar para copiar a clipboard
        
        # Obtener contenido de clipboard
        link = pyperclip.paste()
        links.append(link)
        
        time.sleep(0.5)
finally:
    driver.quit()
    # escribir a txt los enlaces
    with open("data/links.txt","a") as f:
        for l in links:
            f.write(f"{l}\n")


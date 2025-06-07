from bs4 import BeautifulSoup
import time
import requests
def scrape_basic(url):
  """
  scrape without checking robots.txt
  """
  time.sleep(1)
  response = requests.get(url)
  if response.status_code == 200:
    s = BeautifulSoup(response.text, 'html.parser')
    # Process data
  else:
    print("Error:", response.status_code)
  return s

s = scrape_basic('https://ixtrd.calicotab.com/ixtrdunis/motions/')
cards = s.find_all("div",class_="card mt-3")
for card in cards:
  print(card.find("div",class_="mr-auto pr-3 lead").get_text().strip())
  print(card.find("div",class_="modal-body lead").get_text().strip())


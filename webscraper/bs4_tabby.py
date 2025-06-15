from bs4 import BeautifulSoup
import time
import json
import requests
def scrape_basic(url):
  """
  scrape without checking robots.txt
  """
  time.sleep(1)
  response = requests.get(url)
  if response.status_code == 200:
    s = BeautifulSoup(response.text, 'html.parser')

  else:
    print("Error:", response.status_code)
  return s

def format_link(link):
  return "/".join(link.split("/")[:4])+"/"

def get_infoslide(card):
  try:
    info_slide = card.find("div",class_="modal-body lead").get_text().strip()
  except:
    info_slide = "Ninguna"
  return info_slide

# saves motions as txt or JSON on a given path

def scrape_tabbycat(url):
  """
  scrapes a tabbycat url

  Input:
    url of tabbycat.
    format: https://name.calicotab.com/name2/
  """
  motions_list = []
  try: # probar URL motions
    s = scrape_basic(url+"motions")
    cards = s.find_all("div",class_="card mt-3")
    for card in cards:
      motion = card.find("div",class_="mr-auto pr-3 lead").get_text().strip()
      info_slide = get_infoslide(card)
      #print(motion)
      #print(info_slide)
      motions_list.append({"motion":motion,"info_slide":info_slide})
  except:
    try: # Probar url motions/statistics
      s = scrape_basic(url+"motions/statistics")
      cards = s.find_all("div",class_="list-group mt-3")
      for card in cards:
        motion = card.find("h4",class_="mb-3 mt-1").get_text().strip()
        #print(motion)
        info_slide = get_infoslide(card)
        #print(info_slide)
        motions_list.append({"motion":motion,"info_slide":info_slide})
    except:
      return motions_list
  finally:
    return motions_list

def generate_json_motions():
  json_list = []
  with open("data/test.txt","r") as f:
    for line in f:
      link = line.strip("\n")
      motions = scrape_tabbycat(format_link(link))
      print(len(motions))
      if len(motions)>0:
        for x in motions:
          json_list.append(x)
  #print(json.dumps(json_list, indent=2,ensure_ascii=False))
  print(len(json_list))
  # store JSON 
  with open("data/motions.json","w",encoding="utf-8") as f:
    f.write(json.dumps(json_list, indent=2,ensure_ascii=False))


generate_json_motions()
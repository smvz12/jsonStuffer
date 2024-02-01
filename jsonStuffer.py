import json


from selenium import webdriver
from selenium.webdriver.firefox.service import Service
from selenium.webdriver.firefox.options import Options
from webdriver_manager.firefox import GeckoDriverManager

options = Options()
elem = []
jsonQuran = {}

driver = webdriver.Firefox(service=Service(GeckoDriverManager().install()),
                           options=options)
driver.get("https://sacred-texts.com/isl/quran/index.htm")

links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    if "Sūra" in link.get_attribute("innerHTML"):
        link.click()
        break
links = driver.find_elements("xpath", "//a[@href]")
for link in links:
    if "Section" in link.get_attribute("innerHTML"):
        link.click()
        break
for verse in range(557):
    texts = driver.find_elements("tag name", "p")
    for x in texts:
        elem.append(x.text)
        print(x.text)
    links = driver.find_elements("xpath", "//a[@href]")
    for link in links:
        if "Section" in link.get_attribute("innerHTML"):
            link.click()


for x, y in enumerate(elem):
    jsonQuran[x] = y
json_object = json.dumps(elem, indent=4)
with open("quran.json", "w") as outfile:
    outfile.write(json_object)

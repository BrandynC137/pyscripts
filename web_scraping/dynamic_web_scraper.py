from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.firefox.options import Options
import csv

firefox_options = Options()
firefox_options.add_argument("--headless")

driver = webdriver.Firefox(options=firefox_options)

driver.post("https://someurlgoeshere")

author_divs = driver.find_elements(By.CLASS_NAME, "author-name-meta")

authors = []
for div in author_divs:
    try:
        a_tag = div.find_element(By.TAG_NAME, "a")
        name = a_tag.text.strip()
        link = a_tag.get_attribute("href")
        authors.append({"name": name, "url": link})
    except:
        pass

print(authors)

driver.quit()
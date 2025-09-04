import requests
from bs4 import BeautifulSoup
import csv

url = "https://www.reddit.com/r/nextfuckinglevel/comments/1n5l4br/effectiveness_of_a_robot_vacuum/"
response = requests.get(url)
html = response.text
print(html)

soup = BeautifulSoup(html, "html.parser")

authors = soup.find_all("div", class_="author-name-meta")
for author in authors: 
    author = authors.find("a").get_text(strip=True)
    print(author.text.strip())

with open("data.csv", "w", newline="", encoding="utf-8") as file:
    writer = csv.writer(file)
    for author in authors:
        writer.writerow([author.text.strip()])
# -*- coding: utf-8 -*-
from bs4 import BeautifulSoup
import requests

url='https://www.worldometers.info/coronavirus'
response = requests.get(url,timeout=5)
content = BeautifulSoup(response.content, "html.parser")


header = content.find('div', attrs={"class": "label-counter"})
time = header.find_next('div')

print(header.text)
print(time.text)

main_data = content.findAll('div',attrs={'id':'maincounter-wrap'})

for entry in main_data:
    title = entry.find('h1')
    number = title.findNext('span')
    print(title.text)
    print(number.text)

#print(main_data)

#/html/body/div[3]/div[2]/div[1]/div/div[4]/div/span

#country_link = time.find_next('div').find('a')
#print(country_link)




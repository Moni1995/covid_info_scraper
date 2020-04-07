# -*- coding: utf-8 -*-
from BeautifulSoup4 import BeautifulSoup
import requests
import re
import pandas as pd
from tabulate import tabulate

def main():

    url='https://www.worldometers.info/coronavirus'
    response = requests.get(url,timeout=5)
    content = BeautifulSoup(response.content, "html.parser")


    header = content.find('div', attrs={"class": "label-counter"})
    time = header.find_next('div')

    print(header.text)
    print(time.text)

    main_data = content.findAll('div',attrs={'id':'maincounter-wrap'})

    world_info = {}

    for entry in main_data:
        title = entry.find('h1')
        number = title.findNext('span')
        world_info[title.text]=parse_int(number.text)

    #print(world_info)

    active_info = {}

    closed_info = {}

    active_str = 'Active Cases'

    active_info = find_info(content,active_str,active_info)

    print(active_info)

    closed_str = 'Closed Cases'

    closed_info = find_info(content, closed_str,closed_info)

    print(closed_info)

    result={}

    df = country_table(content,result)

    writer = pd.ExcelWriter('covid19.xlsx', engine='xlsxwriter')

    ddf = pd.DataFrame(df[0])

    ddf.to_excel(writer, sheet_name='Sheet1')


    writer.save()

    print(ddf)

    #result = df[0].to_json(orient='records')

    tabulated = tabulate(df[0], headers='keys', tablefmt='psql')

    print(tabulated)



def find_info(page_content, str,info):
    unformatted = page_content.find(text=re.compile(str))
    total_number = unformatted.parent.parent.parent.find('div', attrs={'class': 'number-table-main'})
    label1 = total_number.findNext('div')
    info[label1.text] = parse_int(total_number.text)

    left_section = label1.findNext('div')
    left_number = left_section.find('span',attrs={'class': 'number-table'})
    left_label = left_number.findNext('div')
    info[left_label.text] = parse_int(left_number.text)

    right_section = left_label.findNext('div')
    right_number = right_section.find('span', attrs={'class': 'number-table'})
    right_label = right_number.findNext('div')
    info[right_label.text] = parse_int(right_number.text)

    return info

def parse_int(str):
    return int(str.replace(',',''))


def country_table(tbl,result):
    data=tbl.find('table',attrs={'id':'main_table_countries_today'})
    df = pd.read_html(str(data))

    return df


main()









#print(main_data)

#/html/body/div[3]/div[2]/div[1]/div/div[4]/div/span

#country_link = time.find_next('div').find('a')
#print(country_link)



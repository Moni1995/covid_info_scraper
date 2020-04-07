from bs4 import BeautifulSoup
import requests
import re
import sys
import pandas as pd
from tabulate import tabulate
import time
from selenium import webdriver

def main():
    argv = sys.argv[1]
    url='https://www.worldometers.info/coronavirus/country/'+argv+'/'
    print(url)
    response = requests.get(url,timeout=5)
    content = BeautifulSoup(response.content, "html.parser")
    data_unformatted = content.find_all('script', attrs = {'type':'text/javascript'})
    #print(data_unformatted)
    #print(content)
    start=0
    labels = []
    data = []
    for d in data_unformatted:
        ds = str(d)
        label_index= ds.find('name: ')
        label_end = ds.find(",",label_index)
        labels.append(ds[label_index:label_end])
        pos = ds.find('data:')
        end = ds.find(']',pos)
        print(ds[pos:end+1])
        data.append(ds[pos:end+1])
        #print(str(d))


    new_labels = []
    new_data = []
    print(labels)
    for l in labels:
        if l:
            new_label = l[7:-1]
            new_labels.append(new_label)

    for dt in data:
        if dt:
            new_dt = dt[7:-1]
            new_data.append(new_dt)
    print(new_labels)
    print(new_data)




    #temp = driver.execute_script('return window.Highcharts.charts[0]''.series[0].options.data')
    #data = [item[1] for item in temp]
    #print(data)
    #print(test)
   


main()
from bs4 import BeautifulSoup
import requests
import re
import sys
import pandas as pd
from tabulate import tabulate
import time
from selenium import webdriver
import pandas as pd
import datetime as date
from tabulate import tabulate

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
   # print(new_labels)
    #print(new_data)

    #A dict of data {label: data}
    data_list =[]
    for d in new_data:
        parsed = d.split(',')
        numbers = []
        for number in parsed:
            if(number == 'null'):
                numbers.append(0)
            elif(number == '"nan"'):
                numbers.append(0)
            else:
                numbers.append(float(number))
        data_list.append(numbers)



    data={}
    
    for l,d in zip(new_labels, data_list):
        data.update({l:d})

    print(data)


    data_specified = {}

   

    data_specified.update({"Cases": data['Cases']})

    data_specified.update({"Daily Cases": data['Daily Cases']})

    data_specified.update({"Currently Infected": data['Currently Infected']})

    data_specified.update({"Deaths": data['Deaths']})

    data_specified.update({"Daily Deaths": data['Daily Deaths']})


    df = pd.DataFrame(data_specified)

    print(df)

    write_file(df,argv)

def write_file(df,country):

    filename = "covid-19-" + str(date.datetime.now())[0:10] + "-"+country +".xlsx"
    
    writer = pd.ExcelWriter(filename, engine='xlsxwriter')

    #ddf = pd.DataFrame(df[0])

    sheetname = str(date.datetime.now())

    df.to_excel(writer, sheet_name=sheetname[0:10])


    writer.save()



    #temp = driver.execute_script('return window.Highcharts.charts[0]''.series[0].options.data')
    #data = [item[1] for item in temp]
    #print(data)
    #print(test)
   


main()
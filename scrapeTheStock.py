# -*- coding: utf-8 -*-
"""
Created on Mon Dec 16 17:28:41 2019

@author: MohammedZ666
"""

from selenium import webdriver
import csv

driver = webdriver.Chrome()
driver.get("https://www.dsebd.org/data_archive.php")

elements = (driver.find_element_by_id('Symbol')).find_elements_by_tag_name('option')
elements.pop(0);# popping the default select option
k = 0

for k in range(len(elements)):
    

    option = elements[k]
    company = option.text
    option.click() # select() in earlier versions of webdriver
    fromDate = driver.find_element_by_id("DayEndSumDate1")
    fromDate.send_keys("11/03/2019")

    toDate = driver.find_element_by_id("DayEndSumDate2")
    toDate.send_keys("12/15/2019")

    driver.find_element_by_name("ViewDayEndArchive").click();

    xpath = "/html/body/table[2]/tbody/tr/td[2]/table/tbody/tr[2]/td[1]/table/tbody/tr"
    #tr[1]/td[1]

    i = 1
    row_list = []
    web_rows = driver.find_elements_by_xpath(xpath)


    while len(web_rows) >= i:
        j = 1
        row = []
       #updating the percentage completed
        print(str(((k/len(elements))*(1 + (i/len(web_rows)))) * 100 ) +"% completed")
      
        while j<=12 :

            web_columns = driver.find_element_by_xpath(xpath+"["+str(i)+"]"+"/td["+str(j)+"]") 
            row.append(web_columns.text)        
            j+=1
   
        row_list.append(row)        
        i+=1
   
    with open('Mined_Goods/'+company+'.csv', 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(row_list)
    driver.execute_script("window.history.go(-1)")
    elements = (driver.find_element_by_id('Symbol')).find_elements_by_tag_name('option')

    


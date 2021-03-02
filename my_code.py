import xml.etree.ElementTree as ET
import sys
import numpy as np 
import csv
mytree = ET.parse('data.xml')
myroot = mytree.getroot()
for root in myroot:
    for result in root:
        arr=[]
        for element in result:
            if element.tag == 'problem':
                for field in element:
                    if field.tag == 'contestId':
                        arr.append(field.text)
                        str1=field.text
                    if field.tag == 'index':
                        arr.append(field.text)
                        str2=field.text
                        arr.append('https://codeforces.com/contest/'+ str1 + '/problem/'+ str2)
                    if field.tag == 'name':
                        arr.append(field.text)
                    if field.tag == 'rating':
                        arr.append(field.text)
                    if field.tag == 'tags':
                        for concept in field:
                            arr.append(concept.text)
                        
            if element.text == 'OK':
                print(arr)
                final_list.append(arr)
        
# print(len(final_list))
with open('print.csv','w', newline = '') as out:
    csv_out=csv.writer(out)
#     arr=[]
#     arr.append('Contest ID')
#     arr.append('Problem Code')
#     arr.append('Name')
#     arr.append('Rating')
#     arr.append('URL')
#     arr.append('Problem Tags')
#     csv_out.writerow(arr)
    for item in final_list:
        csv_out.writerow(item)
final_list.clear()
# https://codeforces.com/contest/1487/problem/A
# https://codeforces.com/problemset/problem/1487/A
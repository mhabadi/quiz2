# -*- coding: utf-8 -*-
"""
Created on Thu Sep 22 13:59:22 2022

@author: MoAbadi
"""

import csv
dict_trails={}
with open("Trails.csv", 'r') as file:
    csv_file = csv.DictReader(file)
    for row in csv_file:
        temp=dict(row)
        for objects,items in temp.items():
            dict_trails[objects]=dict_trails.get(objects,[])+[items]


general_condition={}

for index,condition in enumerate(dict_trails['CONDITION']):
    if condition == ' ' or condition == '':
        condition='Unknown' 
    general_condition[condition]=general_condition.get(condition,[])+[index]

#Assume that TRAIL_ID is the required output for condition
def classification_condition(condition):
    object_id=[]
    indexes=general_condition[condition]
    for index in indexes:
        object_id.append(dict_trails['TRAIL_ID'][index])
    return(object_id)

print(general_condition.keys())

print(classification_condition('GOOD'))

def installed_after_2000():
    trail_id=[]
    indexes=






    
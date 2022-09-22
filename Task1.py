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


def classification_condition(condition):
    general_condition={}

    for index1,condition1 in enumerate(dict_trails['CONDITION']):
        if condition1 == ' ' or condition1 == '':
            condition1='Unknown' 
        general_condition[condition1]=general_condition.get(condition1,[])+[index1]
    print(general_condition.keys())
    #Assume that TRAIL_ID is the required output for condition
    object_id=[]
    indexes=general_condition[condition]
    for index in indexes:
        object_id.append(dict_trails['TRAIL_ID'][index])
    return(object_id)

    

#print(classification_condition('GOOD'))



def installed_after_2000(parameter='number'):
    '''paramaters: 'number' : number of trails, 'detail' : trails ID will be printed''' 
    installed_after_2000=[]
    for index,year in enumerate(dict_trails['INST_YEAR']):
        if year=='':
            year='0'
        if int(year) >= 2000:
            installed_after_2000.append((int(year),dict_trails['TRAIL_ID'][index]))
    if parameter=='number':
        print(len(installed_after_2000))
    if parameter=='detail':
        print(installed_after_2000)
        
#installed_after_2000('detail')

def counter_based_condition(condition=1):
    '''condition 1: based on Status=Active
    Condition 2: based on Lightning
    condition 3: Walking and Biking'''
    counter=0
    if condition==1:
        condition=['STATUS','ACTIVE']
    elif condition==2:
        condition=['LIGHT','Y']
    elif condition==3:
        condition=['WALKING','Y','BIKING']
    
    for index,status in enumerate(dict_trails[condition[0]]):        
        if status==condition[1]:
            if len(condition)==3:
                if dict_trails[condition[2]][index]==condition[1]:
                    counter+=1
            elif len(condition)==2:
                counter+=1
    
    print(counter)
            
#counter_based_condition(1)        
    
def can_be_hiked_biked():
    parameters=('TRAIL_NAME', 'CONDITION', 'LIGHT', 'STATUS', 'HIKING', 'BIKING', 'ATV')
    condition=['HIKING','Y','BIKING']
    hiked_biked=[]
    for index,status in enumerate(dict_trails[condition[0]]):        
        if status==condition[1]:
            if dict_trails[condition[2]][index]==condition[1]:
                hiked_biked.append([dict_trails[i][index] for i in parameters])
                    
    for items in hiked_biked:
        print(items)


can_be_hiked_biked()
    
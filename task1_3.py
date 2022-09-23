# -*- coding: utf-8 -*-
"""task1.3.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/13LuC_jUp_NkfuaqaATxs0RQVTgS1MiDh
"""

from pandas import *
 
# reading CSV file
data = read_csv("Trails.csv")
 
# converting column data to list

Status_Active_or_not = data['STATUS'].tolist()
status_count=0
for item in Status_Active_or_not:
  if item=='ACTIVE':
    status_count=status_count+1
print(status_count) 

Lighting_or_not = data['LIGHT'].tolist()
light_count=0
for item in Lighting_or_not:
  if item=='Yes':
    light_count=light_count+1
print(light_count)
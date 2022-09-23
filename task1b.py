from pandas import *
 

data = read_csv("Trails.csv")

Inst_year = data['INST_YEAR'].tolist()
count=0
for item in Inst_year:
  if item>2000:
    count=count+1
print(count)

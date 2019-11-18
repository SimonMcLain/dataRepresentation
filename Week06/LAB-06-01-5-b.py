import pandas as pd
from xlwt import *

pd.read_json("githubusers.json").to_excel("githubuserscheat.xlsx")

data = 'githubusers.json'

# write to an excel file
w = Workbook()
ws = w.add_sheet('githubusers')
row = 0;
ws.write(row, 0, 'login')
#ws.write(row, 1, 'id')
row += 1

for person in data:
  #ws.write(row, 0, person["login"])
  #ws.write(row, 1, user['id'])
  row += 1
w.save('githubusers.xls')

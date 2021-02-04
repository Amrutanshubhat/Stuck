
import csv
import os



wb = openpyxl.load_workbook("ledger-KS9897.xlsx")
f=wb["Equity"]
df = pd.DataFrame(f.values)
df.to_csv('ledger.csv',header=False,index=False,encoding='utf-8')



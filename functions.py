import os
import csv
import openpyxl
import pandas as pd

def xlsx_to_csv():
    wb = openpyxl.load_workbook("ledger.xlsx")
    f=wb["Equity"]
    df = pd.DataFrame(f.values)
    df.to_csv('ledger.csv',header=False,index=False,encoding='utf-8')

def total_csv(holding):
    data_file = os.path.join('./', 'ledger.csv')
    credit=0
    debit=0
    closing=0
    final={"credit":0,"debit":0,"total":0}
    try:
        with open(data_file,'r') as file:
            for line in file:
                line=line.strip()
                line=line.split(',')
                try:
                    if 'Opening' in line[1]:
                        credit=float(line[-1])
                    elif('Funds added' in line[1]):
                        credit+=float(line[-2])
                    elif 'Payout' in line[1]:
                        debit+=float(line[-3])
                    elif 'Closing' in line[1]:
                        closing=float(line[-1])
                except:
                    continue
    except:
        return []
    closing+=holding
    funds_added=round((credit-debit),2)
    final["credit"]=round(credit,2)
    final["debit"]=round(debit,2)
    final["total"]=round((closing-funds_added),2)
    return final
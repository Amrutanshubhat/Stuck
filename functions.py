import os
import csv

def total_csv(holding):
    data_file = os.path.join('./', 'ledger.csv')
    index=(0,1,2,3)
    credit=0
    debit=0
    closing=0
    final={"credit":0,"debit":0,"total":0}
    try:
        with open(data_file,'r') as file:
            for line in file:
                line=line.strip()
                line=line.split(',')[2:] 
                try:
                    if 'Opening Balance' in line[0]:
                        credit=float(line[4])
                    elif('Funds added using' in line[0]):
                        credit+=float(line[3])
                        #debit+=float(line[2])
                    elif 'Payout of' in line[0]:
                        debit+=float(line[2])
                    elif 'Closing Balance' in line[0]:
                        closing=float(line[4])
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
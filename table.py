from datascience import *
import numpy as np
import random as rd 
from datetime import datetime,timedelta,date


import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


Table = Table.read_table("Groceries_dataset.csv")


Table_Final = Table.drop("Member_number")

def add_expiration_date(date_f):    
    date_f = date_f.split("-")
    temp = rd.randint(4,14)
    date_before = date(int(date_f[2]),int(date_f[1]),int(date_f[0]))
    result_3 = date_before + timedelta(days=temp)
    return(result_3)  

def fix_format(date):
    date_final = date.split("-")
    date_final = str(date_final[2])+"-"+str(date_final[1])+"-"+str(date_final[0])
    return date_final


Table_Final_n = Table_Final.with_column("expiration date",Table_Final.apply(add_expiration_date,"Date"))
Table_Final_n = Table_Final_n.with_column("Date",Table_Final.apply(fix_format,"Date"))
print(Table_Final_n)

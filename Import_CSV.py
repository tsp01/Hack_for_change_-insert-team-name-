from datascience import *
import numpy as np
import random as rd 
from datetime import datetime,timedelta,date


import matplotlib.pyplot as plots
plots.style.use('fivethirtyeight')


items = Table.read_table("Groceries_dataset.csv").drop("Member_number")


def add_expiration_date(date_input):
    """
    Calculates the expiration date for each item, it randomly finds the number
    of days that it would take for your food to expire,
    Adds it to your actual date to give you the expiration date.

    """
    date_final = date_input.split("-")
    temp = rd.randint(4,14)
    date_before = date(int(date_final[2]),int(date_final[1]),int(date_final[0]))
    result = date_before + timedelta(days=temp)
    return(result)  # returns a str

def fix_format(date):

    '''
    fixes the format of the date to YYYY/MM/DD

    '''
    date_final = date.split("-")
    date_final = str(date_final[2])+"-"+str(date_final[1])+"-"+str(date_final[0])
    return date_final # returns a str


Data_Final = items.with_column("expiration date",items.apply(add_expiration_date,"Date"))
Data_Final = Data_Final.with_column("Date",items.apply(fix_format,"Date"))
print(Data_Final)
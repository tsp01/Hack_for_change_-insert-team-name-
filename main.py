"""
Authors: 
-Taranveer Purewal
-Mike Kabbabe
-Watkin Tang

Run This file as an executable to launch program
"""
# from datetime import datetime
# from threading import Timer
from grocery_tracker import Groceries

# x=datetime.today()
# y=x.replace(day=x.day+1, hour=0, minute=0, second=0, microsecond=0)
# delta_t=y-x

# secs=delta_t.seconds+1

def main():
    groceries = Groceries()
    groceries.check_expirations()
    

    # t = Timer(secs, groceries.check_expirations())
    # t.start()

if __name__ == '__main__':
    main()
    
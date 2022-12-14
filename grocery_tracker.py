"""
This file is for tracking groceries and expiration dates
"""
from datetime import date, datetime

PRODUCTS_FILE = "tracked_products.txt"

class Groceries:

    def __init__(self):
        self.foods = self.total_food_list()
        self.food_good = []
        self.food_expiring_soon = []
        self.food_expired = []
        self.date = date.today()

    def add_food(self, food, expiration="9999-99-99"):
        """
        writes to file in format:
            [Food_Name, Expiration_Date, Purchase_Date, Expiring_Soon, Expired]
            Expiring_Soon, Expired are represented as 1 or 0
        """
        
        with open(PRODUCTS_FILE, "a") as products:
            products.write(f"{food} {expiration} {self.date} 0 0 \n")

        self.foods = self.total_food_list()

    def remove_food(self, food):
        
        with open(PRODUCTS_FILE, "r") as f:
            lines = f.readlines()
        with open(PRODUCTS_FILE, "w") as f:
            for line in lines:
                if line.strip().split(" ")[0] != food: # Only writes to file if it's not what we inputted.
                    f.write(line)

        self.foods = self.total_food_list()

    # def notify(self, food, count):

    #     self.ui.display_notification(food, count)

    def check_expired(self):

        with open(PRODUCTS_FILE, "r") as f:
            lines = f.readlines()
        with open(PRODUCTS_FILE, "w") as f:
            for line in lines:
                if datetime.strptime(line.strip("\n").split(" ")[1], '%Y-%m-%d').date() > self.date:
                    f.write(line)
                else:
                    f.write(line[:-4] + "0 1\n")

        self.foods = self.total_food_list()
        
    def check_expiring_soon(self):

        with open(PRODUCTS_FILE, "r") as f:
            lines = f.readlines()
        with open(PRODUCTS_FILE, "w") as f:
            for line in lines:
                food_values = line.strip("\n").split(" ")
                expiration = datetime.strptime(food_values[1], '%Y-%m-%d').date()
                initial_date = datetime.strptime(food_values[2], '%Y-%m-%d').date()
                if  (expiration - initial_date).days > 2:
                    f.write(line)
                elif(expiration - initial_date).days <= 2:
                    f.write(line[:-4] + "1 0\n")

                    

        self.foods = self.total_food_list()

    def total_food_list(self):

        foods = []

        with open(PRODUCTS_FILE, "r") as products:
            for line in products:
                foods.append(line.strip().split(" "))

        return foods

    def sort_foods_list(self):

        
        self.check_expiring_soon()
        self.check_expired()
        self.food_good = []
        self.food_expiring_soon = []
        self.food_expired = []
        
        for item in self.foods:
            if int(item[3]) == int("1"):
                self.food_expiring_soon.append(item)
            elif int(item[4]) == 1:
                self.food_expired.append(item)
            else:
                self.food_good.append(item)

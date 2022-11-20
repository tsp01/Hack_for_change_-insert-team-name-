"""
This file is for tracking groceries and expiration dates
"""
from food import Food
from datetime import date, datetime

PRODUCTS_FILE = "tracked_products.txt"

class Groceries:

    def __init__(self):
        self.foods = self.total_food_list()
        self.food_good = []
        self.food_expiring_soon = []
        self.food_expired = []
        self.sort_foods_list()
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


    def remove_food(self, food, expiration):

        with open(PRODUCTS_FILE, "r") as f:
            lines = f.readlines()
        with open(PRODUCTS_FILE, "w") as f:
            for line in lines:
                if line.strip("\n").split(" ") != [food, expiration]:
                    f.write(line)

        self.foods = self.total_food_list()

    # def notify(self, food, count):

    #     self.ui.display_notification(food, count)

    def check_expired(self):

        with open(PRODUCTS_FILE, "r") as f:
            lines = f.readlines()
        with open(PRODUCTS_FILE, "w") as f:
            for line in lines:
                if datetime.strptime(line.strip("\n").split(" ")[1], '%Y-%m-%d') > self.date:
                    f.write(line)
                else:
                    f.write(line[:-1] + " 1")

        self.foods = self.total_food_list()
        
    def check_expiring_soon(self):

        with open(PRODUCTS_FILE, "r") as f:
            lines = f.readlines()
        with open(PRODUCTS_FILE, "w") as f:
            for line in lines:
                food_values = line.strip("\n").split(" ")
                expiration = datetime.strptime(food_values[1], '%Y-%m-%d')
                initial_date = datetime.strptime(food_values[2], '%Y-%m-%d')
                if  (expiration - self.date).days > round(0.25(expiration - initial_date)).days:
                    f.write(line)
                else:
                    f.write(line[:-3] + " 1 0")
                    

        self.foods = self.total_food_list()

    def total_food_list(self):

        foods = []

        with open(PRODUCTS_FILE, "r") as products:
            for line in products:
                foods.append(line.strip().split(" "))

        return foods

    def sort_foods_list(self):

        for item in self.foods:
            if item[3] == "1":
                self.food_expiring_soon.append(item)
            elif item[4] == "1":
                self.food_expired.append(item)
            else:
                self.food_good.append(item)

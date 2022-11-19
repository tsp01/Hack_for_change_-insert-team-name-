"""
This file is for tracking groceries and expiration dates
"""
from food import Food
from ui import Ui
from datetime import date
PRODUCTS_FILE = "tracked_products.txt"

class Groceries:

    def __init__(self):
        self.foods = self.food_list()
        self.ui = Ui(self.foods)
        self.date = date.today()

    def add_food(self, food, expiration=None):
        """
        writes to file in format:
            [Food_Name, Expiration_Date, Todays_Date, Expiring_Soon, Expired]
        """
        
        with open(PRODUCTS_FILE, "a") as products:
            products.write(food + " " + expiration + " " + self.date + " 0" + " 0" )

        self.foods = self.food_list()


    def remove_food(self, food, expiration):

        with open(PRODUCTS_FILE, "r") as f:
            lines = f.readlines()
        with open(PRODUCTS_FILE, "w") as f:
            for line in lines:
                if line.strip("\n").split(" ") != [food, expiration]:
                    f.write(line)

        self.foods = self.food_list()

    # def notify(self, food, count):

    #     self.ui.display_notification(food, count)

    def check_expired(self):

        pass

    def food_list(self):

        foods = []

        with open(PRODUCTS_FILE, "r") as products:
            for line in products:
                foods.append(line.strip().split(" "))

        return foods
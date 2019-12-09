
import sqlite3
import random

users_db = sqlite3.connect("database.db")
curs = users_db.cursor()
curs.execute("SELECT * FROM users_tb")
users = curs.fetchall()

def inv (u):  
    for a in users:
        if u == a[0]:
            inventory = [
                    {
                        "name": "diamant",
                        "price": random.randint(501, 1000),
                        "amount": a[3]
                    },
                    {
                        "name": "guld",
                        "price": random.randint(201, 500),
                        "amount": a[4]
                    },
                    {
                        "name": "järn",
                        "price": random.randint(101, 200),
                        "amount": a[5]
                    },
                    {
                        "name": "sten",
                        "price": random.randint(11, 100),
                        "amount": a[6]
                    },
                    {
                        "name": "trä",
                        "price": random.randint(1, 10),
                        "amount": a[7]
                    }
                ] 
    return inventory

def afford (user, item_to_buy, local_money, amount):
    for item in inv(user):
        if item_to_buy == item["name"]:
            if amount * item["price"] > local_money:
                print("Du har inte råd")
                return False
            else:
                return True


def buy(user, item_to_buy, local_money, amount):
    for item in inv(user):
        if item_to_buy == item["name"]:
            local_money = local_money - (amount * item["price"])
            item["amount"] = item["amount"] + amount
            print("Du har", local_money, "kronor kvar!")
    return local_money

def sell(user, item_to_sell, local_money):
    for item in inv(user):
        if item_to_sell == item["name"]:
            quantity = int(input("Hur många? "))
            if quantity > item["amount"]:
                print("Du har inte så många!")
            else:
                local_money = local_money + (quantity * item["price"])
                item["amount"] = item["amount"] - quantity
                print("Du har", local_money, "kronor!")
    return local_money

    #när inloggad så får en variabel ett värde som sedan gör att man vet
    #vilket inventory man ska ha // for a: x + 1 då kan man veta vilken användare
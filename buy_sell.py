import sqlite3
import random

users_db = sqlite3.connect("database.db")
curs = users_db.cursor()
curs.execute("SELECT * FROM users_tb")
users = curs.fetchall()

quit_buymenu = False
usern_taken = False
default_money = 1000.0

def buy(item_to_buy):
    local_money = user_money
    for item in invetory:
        if item_to_buy == item["name"]:
            quantity = int(input("Hur många? "))
            if quantity * item["price"] > local_money:
                print("Du har inte råd")
            else:
                local_money = local_money - (quantity * item["price"])
                item["amount"] = item["amount"] + quantity
                print("Du har", local_money, "kronor kvar!")
    return local_money

def sell(item_to_sell):
    local_money = user_money
    for item in invetory:
        if item_to_sell == item["name"]:
            quantity = int(input("Hur många? "))
            if quantity > item["amount"]:
                print("Du har inte så många!")
            else:
                local_money = local_money + (quantity * item["price"])
                item["amount"] = item["amount"] - quantity
                print("Du har", local_money, "kronor!")
    return local_money

print("Vill du: Logga in/Registrera ")
choice = input()

if choice == "Logga in".lower() or choice == "Logga in":
    username = input("Skriv ditt användar namn: ")
    for a in users:
        if username == a[0]:
            password = input("Skriv ditt lösenord: ")
            if password == a[1]:
                print("Du är nu inloggad!")

                invetory = [
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

                user_money = a[2]                

                print("Du har", user_money, "kronor!")
                print("Du har", a[3], "diamant,", a[4], "guld,", a[5], "järn,", a[6], "sten och", a[7], "trä.")
                print("Priser: Diamant", invetory[0]["price"],"kr,", "guld", invetory[1]["price"],"kr,", "järn", invetory[2]["price"],"kr,", "sten", invetory[3]["price"],"kr,", "trä", invetory[4]["price"],"kr.")
                
                buy_question = input("Vill du köpa, sälja eller avsluta? ")
                if buy_question == "Avsluta".lower() or buy_question == "Avsluta":
                   quit_buymenu = True

                while quit_buymenu == False:
                    if buy_question == "Köpa".lower() or buy_question == "Köpa":

                        buy_item = input("Vad vill du köpa? diamant, guld, järn, sten eller trä: ")
                        user_money = buy(buy_item)
                    elif buy_question == "Sälja".lower() or buy_question == "Sälja":
                        sell_item = input("Vad vill du sälja? diamant, guld, järn, sten eller trä: ")
                        user_money = sell(sell_item)
         
                    buy_question = input("Vill du köpa, sälja eller avsluta? ")
                    if buy_question == "Avsluta".lower() or buy_question == "Avsluta":
                        quit_buymenu = True
                curs.execute("UPDATE users_tb SET money = {}, diamond = {}, gold = {}, iron = {}, stone = {}, wood = {} WHERE user = '{}' ".format(user_money, invetory[0]["amount"], invetory[1]["amount"], invetory[2]["amount"], invetory[3]["amount"], invetory[4]["amount"], username))
            else:
                print("Fel lösenord")
        
elif choice == "Registrera".lower() or choice == "Registrera":
    new_user = input("Skriv in nytt användarnamn: ")
    for a in users:
        if new_user == a[0].lower():
            usern_taken = True
            print("Användarnamnet finns redan!")

    if usern_taken != True:
        newpass = input("Skriv in nytt lösenord: ")
        curs.execute("INSERT INTO users_tb (user, password, money, diamond, gold, iron, stone, wood) VALUES ('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(new_user, newpass, default_money, 0, 0, 0, 0, 0))

print ("hej")
users_db.commit()
users_db.close()   
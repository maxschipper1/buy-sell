import sqlite3
import random
import inventory

users_db = sqlite3.connect("database.db")
curs = users_db.cursor()
curs.execute("SELECT * FROM users_tb")
users = curs.fetchall()

quit_buymenu = False
usern_taken = False
default_money = 1000.0

print("Vill du: Logga in/Registrera ")
choice = input().lower()

if choice == "logga in":
    username = input("Skriv ditt användar namn: ")
    for a in users:
        if username == a[0]:
            password = input("Skriv ditt lösenord: ")
            if password == a[1]:
                print("Du är nu inloggad!")
                inventory.inv(a[0])    
                user_money = a[2]                

                print("Du har", user_money, "kronor!")
                print("Du har", a[3], "diamant,", a[4], "guld,", a[5], "järn,", a[6], "sten och", a[7], "trä.")
                print("Priser: Diamant", inventory.inv(a[0])[0]["price"],"kr,", "guld", inventory.inv(a[0])[1]["price"],"kr,", "järn", inventory.inv(a[0])[2]["price"],"kr,", "sten", inventory.inv(a[0])[3]["price"],"kr,", "trä", inventory.inv(a[0])[4]["price"],"kr.")
                
                buy_question = input("Vill du köpa, sälja eller avsluta? ")
                if buy_question == "Avsluta".lower() or buy_question == "Avsluta":
                   quit_buymenu = True

                while quit_buymenu == False:
                    if buy_question == "Köpa".lower() or buy_question == "Köpa":

                        buy_item = input("Vad vill du köpa? diamant, guld, järn, sten eller trä: ")
                        amount_to_buy = int(input("Antal?"))
                        if inventory.afford(a[0], buy_item, user_money, amount_to_buy) == True:
                            user_money = inventory.buy(a[0], buy_item, user_money, amount_to_buy)

                    elif buy_question == "Sälja".lower() or buy_question == "Sälja":
                        sell_item = input("Vad vill du sälja? diamant, guld, järn, sten eller trä: ")
                        user_money = inventory.sell(a[0], sell_item, user_money)
         
                    buy_question = input("Vill du köpa, sälja eller avsluta? ")
                    if buy_question == "Avsluta".lower() or buy_question == "Avsluta":
                        quit_buymenu = True
                curs.execute("UPDATE users_tb SET money = {}, diamond = {}, gold = {}, iron = {}, stone = {}, wood = {} WHERE user = '{}' ".format(user_money, inventory.inv(a[0])[0]["amount"], inventory.inv(a[0])[1]["amount"], inventory.inv(a[0])[2]["amount"], inventory.inv(a[0])[3]["amount"], inventory.inv(a[0])[4]["amount"], username))
            else:
                print("Fel lösenord")
        
elif choice == "registrera":
    new_user = input("Skriv in nytt användarnamn: ")
    for a in users:
        if new_user == a[0].lower():
            usern_taken = True
            print("Användarnamnet finns redan!")

    if usern_taken != True:
        newpass = input("Skriv in nytt lösenord: ")
        curs.execute("INSERT INTO users_tb (user, password, money, diamond, gold, iron, stone, wood) VALUES ('{}','{}', '{}', '{}', '{}', '{}', '{}', '{}')".format(new_user, newpass, default_money, 0, 0, 0, 0, 0))

users_db.commit()
users_db.close()   
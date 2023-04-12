import tkinter
import random
import numpy as np

main_window = tkinter.Tk()
main_window.title("Text based adventure game")
main_window.geometry("400x400")
# name = input("Enter your name >> ")
name = "Ivan"
# money = random.randint(50, 310)
money = 500
point = 0
health = 100

inventory = {"Weapons":[], "Keys":[], "Armours":[]}

top_frame = tkinter.Frame(main_window)
top_frame.pack(anchor = "n")

name_label = tkinter.Label(top_frame, text = "Name: "+name, font= ("Calibri, 16"))
name_label.grid(row=0, column=0)
health_label = tkinter.Label(top_frame, text = "Health: "+str(health), font= ("Calibri, 16"))
health_label.grid(row=1, column=0)
money_label = tkinter.Label(top_frame, text = "Money: "+str(money), font= ("Calibri, 16"))
money_label.grid(row=0, column=1)
point_label = tkinter.Label(top_frame, text = "Points: "+str(point), font= ("Calibri, 16"))
point_label.grid(row=1, column=1)

bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(anchor= "s")


# ---------------------------------------------------------------
# SHOP LISTS FOR REMOVAL    (´。＿。｀)
# ---------------------------------------------------------------


shop_weapon = []
with open("Shop.txt", "r") as dev_shop_update_weapon:
    lines = np.arange(1, 8, 1)
    i = 0
    for line in dev_shop_update_weapon:
        if i in lines:
            shop_weapon.append(line.strip())
        i += 1

#----------------------------

shop_keys = []
with open("Shop.txt", "r") as dev_shop_update_key:
    lines = np.arange(9, 11, 1)
    i = 0
    for line in dev_shop_update_key:
        if i in lines:
            shop_keys.append(line.strip())
        i += 1

#----------------------------

shop_heal = []
with open("Shop.txt", "r") as dev_shop_update_heal:
    lines = np.arange(12, 14, 1)
    i = 0
    for line in dev_shop_update_heal:
        if i in lines:
            shop_heal.append(line.strip())
        i += 1
    heal_left = int(shop_heal[1])

#----------------------------

shop_armour = []
with open("Shop.txt", "r") as dev_shop_update_armour:
    lines = np.arange(15, 18, 1)
    i = 0
    for line in dev_shop_update_armour:
        if i in lines:
            shop_armour.append(line.strip())
        i += 1


# ---------------------------------------------------------------
# DEF MAIN FUNCTIONS    \(￣︶￣*\))
# ---------------------------------------------------------------


def Room1(): # enter the room No1
    pass
#----------------------------
def Room2(): # enter the room No2
    pass
#----------------------------
def Room3(): # enter the room No3
    pass
#----------------------------
def Room4(): # enter the room No4
    pass
#----------------------------
def Shop(): # enter the shop
    global money, health
    global shop_weapon, shop_keys, shop_armour, shop_heal

    dev_shop = open("Shop.txt", "r")
    print("\n", dev_shop.readline())

    play_shop = True

    while play_shop:
        
        print("1) Weapons\n" +
            "2) Key\n" + 
            "3) HealingPad\n" + 
            "4) Armour\n" +
            "5) Continue the adventure")
        
        user_buy = int(input("\nChoose what you would like to buy, stranger\n>> "))
        print("\n")

        if user_buy == 1: # buy weapons
            print(*shop_weapon, sep="\n")
            user_weapon_choose = input("Which of them you liked the most?\n>> ")
            if user_weapon_choose == "1" or user_weapon_choose == "weapon1":
                if money >= 50:
                        money -= 50
                        change_labels(health, money, point)
                        add_item("knife,10,50", "w")
                        shop_weapon.remove("weapon1:knife,10,50")

                        print("Thanks for purchase")
                else:
                    print("Not enough cash")

            elif user_weapon_choose == "2" or user_weapon_choose == "weapon2":
                if money >= 150:
                    money -= 150
                    change_labels(health, money, point)
                    add_item("rifle,30,150", "w")
                    shop_weapon.remove("weapon2:rifle,30,150")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")

            elif user_weapon_choose == "3" or user_weapon_choose == "weapon3":
                if money >= 100:    
                    money -= 100
                    change_labels(health, money, point)
                    add_item("pistol,20,100", "w")
                    shop_weapon.remove("weapon3:pistol,20,100")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")
                
            elif user_weapon_choose == "4" or user_weapon_choose == "weapon4":
                if money >= 300:
                    money -= 300
                    change_labels(health, money, point)
                    add_item("bomb,50,300", "w")
                    shop_weapon.remove("weapon4:bomb,50,300")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")
                
            elif user_weapon_choose == "5" or user_weapon_choose == "weapon5":
                if money >= 250:    
                    money -= 250
                    change_labels(health, money, point)
                    add_item("sniper,40,250", "w")
                    shop_weapon.remove("weapon5:sniper,40,250")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")


            else: print("\nThere is no such an item\nLook wisely")


        elif user_buy == 2: # buy keys
            print(*shop_keys, sep="\n")
            user_key_choose = input("Would you like to buy this key? (y/n)\n>> ")

            if user_key_choose == "y":
                if money >= 300:
                    money -= 300
                    change_labels(health, money, point)
                    add_item("0,300", "k")
                    shop_keys.remove("key:0,300")
                    
                    print("Thanks for purchase")
                else:
                    print("Not enough cash")

            elif user_key_choose == "n":
                print("As you wish!\nBut still take a look on the other items")
            
            else:
                print("Did not understand you")
                    

        elif user_buy == 3: # HealingPad
            global heal_left
            
            if heal_left > 0:
                print(*shop_heal[0], sep="")
                print("HealingPads left: ", heal_left)
                user_heal_choose = input("\nWould you like to buy the HelingPad? (y/n)\n>> ")

                if user_heal_choose == "y":
                    if money >= 100:
                        money -= 100
                        health += 50
                        change_labels(health, money, point)
                        heal_left -= 1

                        print("Thanks for purchase")
                    else:
                        print("Not enough cash")

                elif user_heal_choose == "n":
                    print("Be careful then!")
                
                else: print("Didn't understand you")

            else: print("Sorry but you have bought all I had")
            

        elif user_buy == 4: # Armour
            print(*shop_armour, sep="\n")
            user_armour_choose = input("Which armour do you prefer?\n>> ")

            if user_armour_choose == "1": # choose armour 1
                if money >= 200:
                    money -= 200
                    change_labels(health, money, point)
                    add_item("2,200", "a")
                    shop_armour.remove("armour1:2,200")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")

            elif user_armour_choose == "2": # choose armour 2
                if money >= 400:
                    money -= 400
                    change_labels(health, money, point)
                    add_item("3,400", "a")
                    shop_armour.remove("armour2:3,400")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")
            
            else:
                print("I do not have the thing you are asking for")


        elif user_buy == 5: # exit shop
            print("Thanks for visiting the shop\n")
            play_shop = False
            

        else: print("\nDid not get what you have wanted, repeat please")

    
    pass
#----------------------------
def Inventory(): # show inventory
    global inventory

    for key in inventory.keys():
        print("\nList of ", key)
        for item in inventory[key]:
            print(item)

    pass
#----------------------------
def add_item(text,type): # add item to the inventory
    global inventory

    text_list = text.split(",")
    if type[0].lower() == "w": # add to weapons
        inventory["Weapons"].append({"name":text_list[0], "damage":int(text_list[1]), "price":int((text_list[2]))})

    elif type[0].lower() == "k": # add to keys
        inventory["Keys"].append({"code":text_list[0], "price":int(text_list[1])})

    elif type[0].lower() == "a": # add to armours
        inventory["Armours"].append({"Durability":int(text_list[0]), "price":int(text_list[1])})

    else:
        print("Adding the item <", text, "> into the invenory was unsuccessful")
#----------------------------
def change_labels(health, money, point): # change the values on the user window, whenever they happen  
    health_label.configure(text= "Health: "+str(health))
    money_label.configure(text= "Money: "+str(money))
    point_label.configure(text= "Points: "+str(point))


# ---------------------------------------------------------------
# BUTTONS    (‾◡◝)
# ---------------------------------------------------------------


R1_btn = tkinter.Button(bottom_frame, text= "Room 1", command= Room1)
R1_btn.grid(row=0, column=0)

R2_btn = tkinter.Button(bottom_frame, text= "Room 2", command= Room2)
R2_btn.grid(row=1, column=0)

R3_btn = tkinter.Button(bottom_frame, text= "Room 3", command= Room3)
R3_btn.grid(row=0, column=1)

R4_btn = tkinter.Button(bottom_frame, text= "Room 4", command= Room4)
R4_btn.grid(row=1, column=1)

Shp_btn = tkinter.Button(bottom_frame, text= "   Shop   ", command= Shop)
Shp_btn.grid(row=1, column=2)

Inv_btn = tkinter.Button(bottom_frame, text= "Inventory", command= Inventory)
Inv_btn.grid(row=0, column=2)



main_window.mainloop()

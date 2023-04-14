import tkinter
from tkinter import messagebox
import random
import numpy as np
import time


main_window = tkinter.Tk()
main_window.title("Text based adventure game")
main_window.geometry("400x400")
name = input("Enter your name >> ")
money = random.randint(50, 310)
point = 0
health = 100

# variables for checking if the chest is closed
opened_chest1 = False
opened_chest2 = False
opened_chest4 = False

# variables for checking if the enemy is alive
enemy_alive4 = True 
enemy_alive1 = True 
enemy_alive2 = True 
enemy_alive3 = True 

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
# TEXT LISTS    (´。＿。｀)
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

#----------------------------

room1 = open ("Room1.txt", "r").readlines()
enemy_info1 = room1[4].strip().split(",")

room2 = open("Room2.txt", "r").readlines() 
enemy_info2 = room2[4].strip().split(",")

room3 = open("Room3.txt", "r").readlines() 
enemy_info3 = room3[4].strip().split(",") 

room4 = open("Room4.txt", "r").readlines()
enemy_info4 = room4[4].strip().split(",")


# ---------------------------------------------------------------
# DEF MAIN FUNCTIONS    \(￣︶￣*\))
# ---------------------------------------------------------------


def Room1(): # enter the room No1
    global health, point, enemy_info1, enemy_alive1, opened_chest1

    r1 = open("Room1.txt", "r").readlines() 
    
    # figting enemy variables
    armour_dur = 1 # user's armour
    weapon_dmg = 0


    print("\n------------------------")
    print(r1[0], r1[1])
    
    if enemy_alive1:
        print(r1[3])
        print("\033[A\033[A")
        print(*enemy_info1, sep=",")
        print()
    else: print("There is no danger in these lands\n")

    play_room1 = True

    # ================
    # Main inner loop
    # ================

    while play_room1:
        print("1) Fight the enemy\n" +
            "2) Open chest\n" + 
            "3) Runaway")
        
        user_room_choose = input("\nChoose your action\n>> ")


        if user_room_choose == "1": # fight an enemy
            if enemy_alive1:
                if choose_equipment(r1, enemy_info1, weapon_dmg, armour_dur) == True:
                    enemy_alive1 = False
                
                else: play_room1 = False

            else: print("\nYou have already defeated the enemy in this room\n")
            

            pass              


        elif user_room_choose == "2": # open chest
            chest_code = r1[16]
            
            i = 0
            flag = True
            
            if opened_chest1 == False: # checks if the chest was already opened
                
                while flag == True:
                
                    if len(inventory["Keys"]) != 0:
                        for i in range(len(inventory["Keys"])): 
                            if inventory["Keys"][i]["code"] == int(chest_code[0]): # checks if user can open the chest
                                print("You have the key open the chest\n")
                                user_open_chest = input("Do you want to open a chest and obtain prize (y/n)\n>> ")
                                    
                                if user_open_chest == "y":
                                    del inventory["Keys"][i]
                                    point += int(chest_code[2])
                                    change_labels(health, money, point)
                                    opened_chest1 = True
                                    print("\nYou have successfully opened the chest\n") 
                                    print("\n+", chest_code[2], "points\n")
                                    flag = False                                       

                                elif user_open_chest == "n":
                                    print("")
                                    flag = False

                        
                            else: i += 1

                    

                    else: print("\nYou don't have a key to this chest\n")

            else: print("\nThe chest is already opened\n")


        elif user_room_choose == "3": # exit room
            print("\nYou have escaped successfully")
            play_room1 = False


    print("------------------------")


    pass
#----------------------------
def Room2(): # enter the room No2
    global health, point, enemy_info2, enemy_alive2, opened_chest2
    
    
    r2 = open("Room2.txt", "r").readlines() 
    
    # figting enemy variables
    armour_dur = 1 # user's armour
    weapon_dmg = 0

    print("\n------------------------")
    print(r2[0], r2[1])
    
    if enemy_alive2:
        print(r2[3])
        print("\033[A\033[A")
        print(*enemy_info2, sep=",")
        print()
    else: print("There is no danger in these lands\n")


    play_room2 = True

    # ================
    # Main inner loop
    # ================
    
    while play_room2:
        print("1) Fight the enemy\n" +
            "2) Open chest\n" + 
            "3) Runaway")
        
        user_room_choose = input("\nChoose your action\n>> ")


        if user_room_choose == "1": # fight an enemy
            if enemy_alive2:
                if choose_equipment(r2, enemy_info2, weapon_dmg, armour_dur) == True:
                    enemy_alive2 = False
            
                else: play_room2 = False

            else: print("\nYou have already defeated the enemy in this room\n")


            pass


        elif user_room_choose == "2": # open chest
            chest_code = r2[16]
            
            i = 0
            flag = True
            
            if opened_chest2 == False: # checks if the chest was already opened
                if len(inventory["Keys"]) != 0:
                    
                    while flag == True:
                    
                        for i in range(len(inventory["Keys"])): 
                            if inventory["Keys"][i]["code"] == int(chest_code[0]): # checks if user can open the chest
                                print("You have the key open the chest\n")
                                user_open_chest = input("Do you want to open a chest and obtain prize (y/n)\n>> ")
                                    
                                if user_open_chest == "y":
                                    del inventory["Keys"][i]
                                    point += int(chest_code[2])
                                    change_labels(health, money, point)
                                    opened_chest2 = True
                                    print("\nYou have successfully opened the chest\n")
                                    print("\n+", chest_code[2], "points\n")
                                    flag = False

                                elif user_open_chest == "n":
                                    print("")
                                    flag = False


                            else: i += 1

                        

                else: print("\nYou don't have a key to this chest\n") 
                    

            else: print("\nThe chest is already opened\n")


        elif user_room_choose == "3": # exit room
            print("\nYou have escaped successfully")
            play_room2 = False
    
    
    print("------------------------")


    pass
#----------------------------
def Room3(): # enter the room No3
    global health, point, enemy_info3, enemy_alive3 
    
    r3 = open("Room3.txt", "r").readlines() 
    
    healPad = int(r3[16])

    # figting enemy variables
    armour_dur = 1 # user's armour
    weapon_dmg = 0


    print("\n------------------------")
    print(r3[0], r3[1])

    if enemy_alive3:
        print(r3[3])
        print("\033[A\033[A")
        print(*enemy_info3, sep=",")
        print()
    else: print("There is no danger in these lands\n")

    play_room3 = True

    # ================
    # Main inner loop
    # ================

    while play_room3:
        print("1) Fight the enemy\n" +
            "2) Use HealingPad\n" + 
            "3) Runaway")
        
        user_room_choose = input("\nChoose your action\n>> ")


        if user_room_choose == "1": # fight an enemy
            if enemy_alive3:
                if choose_equipment(r3, enemy_info3, weapon_dmg, armour_dur) == True:
                    enemy_alive3 = False
                
                else: play_room3 = False
                
            else: print("\nYou have already defeated the enemy in this room\n")
    

        elif user_room_choose == "2": # use healingPad
            use_health = input("Do you waant to use HealthPad? (y/n)\n>> ")

            if use_health.lower() == "y":
                if healPad > 0:
                    if (health + 50) <= 100:
                        health += 50
                    else: health = 100
                    change_labels(health, money, point)
                    healPad -= 1
                    print("\nYou have gained +50 health\n")

                else: print("\nYou have already used the healthPad\n")

            elif use_health.lower() == "n":
                print("")

            else: print("\nWrong input\n") 


        elif user_room_choose == "3": # exit room
            print("\nYou have escaped successfully")
            play_room3 = False
    

    print("------------------------")


    pass
#----------------------------
def Room4(): # enter the room No4
    global health, point, enemy_info4, enemy_alive4, opened_chest4
    
    r4 = open("Room4.txt", "r").readlines() 
    
    healPad = int(r4[16])
    
    # figting enemy variables
    armour_dur = 1 # user's armour
    weapon_dmg = 0


    print("\n------------------------")
    print(r4[0], r4[1])
    
    if enemy_alive1:
        print(r4[3])
        print("\033[A\033[A")
        print(*enemy_info4, sep=",")
        print()
    else: print("There is no danger in these lands\n")

    play_room4 = True

    # ================
    # Main inner loop
    # ================

    while play_room4:
        print("1) Fight the enemy\n" +
            "2) Open chest\n" + 
            "3) Use HealingPad\n" +
            "4) Runaway")
        
        user_room_choose = input("\nChoose your action\n>> ")


        if user_room_choose == "1": # fight the enemy
            if enemy_alive4:
                if choose_equipment(r4, enemy_info1, weapon_dmg, armour_dur) == True:
                    enemy_alive4 = False
                
                else: play_room4 = False

            else: print("\nYou have already defeated the enemy in this room\n")

            
            pass


        elif user_room_choose == "2": # open chest
            chest_code = r4[19]
            
            i = 0
            flag = True
            
            if opened_chest4 == False: # checks if the chest was already opened
                if len(inventory["Keys"]) != 0:
                    
                    while flag == True:

                        for i in range(len(inventory["Keys"])): 
                            if inventory["Keys"][i]["code"] == int(chest_code[0]): # checks if user can open the chest
                                print("You have the key open the chest\n")
                                user_open_chest = input("Do you want to open a chest and obtain prize (y/n)\n>> ")
                                    
                                if user_open_chest == "y":
                                    del inventory["Keys"][i]
                                    point += int(chest_code[2])
                                    change_labels(health, money, point)
                                    opened_chest4 = True
                                    print("\nYou have successfully opened the chest\n")
                                    flag = False
                                                        
                                elif user_open_chest == "n":
                                    print("")
                                    flag = False

                            else: i += 1

                

                else: print("\nYou don't have a key to this chest\n")

            else: print("\nThe chest is already opened\n")


        elif user_room_choose == "3": # use healingPad
            use_health = input("Do you want to use HealthPad? (y/n)\n>> ")

            if use_health.lower() == "y":
                if healPad > 0:
                    if (health + 50) <= 100:
                        health += 50
                    else: health = 100
                    change_labels(health, money, point)
                    healPad -= 1
                    print("\nYou have gained +50 health\n")

                else: print("\nYou have already used the healthPad\n")

            elif use_health.lower() == "n":
                print("")

            else: print("\nWrong input\n") 


        elif user_room_choose == "4": # exit room
            print("\nYou have escaped successfully")
            play_room4 = False

    
    print("------------------------")

    
    pass
#----------------------------
def Shop(): # enter the shop
    global money, health, point, heal_left
    global shop_weapon, shop_keys, shop_armour, shop_heal

    dev_shop = open("Shop.txt", "r")
    print("\n", dev_shop.readline())

    play_shop = True

    while play_shop:
        
        print("1) Weapons\n" +
            "2) Key\n" + 
            "3) HealingPad\n" + 
            "4) Armour\n" +
            "5) Sell items\n" + 
            "6) Continue the adventure")
        

        
        user_buy = input("\nChoose what you would like to buy, stranger\n>> ")
        print()

        
        if user_buy == "1": # buy weapons
            print(*shop_weapon, sep="\n")
            user_weapon_choose = input("\nWhich of them you liked the most? <Enter a weapon number>\n>> ")
            
            try:
                if user_weapon_choose == "1" or user_weapon_choose == "weapon1":
                    if money >= 50:
                            money -= 50
                            change_labels(health, money, point)
                            add_item("knife,10,50", "w")
                            shop_weapon.remove("weapon1:knife,10,50")

                            print("\nThanks for purchase\n")
                    else:
                        print("\nNot enough cash\n")


                elif user_weapon_choose == "2" or user_weapon_choose == "weapon2":
                    if money >= 150:
                        money -= 150
                        change_labels(health, money, point)
                        add_item("rifle,30,150", "w")
                        shop_weapon.remove("weapon2:rifle,30,150")

                        print("\nThanks for purchase\n")
                    else:
                        print("\nNot enough cash\n")

            
                elif user_weapon_choose == "3" or user_weapon_choose == "weapon3":
                    if money >= 100:    
                        money -= 100
                        change_labels(health, money, point)
                        add_item("pistol,20,100", "w")
                        shop_weapon.remove("weapon3:pistol,20,100")

                        print("\nThanks for purchase\n")
                    else:
                        print("\nNot enough cash\n")

                    
                elif user_weapon_choose == "4" or user_weapon_choose == "weapon4":
                    if money >= 300:
                        money -= 300
                        change_labels(health, money, point)
                        add_item("bomb,50,300", "w")
                        shop_weapon.remove("weapon4:bomb,50,300")

                        print("\nThanks for purchase\n")
                    else:
                        print("\nNot enough cash\n")

        
                elif user_weapon_choose == "5" or user_weapon_choose == "weapon5":
                    if money >= 250:    
                        money -= 250
                        change_labels(health, money, point)
                        add_item("sniper,40,250", "w")
                        shop_weapon.remove("weapon5:sniper,40,250")

                        print("\nThanks for purchase\n")
                    else:
                        print("\nNot enough cash\n")

            except: print("\nThere's no such a weapon\n")


        elif user_buy == "2": # buy keys
            print(*shop_keys, sep="\n")
            user_key_choose = input("\nWould you like to buy this key? (y/n)\n>> ")

            if user_key_choose == "y":
                if money >= 300:
                    money -= 300
                    change_labels(health, money, point)
                    add_item("0,300", "k")
                    shop_keys.remove("key:0,300")
                    
                    print("\nThanks for purchase\n")
                else:
                    print("\nNot enough cash\n")

            elif user_key_choose == "n":
                print("\nAs you wish!\nBut still take a look on the other items\n")
            
            else:
                print("\nDid not understand you\n")
                    

        elif user_buy == "3": # HealingPad
            if heal_left > 0:
                print("\n", *shop_heal[0], sep="")
                print("HealingPads left: ", heal_left)
                user_heal_choose = input("\nWould you like to buy the HelingPad? (y/n)\n>> ")

                if user_heal_choose == "y":
                    if money >= 100:
                        money -= 100
                        if (health + 50) <= 100:
                            health += 50
                        else: 
                            health = 100
                        change_labels(health, money, point)
                        heal_left -= 1 

                        print("\nThanks for purchase\n")
                    else:
                        print("\nNot enough cash\n")

                elif user_heal_choose == "n":
                    print("\nBe careful then!\n")
                
                else: print("\nDidn't understand you\n")

            else: print("\nSorry but you have bought all I had\n")
            

        elif user_buy == "4": # Armour
            print(*shop_armour, sep="\n")
            user_armour_choose = input("\nWhich armour do you prefer?\n>> ")

            try:
                if user_armour_choose == "1": # choose armour 1
                    if money >= 200:
                        money -= 200
                        change_labels(health, money, point)
                        add_item("2,200", "a")
                        shop_armour.remove("armour1:2,200")

                        print("\nThanks for purchase\n")
                    else:
                        print("\nNot enough cash\n")
            
        
                elif user_armour_choose == "2": # choose armour 2
                    if money >= 400:
                        money -= 400
                        change_labels(health, money, point)
                        add_item("3,400", "a")
                        shop_armour.remove("armour2:3,400")

                        print("\nThanks for purchase\n")
                    else:
                        print("\nNot enough cash\n")
            
            except: print("\nThere's no such an armour\n")


        elif user_buy == "5": # sell items
            selling = True

            while selling:
                Inventory()
                user_sell = input("\nWhich items you want to sell, stranger?\nCommands: <weapons> | <keys> | <armours>| <nothing>\n>> ")

                if user_sell == "weapons": # sell weapons
                    user_sell_weapon = input("\nWhich of them are you ready to sell? <enter the name of the weapon>\n>> ")
                    
                    for idx, item in enumerate(inventory["Weapons"]): 
                        if item["name"] == user_sell_weapon.lower():
                            print("You have chosen to sell", item["name"], "for", item["price"], "? (y/n)")
                            user_confirm = input(">> ")
                            
                            if user_confirm == "y":
                                money += item["price"]
                                change_labels(health, money, point)
                                print("\nIt's a deal then\n", item["name"], "was removed from your inventory\n+", item["price"], "money\n")
                                del inventory["Weapons"][idx]

                            elif user_confirm == "n":
                                print("\nOkay, but don't argue if I won't buy it next time\n")

                            else: print("\nDid not understood you\n")

                        else: print("\nNah, don't see the thing you named in your backpack\n")
                                

                elif user_sell == "keys": # sell keys
                    user_sell_key = input("\nWhich key do you want to sell? <Enter key's place number>\n>> ")

                    for idx in range(len(inventory["Keys"])): 
                        if idx == int(user_sell_key) - 1:
                            print("You have chosen to sell", inventory["Keys"][idx], "for", inventory["Keys"][idx]["price"], "money? (y/n)")
                            user_confirm = input(">> ")
                            
                            if user_confirm == "y":
                                money += inventory["Keys"][idx]["price"]
                                change_labels(health, money, point)
                                print("\nIt's a deal then\n", inventory["Keys"][idx], "was removed from your inventory\n+", inventory["Keys"][idx]["price"], "money\n")
                                del inventory["Keys"][idx]

                            elif user_confirm == "n":
                                print("\nIf you are not selling go better open something with it then\n")

                            else: print("\nDid not understood you\n")

                        else: print("\nWhat? Repeat\n")

                elif user_sell == "armours": # sell armour
                    user_sell_armour = input("\nWhich armour do you want to sell? <Enter armour's place number>\n>> ")

                    for idx in range(len(inventory["Armours"])): 
                        if idx == int(user_sell_armour) - 1:
                            print("You have chosen to sell", inventory["Armours"][idx], "for", inventory["Armours"][idx]["price"], "money? (y/n)")
                            user_confirm = input(">> ")
                            
                            if user_confirm == "y":
                                money += inventory["Armours"][idx]["price"]
                                change_labels(health, money, point)
                                print("\nIt's a deal then\n", inventory["Armours"][idx], "was removed from your inventory\n+", inventory["Armours"][idx]["price"], "money\n")
                                del inventory["Armours"][idx]

                            elif user_confirm == "n":
                                print("\nHope you will need it more than me\n")

                            else: print("\nDid not understood you\n")

                        else: print("\nWhich one, again?\n")

                elif user_sell == "nothing":
                    print("\nYeah, better save everything for a rainy day, hehe\n")
                    selling = False
                    
                else: print("\nDid not understood you\n")


        elif user_buy == "6": # exit shop
            print("Thanks for visiting the shop\n")
            play_shop = False
        

        else: print("\nDid not get what you have wanted, repeat please\n")


    pass
#----------------------------
def Inventory(): # show inventory
    global inventory

    print("<-------------------------->")
    for key in inventory.keys():
        print("\nList of", key)
        for item in inventory[key]:
            print(item)
    print("\n<-------------------------->")


    pass
#----------------------------
def add_item(text,type): # add item to the inventory
    global inventory

    text_list = text.split(",")
    if type[0].lower() == "w": # add to weapons
        inventory["Weapons"].append({"name":text_list[0], "damage":int(text_list[1]), "price":int((text_list[2]))})

    elif type[0].lower() == "k": # add to keys
        inventory["Keys"].append({"code":int(text_list[0]), "price":int(text_list[1])})

    elif type[0].lower() == "a": # add to armours
        inventory["Armours"].append({"Durability":int(text_list[0]), "price":int(text_list[1])})

    else:
        print("Adding the item <", text, "> into the invenory was unsuccessful")
#----------------------------
def change_labels(health, money, point): # change the values on the user window, whenever they happen  
    health_label.configure(text= "Health: "+str(health))
    money_label.configure(text= "Money: "+str(money))
    point_label.configure(text= "Points: "+str(point))
#----------------------------
def battle(my_file, enemy, weapon, armour): # battle function
    global health, point, money
    
    enemy_hp = int(enemy[-1])
    enemy_dmg = int(enemy[1])

    animation_loading()
    print()

    while (enemy_hp > 0) or (health > 0):
        enemy_hp -= weapon
        
        if enemy_hp <= 0: # user has won
            print("\nYou have defeated the enemy\n")
            point += int(my_file[7])
            money += int(my_file[13])
            change_labels(health, money, point)
            add_item(my_file[10], "w")
            gained_weapon = my_file[10].strip().split(",")

            print("You feel how you getting stronger\nYour mother will be prowd of you\nOh, it seems he dropped something!\n")
            print("+", point, "points", "\n+", money, "money", "\nThe", gained_weapon[0], "was added to your inventory\n")
            return True
            break
        

        health -= (enemy_dmg//armour)

        if health <= 0: # user has lost
            print("\nYou lost the battle\n")
            health = 0
            point -= 2
            enemy[-1] = enemy_hp
            
            change_labels(health, money, point)

            print("You were kicked out from the city after humilating defeat\nYou have lost you pride and used equipment\nIt is better to go home and heal\n")
            print("-2 points\nyour hp is 0\n")
            return False
            break
#----------------------------          
def choose_equipment(my_file, enemy, weapon, armour): # choose weapon and armour for the battle
    the_weapon_exist = False # if the weapon was chosen right
    the_armour_exist = False # if the armour was chosen right
    
    # weapon choose
    print("\nChoose your weapon:\n")
    for items in range(len(inventory["Weapons"])):
        print(inventory["Weapons"][items])

    user_weapon = input("\nEnter the name of your weapon\n>> ")

    for idx, item in enumerate(inventory["Weapons"]): 
        if item["name"] == user_weapon:
            print("You have chosen ", item, " as a weapon\n")
            weapon = item["damage"]
            the_weapon_exist = True
            del inventory["Weapons"][idx]

    if the_weapon_exist == False: # checks for equiped weapon
        print("\nThere is no such a weapon\n")


    # armour choose
    user_use_armour = input("\nDo you want to use armour? (y/n)\n>> ")

    if user_use_armour == "y": 
        print("\nChoose your armour by its durability:\n")
        for items in range(len(inventory["Armours"])):
            print(inventory["Armours"][items])

            user_armour = int(input("\nEnter the durability of your armour\n>> "))
            for idx, item in enumerate(inventory["Armours"]):
                if item["Durability"] == user_armour:
                    print("You have chosen ", item, " as an armour\n")
                    armour = item["Durability"]
                    the_armour_exist = True
                    del inventory["Armours"][idx]

            if the_armour_exist == False: # checks for equiped armour
                print("\nThere is no such an armour\n")
        

    elif user_use_armour == "n": print("\nYou will fight without an armour\n")

    else: print("\nWrong input\n")


    if the_weapon_exist == False: # do not let the user fight without the weapon
        print("You CANNOT fight without a weapon\n")
    
    elif the_weapon_exist == True:
        if battle(my_file, enemy, weapon, armour) == True:
            return True
        else: return False
#----------------------------          
def animation_loading(): # loading animation
    animation = "|/-\\"
    idx = 0
    timer = 0
    anim_len = len(animation)
    while timer < 2:
        selected_anim = animation[idx % anim_len]
        print(selected_anim, end="\r")
        idx += 1
        time.sleep(0.1)
        timer += 0.10


# ---------------------------------------------------------------
# LOSE/WIN CHECKERS     (￣m￣）
# ---------------------------------------------------------------


if point >= 10:
    messagebox.showinfo("The result of the game", "You have won! ( •̀ ω •́ )y")

elif point < 0:
    messagebox.showinfo("The result of the game", "You have lost 〒▽〒")


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

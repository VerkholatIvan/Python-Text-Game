import tkinter
import random
import numpy as np

main_window = tkinter.Tk()
main_window.title("Text based adventure game")
main_window.geometry("400x400")
# name = input("Enter your name >> ")
name = "Ivan"
money = random.randint(50, 310)
point = 0
health = 100
inventory = {}

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


def change_labels(health, money, point):
    health_label.configure(text= "Health: "+str(health))
    money_label.configure(text= "Money: "+str(money))
    point_label.configure(text= "Points: "+str(point))



shop_weapon = []
with open("Shop.txt", "r") as dev_shop_update_weapon:
    lines = np.arange(1, 8, 1)
    i = 0
    for line in dev_shop_update_weapon:
        if i in lines:
            shop_weapon.append(line.strip())
        i += 1

shop_keys = []
with open("Shop.txt", "r") as dev_shop_update_key:
    lines = np.arange(9, 11, 1)
    i = 0
    for line in dev_shop_update_key:
        if i in lines:
            shop_keys.append(line.strip())
        i += 1



bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(anchor= "s")


def Room1():
    # my_file = open("Room1.txt", "r")
    pass
def Room2():
    pass
def Room3():
    pass
def Room4():
    pass
def Shop():
    global money
    global health
    global shop_weapon
    global shop_keys

    dev_shop = open("Shop.txt", "r")
    print("\n", dev_shop.readline())

    print("1) Weapons\n" +
          "2) Key\n" + 
          "3) HealingPad\n" + 
          "4) Armour\n" +
          "5) Continue the adventure")

    play_shop = True

    while play_shop:
        user_buy = int(input("\nChoose what you would like to buy, stranger\n>> "))
        print("\n")

        if user_buy == 1: # buy weapons
            print(*shop_weapon, sep="\n")
            print("6) back")
            user_weapon_choose = input("Which of them you liked the most?\n>> ")
            if user_weapon_choose == "1" or user_weapon_choose == "weapon1":
                if money >= 50:
                        money -= 50
                        change_labels(health, money, point)
                        inventory["knife"] = 10
                        shop_weapon.remove("weapon1:knife,10,50")

                        print("Thanks for purchase")
                else:
                    print("Not enough cash")

            elif user_weapon_choose == "2" or user_weapon_choose == "weapon2":
                if money >= 150:
                    money -= 150
                    change_labels(health, money, point)
                    inventory["rifle"] = 30
                    shop_weapon.remove("weapon2:rifle,30,150 ")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")

            elif user_weapon_choose == "3" or user_weapon_choose == "weapon3":
                if money >= 100:    
                    money -= 100
                    change_labels(health, money, point)
                    inventory["pistol"] = 20
                    shop_weapon.remove("weapon3:pistol,20,100")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")
                
            elif user_weapon_choose == "4" or user_weapon_choose == "weapon4":
                if money >= 300:
                    money -= 300
                    change_labels(health, money, point)
                    inventory["bomb"] = 50
                    shop_weapon.remove("weapon4:bomb,50,300")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")
                
            elif user_weapon_choose == "5" or user_weapon_choose == "weapon5":
                if money >= 250:    
                    money -= 250
                    change_labels(health, money, point)
                    inventory["sniper"] = 40
                    shop_weapon.remove("weapon5:sniper,40,250")

                    print("Thanks for purchase")
                else:
                    print("Not enough cash")

            # elif user_weapon_choose == "6" or user_weapon_choose == "back":


            else: print("\nThere is no such an item\nLook wisely")

        elif user_buy == 2: # buy keys
            print(*shop_keys, sep="\n")
            user_key_choose = input("Would you like to buy this key? (yes/no) or (1/0)\n>> ")

            if user_key_choose == "yes" or user_key_choose == "1":
                if money >= 300:
                    money -= 300
                    change_labels(health, money, point)
                    inventory["key"] = 0
                    shop_keys.remove("key:0,300")
                    
                    print("Thanks for purchase")
                else:
                    print("Not enough cash")
                    

        # elif user_buy == 3:

        # elif user_buy == 4:

        elif user_buy == 5:
            print("Thanks for visiting the shop\n")
            play_shop = False
            

        else: print("\nDid not get what you have wanted, repeat please")

    
    
    pass

def Inventory():
    if len(inventory) == 0:
        print("Your inventory has no items in it\nGo buy some stuff\n")
    else:
        for key, values in inventory.items():
            print(key, values)

    pass



R1_btn = tkinter.Button(bottom_frame, text= "Room 1", command= Room1)
R1_btn.grid(row=0, column=0)

R2_btn = tkinter.Button(bottom_frame, text= "Room 2", command= Room2)
R2_btn.grid(row=1, column=0)

R3_btn = tkinter.Button(bottom_frame, text= "Room 3", command= Room3)
R3_btn.grid(row=0, column=1)

R4_btn = tkinter.Button(bottom_frame, text= "Room 4", command= Room4)
R4_btn.grid(row=1, column=1)

Shp_btn = tkinter.Button(bottom_frame, text= "Shop", command= Shop)
Shp_btn.grid(row=1, column=2)

Inv_btn = tkinter.Button(bottom_frame, text= "Inventory", command= Inventory)
Inv_btn.grid(row=0, column=2)



main_window.mainloop()

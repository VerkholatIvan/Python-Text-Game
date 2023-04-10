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


# def change_labels(health, money, point):
#     health_label.configure(text= "Health: "+str(health))
#     money_label.configure(text= "Money: "+str(money))
#     point_label.configure(text= "Points: "+str(point))


bottom_frame = tkinter.Frame(main_window)
bottom_frame.pack(anchor= "s")


# def read_certain(f_line, s_line, step):
#     lines = np.arange(f_line, s_line, step)
#     i = 0





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

        if user_buy == 1:
            lines = np.arange(2, 8, 1)
            i = 0
            for line in dev_shop:
                if i in lines:
                    print(line.strip())
                i += 1

            user_weapon_choose = input("Which of them you liked the most?\n>> ")
            if user_weapon_choose == "1" or user_weapon_choose == "weapon1":
                money -= 50
                inventory["knife"] = 10

            elif user_weapon_choose == "2" or user_weapon_choose == "weapon2":
                money -= 150
                inventory["rifle"] = 30
            
            elif user_weapon_choose == "3" or user_weapon_choose == "weapon3":
                money -= 100
                inventory["pistol"] = 20
                
            elif user_weapon_choose == "4" or user_weapon_choose == "weapon4":
                money -= 300
                inventory["bomb"] = 50
                
            elif user_weapon_choose == "5" or user_weapon_choose == "weapon5":
                money -= 250
                inventory["sniper"] = 40

            else: print("\nThere is no such an item\nLook wisely")

        elif user_buy == 2:
            lines = np.arange(9, 11, 1)
            i = 0
            for line in dev_shop:
                if i in lines:
                    print(line.strip())
                i += 1

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

try: # did not work :/
    Shp_btn = tkinter.Button(bottom_frame, text= "Shop", command= Shop)
    Shp_btn.grid(row=1, column=2)
except:
    print("The Shop is already opened")

Inv_btn = tkinter.Button(bottom_frame, text= "Inventory", command= Inventory)
Inv_btn.grid(row=0, column=2)



main_window.mainloop()
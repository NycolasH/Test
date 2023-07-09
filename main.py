print("Hello, welcome to NetworkNick Coffee!")

name = input("What is your name?\n")

if name == "Nick" or name == "Marcus" or name == "Loki":

    evil_status = input("Are you evil?\n")
    good_deeds = int(input("How many acts of kindness have you done today?\n"))
    if evil_status == "Yes" or evil_status == "yes" and good_deeds < 4:
        print("You're not welcome here " + name + "! Get out!!!")
        exit()
    else:
        print("That's wonderful news, you'll recieve $1.00 off your purchase today as a thank you for not being evil.")

else:
    print("Hello " + name + ", thank you so much for coming in today.\n")


menu = "Black Coffee, Espresso, Latte, Cappuccino, Frappuccino"

print("What would you like from our menu today? Here is what we are serving.\n" + menu)

order = input ()

if order == "Frappuccino" or order == "frappuccino":
    price = 8
elif order == "Black Coffee" or order == "black coffee":
    price = 4
elif order == "Espresso" or order == "espresso":
    price = 5
elif order == "Latte" or order == "latte":
    price = 6
elif order == "Cappuccino" or order == "cappuccino":
    price = 7
else:
    print("Sorry we're only serving what's on our menu, could we get you something else?")

quantity = input("Excuse me " + name + ", how many " + order + "s would you like?\n")

total = price * int(quantity)

if name == "Sheli":
    total = price * int(quantity) - 1
else:
    total = price * int(quantity)

print("Wonderful, the total is $" + str(total) + " we'll have your " + quantity + " " + order + "s ready for you in a moment." )


print ("Thank you for the wait, I hope you have a wonderful day!")
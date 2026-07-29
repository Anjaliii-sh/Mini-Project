# cafe-management
print("Hello, Here's the menu")
print("MENU")
class Menu():
    def __init__(self, Item, Price) :
        self.Item = Item
        self.Price = Price
menu_list = [
    Menu("Chips",20),
    Menu("Kurkure",20),
    Menu("Pasta",80),
    Menu("Pizza",220),
    Menu("Burger",60),
    Menu("Momo",80)
]

for i in menu_list :
    print(f"{i.Item} : {i.Price}")


order = input("What would you like to order ? ")

amt = 0
order_present = False
for i in menu_list :
    if (order == i.Item) :
        order_present = True
        print("You ordered",i.Item,"and that will be Rs.",i.Price)
        amt+=i.Price

if (order_present == False) :
    print("Sorry, order not available")

Ask = input("Do you want anything else ? ")
if(Ask == "Yes") :

    order = input("What would you like to order ? ")
    for i in menu_list :
        if (order == i.Item) :
            print("You ordered",i.Item,"and that will be Rs.",i.Price)
            amt+= i.Price
            break
if(Ask == "No") :
    print("Okay")


print("Total amount is - ",amt)
print("Thank You,Have a nice day")

# cafe-management
print("Hello, Here's the menu")
print("Menu")

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
    print(f"{i.Item} : {i.Price}")      #f"..." it is an f-string (formatting string).it lets you insert insert variables directly inside a string using {}

order_list = []

order = input("What would you like to order ? ").strip().lower()

amt = 0
order_present = False
for i in menu_list :
    if (order == i.Item.strip().lower()) :
        order_list.append(i)
        order_present = True
        print("You ordered",i.Item,"and that will be Rs.",i.Price)
        amt+=i.Price

if (order_present == False) :
    print("Sorry, order not available")

Ask = input("Do you want anything else (Yes / No) ? ").strip().lower()
while(Ask == "Yes".strip().lower()) :
    next_order = input("What would you like to order (Your Order / Nothing Else) ? ").strip().lower()
    item_found = False
    for i in menu_list :
        if (next_order == i.Item.strip().lower()) :
            item_found = True
            order_list.append(i)
            print("You ordered",i.Item,"and that will be Rs.",i.Price)
            amt+= i.Price
            break
    if (next_order == "Nothing Else".strip().lower()) :
        break
    if (item_found == False ) :
        print("Sorry, Order currently unavailable")
         
    
if(Ask == "No".strip().lower()) :
    print("Okay")

print("                                                                      ") 
print("Total amount is - ",amt)




print("----------------------------------------------------------------------")
print("RECEIPT")
for i in order_list :
    print(f"{i.Item} : Rs. {i.Price}")
print("----------------------------------------------------------------------")


print("                                                                      ")
print("Thank You, Have a nice day")

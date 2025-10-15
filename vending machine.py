print()
print("Welcome to polytechnics vending machince !")
print()
print("Snacks     Price(Rs)    ID    Quantity left")
print("Snickers      45        41        4")
print("Slai o'lai    25        42        6")
print("Sando         18        43        3")
print("Kinder        18        44        2")
print("Kit-kat       45        45        5")
print(" Oreo         23        46        2")

print()

print("Beverages   Price(Rs)    ID   Quantity left")
print("Fuse Tea       50        31        3")
print("Coca-cola      55        32        5")
print("Water          22        33        6")
print("White Mirinda  42        34        2")
print("Pink Mirinda   42        35        7")
print("Sprite         55        36        2")

items = {
    41: {"name": "Snickers", "price": 45, "quantity": 4, "category": "Snacks"},
    42: {"name": "Slai o'lai", "price": 25, "quantity": 6, "category": "Snacks"},
    43: {"name": "Sando", "price": 18, "quantity": 3, "category": "Snacks"},
    44: {"name": "Kinder", "price": 18, "quantity": 2, "category": "Snacks"},
    45: {"name": "Kit-kat", "price": 45, "quantity": 5, "category": "Snacks"},
    46: {"name": "Oreo", "price": 23, "quantity": 2, "category": "Snacks"},
    31: {"name": "Fuse Tea", "price": 50, "quantity": 3, "category": "Beverages"},
    32: {"name": "Coca-cola", "price": 55, "quantity": 5, "category": "Beverages"},
    33: {"name": "Water", "price": 22, "quantity": 6, "category": "Beverages"},
    34: {"name": "White Mirinda", "price": 42, "quantity": 2, "category": "Beverages"},
    35: {"name": "Pink Mirinda", "price": 42, "quantity": 7, "category": "Beverages"},
    36: {"name": "Sprite", "price": 55, "quantity": 2, "category": "Beverages"},
}

while True :
    money=int(input("Enter your money in(RS) :"))
    if not 50 <= money <= 200 :
        print("Your money wasn't accepted !")
        print("Your change is",money)
    else:
        item_id = int(input("Enter the id of the item that you want ! :"))
        if item_id not in items :
            print("You have inserted a wrong id")
            print("Your refund is Rs",money)
        else :
            quantity=int(input("Enter the quantity that you want :"))
            confirm=int(input("Enter 1 to confirm purchase or enter 2 to exit"))
            item=items[item_id]
            price=item["price"] * quantity
            if confirm == 1 :
                if quantity > item["quantity"] :
                    price = item["price"] * quantity
                    print("There is not enough product available")
                    print("Your change is",money)
                elif price > money :
                    print("You haven't inserted enough money")
                    print("Your change is",money)
                else :
                    change = money - price
                    print("You have selected",quantity,item["name"])
                    print("Your change is",change)
            elif confirm == 2 :
                print("You have exited vending machine")
                print("Your change is RS",money)
            else :
                print("You have entered wrong command")
    

            

            





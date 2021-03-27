from product import *
from balance import *
from Database.database import *

database = Database()
product = Product(database)
balance = Balance(database)


while True:
    print("\n")
    print("* To add a product --> Enter 1")
    print("* To delete a product --> Enter 2")
    print("* To buy a product --> Enter 3")
    print("* To sell a product --> Enter 4")
    print("* To see all the products --> Enter 5")
    print("* To see balance --> Enter 6")
    print("* To exit --> Enter 0")
    print("\n")
    value = input("What you want to do? ")
    print("\n")

    
    if value == '0':
        break
    elif value == '1':
        product.addProduct(database)
    elif value == '2':
        product.deleteProduct(database)
    elif value == '3':
        product.buyProduct(balance, database)
    elif value == '4':
        product.sellProduct(balance, database)
    elif value == '5':
        product.showProducts()
    elif value == '6':
        balance.showBalance()
    else:
        print("Invalid choice, please choose carefully.....")

    print("\n")
    print("==================================================")
    

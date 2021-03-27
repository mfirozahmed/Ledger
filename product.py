from Database.commands import *

PRODUCT_NOT_FOUND = 0

class Product:

    def __init__(self, database):
        self.products = []

        allProducts = getProductSQL(database)
        for eachProduct in allProducts:

            product = {
                'name': eachProduct[1],
                'buyPrice': eachProduct[2],
                'sellPrice': eachProduct[3],
                'profit': eachProduct[4],
                'quantity': eachProduct[5],
                'status': eachProduct[6]
            }
            self.products.append(product)




    def getProduct(self, name):
        for eachProduct in self.products:
            if eachProduct['name'] == name:
                return eachProduct
        return PRODUCT_NOT_FOUND




    def addProduct(self, database):
        name = input("Name: ")

        product = self.getProduct(name)
        if product != PRODUCT_NOT_FOUND:
            print("Product Already Added.....")
            return

        buyPrice = int(input("Buy Price: "))
        sellPrice = int(input("Sell Price: "))
        quantity = int(input("Available quantity in inventory: "))
        profit = sellPrice - buyPrice
        status = 1

        product = {
            'name': name,
            'buyPrice': buyPrice,
            'sellPrice': sellPrice,
            'quantity': quantity,
            'profit': profit,
            'status': status
        }

        addProductSQL(product, database)
        self.products.append(product)
        print("\nProduct Added")




    def deleteProduct(self, database):
        name = input("Name: ")

        product = self.getProduct(name)
        if product == PRODUCT_NOT_FOUND:
            print("Product Not Found.....")
            return

        deleteProductSQL(product, database)
        self.products[:] = [i for i in self.products if i.get('name') != name]
        
        print("\nProduct Deleted")




    def buyProduct(self, balance, database):
        name = input("Name: ")
        buyQuantity = int(input("Quantity: "))

        product = self.getProduct(name)
        if product == PRODUCT_NOT_FOUND:
            print("Product Not Found.....")
            return

        cost = product['buyPrice'] * buyQuantity

        if cost <= balance.getBalance():
            product['quantity'] += buyQuantity
            buyProductSQL(product, database)

            balance.reduceBalance(cost, database)

            print("\nProduct Bought")
            return 
        
        print("\nNot Enough Balance!!!!!!")




    def sellProduct(self, balance, database):
        name = input("Name: ")

        product = self.getProduct(name)
        if product == PRODUCT_NOT_FOUND:
            print("Product Not Found.....")
            return

        inventoryQuantity = product['quantity']
        
        sellQuantity = int(input("Quantity (Available {}): ".format(inventoryQuantity)))

        if sellQuantity > inventoryQuantity:
            print("You can't sell more than you have!!!!!!!!")
            return

        product['quantity'] -= sellQuantity
        sellProductSQL(product, database)

        profit = product['profit'] * sellQuantity
        balance.addBalance(profit, database)
        

        print("\nProduct Sold")

#15 spaces


    def showProducts(self):
        print("Name               Quantity               Profit")
        for eachProduct in self.products:
            print(eachProduct['name'], end="")
            nameLength = len(eachProduct['name'])
            for i in range(22 - nameLength):
                print(" ", end="")
            print(eachProduct['quantity'], end="")
            quantityLength = len(str(eachProduct['quantity']))
            for i in range(22 - quantityLength):
                print(" ", end="")

            print(eachProduct['profit'])
        print()
        
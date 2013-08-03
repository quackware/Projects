from collections import defaultdict

class Inventory:
    def __init__(self):
        self.products = defaultdict(int)
        
    def addProduct(self, product):
        self.products[product.pid] = product
        
    def printProducts(self):
        for key in self.products:
            print(self.products[key])
            
    def printProductValues(self):
        for key in self.products:
            print(str(self.products[key].pid) + " " + str(self.products[key].getValue()) + "\n")
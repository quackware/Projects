
class Product:

    def __init__(self, pid, price, quantity):
        self.price = price
        self.pid = pid
        self.quantity = quantity
        
    def __str__(self):
        return "ID: " + self.pid + " price: " + self.price + " quantity: " + self.quantity
    
    def getValue(self):
        return int(self.price) * int(self.quantity)
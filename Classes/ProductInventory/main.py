import inventory
import product

def main():
    
    productInventory = inventory.Inventory()
    while 1:
        result = input("Enter command or Exit\n")
        if result == "Exit":
            break
        elif result.startswith("addp"):
            pid = result.split()[1]
            price = result.split()[2]
            quantity = result.split()[3]
            newProduct = product.Product(pid,price,quantity)
            productInventory.addProduct(newProduct)
        elif result.startswith("printproducts"):
            productInventory.printProducts() 
        elif result.startswith("printvalues"):
            productInventory.printProductValues()  
    

if __name__ == '__main__':
    main()
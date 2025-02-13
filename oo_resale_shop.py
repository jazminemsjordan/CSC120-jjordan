from computer import * 

class ResaleShop:
    '''no attributes other than inventory for the shop itself
    The resale shop handles the methods'''
    inventory:list = []

    def __init__(self, inv:list):
        self.inventory = inv

    def buy(self, desc:str, processor:str, hd_cap:int, ram:int, os:str, year:int, cost:int):
        # add computer to inventory
        computer: Computer = Computer(desc, processor, hd_cap, ram, os, year, cost) 
        self.inventory.append(computer)
        return self.inventory.index(computer)

    def sell(self, item_id:int):
        # remove computer from inventory
        if self.inventory[item_id] is not None:
            self.inventory.pop(item_id)
            print("Item", item_id, "sold!")
        else: 
            print("Item", item_id, "not found. Please select another item to sell.")
    
    def update_price(self, item_id:int, new_price:int):
        # manually change price not based on year
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id]
            computer.price = new_price
        else:
            print("Item", item_id, "not found. Please select another item to alter the price.")

    def refurbish(self, item_id:int, new_os = None):
        if self.inventory[item_id] is not None:
            computer = self.inventory[item_id]
            # scaled pricing based on year made
            if int(computer.year_made) < 2000:
                computer.price = 0 
            elif int(computer.year_made) < 2012:
                computer.price = 250 
            elif int(computer.year_made) < 2018:
                computer.price = 550 
            else:
                computer.price = 1000 
            # optionally update operating system
            if new_os is not None:
                computer.operating_system = new_os   
        else:
            print("Item", item_id, "not found. Please select another item to refurbish.")
    
    def print_inventory(self):
        print(self.inventory)

def main():
    #main function for testing
    inv = []
    resaleShop: ResaleShop = ResaleShop(inv)
    resaleShop.buy(
        "Mac Pro (Late 2013)",
        "3.5 GHc 6-Core Intel Xeon E5",
        1024, 
        64,
        "macOS Big Sur", 
        2013, 
        1500,
        )
    resaleShop.print_inventory()
    resaleShop.update_price(0, 9999)
    # I'm pretty sure there's probably a better way to pull computer attributes other than creating a new variable each time
    # but I don't know what it is so this works for testing functionality
    test_computer = resaleShop.inventory[0]
    print(test_computer.price)
    resaleShop.refurbish(0, "Windows 11")
    test_2_computer = resaleShop.inventory[0]
    print(test_2_computer.price)
    print(test_2_computer.operating_system)





    # What methods will you need?

if __name__ == "__main__": main()

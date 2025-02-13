class Computer:
    
    ''' All computer attributes and specs are stored here
    I chose to put all the methods in oo_resale_shop.py, because a computer cannot buy or sell itself '''

    description: str
    processor_type: str
    hard_drive_capacity: int
    memory: int
    operating_system: str
    year_made: int
    price: int

    def __init__(self, desc:str, processor:str, hd_cap:int, ram:int, os:str, year:int, cost:int):
        self.operating_system = os
        self.processor_type = processor 
        self.hard_drive_capacity = hd_cap
        self.memory = ram
        self.operating_system = os
        self.year_made = year
        self.price = cost


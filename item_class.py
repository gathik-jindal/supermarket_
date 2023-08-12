class item:
    def __init__(self, serial_num='', item_name='', price='', price_type='', discount=''):
        self.serial_num = serial_num
        self.item_name = item_name
        self.price = price
        self.price_type = price_type
        self.discount = discount

    def write_row(self, writer):
        
        writer.writerow({
            "Serial number": self.serial_num, 
            "Item name": self.item_name,
            "Price": self.price,
            "Price type": self.price_type,
            "Discount": self.discount
            })
        
    def get_details(self):

        self.serial_num = input("Enter serial number: ")
        while not self.serial_num.isalnum():
            print("Error: serial number should only contain numbers and letters!")
            self.serial_num = input("Enter serial number: ")

        self.item_name = input("Enter item name: ")
        while not self.item_name.isalnum():
            print("Error: item name should only contain numbers and letters!")
            self.item_name = input("Enter item name: ")

        self.price = input("Item price: ")
        while not self.price.isnumeric():
            print("Error: price should only contain numbers!")
            self.price = input("Item price: ")

        self.price_type = input("Price type (if by quantity type \"qty\", if by bunch \"bnch\"): ")
        while not (self.price_type == "bnch" or self.price_type == "qty"):
            print("Error: price type should be either \"bnch\" or \"qty\"!")
            self.price_type = input("Price type (if by quantity type \"qty\", if by bunch \"bnch\"): ")

        self.discount = input("Enter discount on price: ")
        while not self.discount.isnumeric():
            print("Error: discount should only contain numbers!")
            self.discount = input("Enter discount on price: ")
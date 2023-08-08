class item:
    def __init__(self, serial_num, item_name, price, price_type, discount):
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
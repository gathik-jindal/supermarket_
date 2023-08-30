HEADER = ["Serial number", "Item name", "Price", "Price type", "Discount"]

class item:
    def __init__(self, serial_num='', item_name='', price='', price_type='', discount=''):
        self.serial_num = serial_num
        self.item_name = item_name
        self.price = price
        self.price_type = price_type
        self.discount = discount

        self.update_dict()

    def update_dict(self):
        self.dict = {HEADER[0]: [self.serial_num],
                     HEADER[1]: [self.item_name],
                     HEADER[2]: [self.price],
                     HEADER[3]: [self.price_type],
                     HEADER[4]: [self.discount]}
    
    def get_real_dict(self):
        self.dict = {HEADER[0]: self.serial_num,
                     HEADER[1]: self.item_name,
                     HEADER[2]: self.price,
                     HEADER[3]: self.price_type,
                     HEADER[4]: self.discount}

    def get_details(self):

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

        self.update_dict()

    def serial_num_gen(self, df, file_does_not_exist):
        #write some useful generator code

        try:
            if not file_does_not_exist:
                self.serial_num = str(int(df.iloc[-1][0]) + 1)
            else:
                self.serial_num = "1"

            self.update_dict()

        except TypeError:
            print("File corrupt")
            quit()
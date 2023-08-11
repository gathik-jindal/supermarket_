import csv
from item_class import item

HEADER = ["Serial number", "Item name", "Price", "Price type", "Discount"]

# add item function

def add_item():
    serial_num = input("Enter serial number: ")
    item_name = input("Enter item name: ")
    price = input("Item price: ")
    price_type = input("Price type (if by quantity type \"qty\", if by bunch \"bnch\"): ")
    discount = input("Enter discount on price: ")

    if price == '':
        price = 0
    if price_type == '':
        price_type = "bnch"
    if discount == '':
        discount = 0

    item1 = item(serial_num, item_name, price, price_type, discount)

    fh.seek(0, 2)
    item1.write_row(writer)

def search_item():
    pass

def delete_item():
    pass


# Initialising file

file_does_not_exist = False
try:
    fh = open("item_Database.csv", "r", newline='')
except FileNotFoundError:
    fh = open("item_Database.csv", "w", newline='')
    file_does_not_exist = True
fh.close()

fh = open("item_Database.csv", "r+", newline='')
writer = csv.DictWriter(fh, fieldnames=HEADER)
reader = csv.DictReader(fh, fieldnames=HEADER)

if file_does_not_exist:
    writer.writeheader()

if __name__ == "__main__":
    add_item()
    fh.close()
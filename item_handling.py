import csv
from item_class import item

# add item function

def add_item():
    fh.seek(0, 2)
    serial_num = input("Enter serial number: ")
    item_name = input("Enter item name: ")
    price = input("Item price: ")
    price_type = input("Price type (if by quantity type \"qty\", if by bunch \"bnch\"): ")
    discount = input("Enter discount on price: ")

    if price_type == '':
        price_type = "bnch"
    if discount == '':
        discount = 0

    item1 = item(serial_num, item_name, price, price_type, discount)

    item1.write_row(writer)

# Initialising file

file_does_not_exist = False
try:
    fh = open("item_Database.csv", "r", newline='')
except FileNotFoundError:
    fh = open("item_Database.csv", "w", newline='')
    file_does_not_exist = True
fh.close()

fh = open("item_Database.csv", "r+", newline='')
writer = csv.DictWriter(fh, fieldnames=["Serial number", "Item name", "Price", "Price type", "Discount"])

if file_does_not_exist:
    writer.writeheader()

if __name__ == "__main__":
    add_item()
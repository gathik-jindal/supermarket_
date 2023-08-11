import csv
from item_class import item
import panda as pd

HEADER = ["Serial number", "Item name", "Price", "Price type", "Discount"]

# add item function

def add_item():

    with open("item_Database.csv", "r+", newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=HEADER)

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

        print("written row")

def search_item(serial_or_name="serial"):
    
    with open("item_Database.csv", "r", newline='') as fh:
        reader = csv.DictReader(fh, fieldnames=HEADER)

        pos = fh.tell()

        match serial_or_name:

            case "serial":
                find_serial = input("Enter serial number: ")

                for row in reader:
                    if row[HEADER[0]] == find_serial:
                        print(row)
                        break

            case "name":
                find_name = input("Enter name: ")

                for row in reader:
                    if row[HEADER[1]] == find_name:
                        print(row)
                        break

        print("completed search")

    return pos

def delete_item():
    
    pos = search_item()

    with open("item_Database.csv", "r+") as fh:
        writer = csv.DictWriter(fh, fieldnames=HEADER)

        fh.seek(pos)

        writer.writerow({
            "Serial number": None,
            "Item name": None,
            "Price": None,
            "Price type": None,
            "Discount": None
            })
        
        print("deletion complete")


# Initialising file

file_does_not_exist = False
try:
    fh = open("item_Database.csv", "r", newline='')
except FileNotFoundError:
    fh = open("item_Database.csv", "w", newline='')
    file_does_not_exist = True

writer = csv.DictWriter(fh, fieldnames=HEADER)
if file_does_not_exist:
    writer.writeheader()
fh.close()

if __name__ == "__main__":
    delete_item()
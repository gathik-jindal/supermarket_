import csv
from item_class import item

def add_items(writer, l):
    item_ = item(writer, l[0], l[1], l[2], l[3], l[4])
    
    item_.write_row()

fh = open("item_Database.csv", "a+")
writer = csv.DictWriter(fh, fieldnames=["Serial number", "Item name", "Price", "Price type", "Discount"])
writer.writeheader()

list_of_items = []

fh.close()
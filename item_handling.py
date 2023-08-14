import csv
from item_class import item
import pandas as pd

HEADER = ["Serial number", "Item name", "Price", "Price type", "Discount"]
CSV_FILE_NAME = "item_Database.csv"

def add_item():

    with open(CSV_FILE_NAME, "r+", newline='') as fh:
        writer = csv.DictWriter(fh, fieldnames=HEADER)

        item1 = item()

        df = pd.read_csv(CSV_FILE_NAME)
        item1.serial_num_gen(df)

        item1.get_details()

        fh.seek(0, 2)
        item1.write_row(writer)

        print("written row")

def search_item(serial_or_name="serial"):
    
    with open(CSV_FILE_NAME, "r", newline='') as fh:
        reader = csv.DictReader(fh, fieldnames=HEADER)

        pos = -2

        match serial_or_name:

            case "serial":
                find_serial = input("Enter serial number: ")

                for row in reader:
                    pos += 1
                    if row[HEADER[0]] == find_serial:
                        print(row)
                        break

            case "name":
                find_name = input("Enter name: ")

                for row in reader:
                    pos += 1
                    if row[HEADER[1]] == find_name:
                        print(row)
                        break

        print("completed search")

    return pos

def delete_item():
    
    pos = search_item()

    df = pd.read_csv(CSV_FILE_NAME)
    df = df.drop(pos)
    df.to_csv(CSV_FILE_NAME, index=False, header=HEADER)
        
    print("deletion complete")


# Initialising file

file_does_not_exist = False
try:
    fh = open(CSV_FILE_NAME, "r", newline='')
except FileNotFoundError:
    fh = open(CSV_FILE_NAME, "w", newline='')
    file_does_not_exist = True

writer = csv.DictWriter(fh, fieldnames=HEADER)
if file_does_not_exist:
    writer.writeheader()
fh.close()

if __name__ == "__main__":
    delete_item()
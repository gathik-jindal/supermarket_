import csv
from item_class import item
import pandas as pd

HEADER = ["Serial number", "Item name", "Price", "Price type", "Discount"]
CSV_FILE_NAME = "item_Database_test.csv"

def get_df():
    df = pd.read_csv(CSV_FILE_NAME)
    for x in range(len(HEADER)):
        df[HEADER[x]] = df[HEADER[x]].astype("string")

    return df

def add_item():

    df = get_df()

    item1 = item()
    item1.serial_num_gen(df, file_does_not_exist)
    item1.get_details()

    df_to_add = pd.DataFrame.from_dict(item1.dict)
    df = pd.concat([df, df_to_add], ignore_index=True)

    df.to_csv(CSV_FILE_NAME, index=False)

def search_item(serial_or_name="serial"):
    
    df = get_df()

    match serial_or_name:

        case "serial":
            print(df.loc[df[HEADER[0]] == input("Serial Number: ")])

        case "name":
            print(df.loc[df[HEADER[1]] == input("Item Name: ")])

    # return pos

def delete_item(serial_or_name="serial"):
    
    df = get_df()

    match serial_or_name:

        case "serial":
            ser = input("Serial number: ")
            print(df.loc[df[HEADER[0]] == ser])
            y_n = input("Are you sure you want to delete this item(Y/n): ")
            if y_n == "Y" or y_n == "y":
                df = df[df[HEADER[0]] != ser]

        case "name":
            name = input("Item name: ")
            print(df.loc[df[HEADER[1]] == name])
            y_n = input("Are you sure you want to delete this item(Y/n): ")
            if y_n == "Y" or y_n == "y":
                df = df[df[HEADER[1]] != name]

    df.to_csv(CSV_FILE_NAME)

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
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

def show_items():
    print(get_df())

def add_item():

    df = get_df()

    item1 = item()
    item1.serial_num_gen(df, file_does_not_exist)
    item1.get_details()

    df_to_add = pd.DataFrame.from_dict(item1.dict)
    df = pd.concat([df, df_to_add], ignore_index=True)

    df.to_csv(CSV_FILE_NAME, index=False)

def search_item(serial_or_name="serial", ser='', name=''):
    
    df = get_df()

    match serial_or_name:

        case "serial":
            if ser != '':
                df_temp = df.loc[df[HEADER[0]] == ser]

                if not df_temp.empty:
                    print(df_temp)
                else:
                    return 1 # could not find item
            
            else:
                df_temp = df.loc[df[HEADER[0]] == input("Serial Number: ")]

                if not df_temp.empty:
                    print(df_temp)
                else:
                    return 1 # could not find item

        case "name":
            if name != '':
                df_temp = df.loc[df[HEADER[1]] == name]
                
                if not df_temp.empty:
                    print(df_temp)
                else:
                    return 1 # could not find item
            
            else:
                df_temp = df.loc[df[HEADER[1]] == input("Item Name: ")]

                if not df_temp.empty:
                    print(df_temp)
                else:
                    return 1 # could not find item

def modify_item():
    ser_or_name = input("Get item with serial or name: ")
    while not (ser_or_name == "serial" or ser_or_name == "name"):
        ser_or_name = input("Get item with serial or name: ")

    match ser_or_name:

        case "serial":
            ser = input("Serial number: ")
            if search_item(serial_or_name="serial", ser=ser) == 1: # checking if item exists
                print("Item to modify does not exist")
                return 1 # item does not exist
            else:
                y_n = input("Are you sure you want to modify this item(Y/n): ")

                if y_n == "y" or y_n == "Y":
                    df = get_df()

                    index = df[df[HEADER[0]] == ser].index[0]

                    item1 = item()
                    item1.serial_num_gen(df, file_does_not_exist)
                    item1.get_details()
                    item1.get_real_dict()

                    print(index)

                    df.iloc[index] = item1.dict

                    df.to_csv(CSV_FILE_NAME, index=False)

                    print("Modification doen successfully")
                    return 0 # success!
                
        case "name":
            name = input("Item name: ")
            if search_item(serial_or_name="name", name=name) == 1: # checking if item exists
                print("Item to modify does not exist")
                return 1 # item does not exist
            else:
                y_n = input("Are you sure you want to modify this item(Y/n): ")

                if y_n == "y" or y_n == "Y":
                    df = get_df()

                    index = df[df[HEADER[1]] == name].index[0]

                    item1 = item()
                    item1.serial_num_gen(df, file_does_not_exist)
                    item1.get_details()
                    item1.get_real_dict()

                    print(index)

                    df.iloc[index] = item1.dict

                    df.to_csv(CSV_FILE_NAME, index=False)

                    print("Modification done successfully")
                    return 0 # success!


def delete_item(serial_or_name="serial"):
    
    df = get_df()

    match serial_or_name:

        case "serial":
            ser = input("Serial number: ")

            if search_item(serial_or_name=serial_or_name, ser=ser) == 1:
                return 1 # could not find item to delete
            
            else:
                y_n = input("Are you sure you want to delete this item(Y/n): ")
                if y_n == "Y" or y_n == "y":
                    df = df[df[HEADER[0]] != ser]

        case "name":
            name = input("Item name: ")

            if search_item(serial_or_name=serial_or_name, name=name) == 1:
                return 1 # could not find item to delete
            else:
                y_n = input("Are you sure you want to delete this item(Y/n): ")
                if y_n == "Y" or y_n == "y":
                    df = df[df[HEADER[1]] != name]

    df.to_csv(CSV_FILE_NAME, index=False)

    return 0

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
    modify_item()
import item_handling

print("Type -h for help")

help = """

show items - displays all the items

add item - adds a new item

search item - searches for an item using serial or name

delete item - deletes an item using serial number

quit - quits the program

"""

def main():
    command = input(">>")

    # possible outputs for command

    match command:
        
        case "-h":
            print(help)

            return 1 # restarts program
        
        case "show items":
            item_handling.show_items()

            return 1 # restart the program

        case "add item":
            item_handling.add_item()

            return 1 # restarts program

        case "search item":
            serial_or_name = input("Search by serial or name: ")
            while not (serial_or_name == "serial" or serial_or_name == "name"):
                print("Please enter a valid option")
                serial_or_name = input("Search by serial or name: ")
            if item_handling.search_item(serial_or_name) == 1:
                print("Item does not exist")

            return 1 # restarts program

        case "modify item":
            item_handling.modify_item()

            return 1 # restarts the program

        case "delete item":
            serial_or_name = input("Delete by serial or name: ")
            while not (serial_or_name == "serial" or serial_or_name == "name"):
                print("Please enter a valid option")
                serial_or_name = input("Delete by serial or name: ")
            if item_handling.delete_item(serial_or_name) == 1:
                print("Item to delete does not exist")

            return 1 # restarts program
        
        case "scan item":
            pass # do something

        case "quit":

            return 0 # quits program


if __name__ == "__main__":
    ret = 1
    while ret != 0:
        ret = main()
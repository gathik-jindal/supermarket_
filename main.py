import item_handling

print("Type -h for help")

help = """

add item - adds a new item

search item - searches for an item using serial or name

delete item - deletes an item using serial number

"""

def main():
    command = input(">>")

    # possible outputs for command

    match command:

        case "-h":
            print(help)

            return 1

        case "add item":
            item_handling.add_item()

            return 1

        case "search item":
            serial_or_name = input("Search by serial or name: ")
            while serial_or_name != "serial" or serial_or_name != "name":
                serial_or_name = input("Search by serial or name: ")
            item_handling.search_item(serial_or_name)

            return 1

        case "delete item":
            serial_or_name = input("Search by serial or name: ")
            while serial_or_name != "serial" or serial_or_name != "name":
                serial_or_name = input("Search by serial or name: ")
            item_handling.delete_item(serial_or_name)

            return 1

        case "quit":

            return 0


if __name__ == "__main__":
    ret = 1
    while ret != 0:
        ret = main()
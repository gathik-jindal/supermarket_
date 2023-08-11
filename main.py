import item_handling

print("Type -h for help")

help = """
//type some help
"""

def main():
    command = input(">>")

    # possible outputs for command

    match command:

        case "-h":
            print(help)

        case "add items":
            item_handling.add_item()


if __name__ == "__main__":
    main()

item_handling.fh.close()
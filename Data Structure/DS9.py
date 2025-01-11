def add_contact(contact_dict):
    name = input("Enter the conctact name:")
    phone = input("Enter the phone number:")
    contact_dict[name]=phone
    print(f"Contact {name} added successfully.")



def search_contact(contact_dict):
    name = input("Enter the contact name to search:")
    if name in contact_dict:
        print(f"Phone number for {name}:{contact_dict[name]}")
    else:
        print(f"Contact {name} not found.")


if __name__ = "__main__":

    contacts = {}

    while True:
        print("\nMenu:")
        print("1. Add a new conctact")
        print("2. Search for an existing contact")
        print("3. Exit")

        choice =input("Enter your choice(1/2/3):")

        if choice == "1":
            add_contact()
        elif choice == "2":
            search_contact()
        elif choice == "3":
            print("Exiting the program.")
            break
        else:
            print("Invalid choice, please select again.")
    

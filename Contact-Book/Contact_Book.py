contacts = {}

def add_contact():
    name = input("Enter the contact's name: ")
    phone = input("Enter the contact's phone number: ")
    email = input("Enter the contact's email address: ")
    address = input("Enter the contact's address: ")

    contacts[name] = {
        'phone': phone,
        'email': email,
        'address': address
    }
    print("Contact added successfully!")

def view_contacts(): 
    if not contacts:
        print("No contacts found.")
    else:
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['phone']}")

def search_contact():
    query = input("Enter the name or phone number to search: ")
    found = False

    for name, details in contacts.items():
        if query.lower() in name.lower() or query == details['phone']:
            print(f"Name: {name}, Phone: {details['phone']}, Email: {details['email']}, Address: {details['address']}")
            found = True

    if not found:
        print("No matching contact found.")

def update_contact():
    name = input("Enter the name of the contact to update: ")

    if name in contacts:
        print(f"Current details: Phone: {contacts[name]['phone']}, Email: {contacts[name]['email']}, Address: {contacts[name]['address']}")
        phone = input("Enter the new phone number (or press enter to keep current): ")
        email = input("Enter the new email address (or press enter to keep current): ")
        address = input("Enter the new address (or press enter to keep current): ")

        if phone:
            contacts[name]['phone'] = phone
        if email:
            contacts[name]['email'] = email
        if address:
            contacts[name]['address'] = address

        print("Contact updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the name of the contact to delete: ")

    if name in contacts:
        del contacts[name]
        print("Contact deleted successfully!")
    else:
        print("Contact not found.")

def main():
    while True:
        print("\nContact Management System")
        print("1. Add Contact")
        print("2. View Contact List")
        print("3. Search Contact")
        print("4. Update Contact")
        print("5. Delete Contact")
        print("6. Exit")

        choice = input("Choose an option: ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            update_contact()
        elif choice == '5':
            delete_contact()
        elif choice == '6':
            break
        else:
            print("Invalid choice, please try again.")

if __name__ == "__main__":
    main()

#Copyright &copy; 2024 by @Pavani-Manni | All Rights Reserved.


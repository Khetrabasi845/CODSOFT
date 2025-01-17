contacts = {}
def show_menu():
    print("\n--- Contact Management System ---")
    print("1. Add Contact")
    print("2. View Contact List")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")

def add_contact():
    name = input("Enter Name: ")
    phone = input("Enter Phone Number: ")
    email = input("Enter Email: ")
    address = input("Enter Address: ")
    contacts[name] = {"Phone": phone, "Email": email, "Address": address}
    print(f"Contact '{name}' added successfully!")

def view_contacts():
    if not contacts:
        print("No contacts available.")
    else:
        print("\n--- Contact List ---")
        for name, details in contacts.items():
            print(f"Name: {name}, Phone: {details['Phone']}")

def search_contact():
    search = input("Enter Name or Phone Number to search: ")
    found = False
    for name, details in contacts.items():
        if search.lower() in name.lower() or search == details["Phone"]:
            print(f"\n--- Contact Found ---")
            print(f"Name: {name}, Phone: {details['Phone']}, Email: {details['Email']}, Address: {details['Address']}")
            found = True
            break
    if not found:
        print("Contact not found.")

def update_contact():
    name = input("Enter the Name of the contact to update: ")
    if name in contacts:
        print("Leave fields empty if you do not want to change them.")
        phone = input(f"Enter new Phone Number (current: {contacts[name]['Phone']}): ") or contacts[name]["Phone"]
        email = input(f"Enter new Email (current: {contacts[name]['Email']}): ") or contacts[name]["Email"]
        address = input(f"Enter new Address (current: {contacts[name]['Address']}): ") or contacts[name]["Address"]
        contacts[name] = {"Phone": phone, "Email": email, "Address": address}
        print(f"Contact '{name}' updated successfully!")
    else:
        print("Contact not found.")

def delete_contact():
    name = input("Enter the Name of the contact to delete: ")
    if name in contacts:
        del contacts[name]
        print(f"Contact '{name}' deleted successfully!")
    else:
        print("Contact not found.")

# Main Program Loop
while True:
    show_menu()
    choice = input("\nEnter your choice (1-6): ")
    if choice == "1":
        add_contact()
    elif choice == "2":
        view_contacts()
    elif choice == "3":
        search_contact()
    elif choice == "4":
        update_contact()
    elif choice == "5":
        delete_contact()
    elif choice == "6":
        print("Exiting the Contact Management System. Goodbye!")
        break
    else:
        print("Invalid choice. Please try again.")
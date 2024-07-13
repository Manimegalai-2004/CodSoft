import pickle
import os

class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}, Phone: {self.phone}, Email: {self.email}, Address: {self.address}"

class ContactBook:
    def __init__(self, filename='contacts.pkl'):
        self.contacts = []
        self.filename = filename
        self.load_contacts()

    def add_contact(self, contact):
        self.contacts.append(contact)
        self.save_contacts()

    def view_contacts(self):
        for contact in self.contacts:
            print(contact)

    def search_contact(self, query):
        for contact in self.contacts:
            if query.lower() in contact.name.lower() or query in contact.phone:
                print(contact)

    def update_contact(self, name, new_contact):
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts[idx] = new_contact
                self.save_contacts()
                return
        print("Contact not found!")

    def delete_contact(self, name):
        for idx, contact in enumerate(self.contacts):
            if contact.name.lower() == name.lower():
                self.contacts.pop(idx)
                self.save_contacts()
                return
        print("Contact not found!")

    def save_contacts(self):
        with open(self.filename, 'wb') as file:
            pickle.dump(self.contacts, file)

    def load_contacts(self):
        if os.path.exists(self.filename):
            with open(self.filename, 'rb') as file:
                self.contacts = pickle.load(file)

def main():
    contact_book = ContactBook()

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
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            contact = Contact(name, phone, email, address)
            contact_book.add_contact(contact)
            print("Contact added successfully.")
        elif choice == '2':
            contact_book.view_contacts()
        elif choice == '3':
            query = input("Enter name or phone number to search: ")
            contact_book.search_contact(query)
        elif choice == '4':
            name = input("Enter the name of the contact to update: ")
            print("Enter new details:")
            new_name = input("Enter name: ")
            new_phone = input("Enter phone number: ")
            new_email = input("Enter email: ")
            new_address = input("Enter address: ")
            new_contact = Contact(new_name, new_phone, new_email, new_address)
            contact_book.update_contact(name, new_contact)
            print("Contact updated successfully.")
        elif choice == '5':
            name = input("Enter the name of the contact to delete: ")
            contact_book.delete_contact(name)
            print("Contact deleted successfully.")
        elif choice == '6':
            break
        else:
            print("Invalid choice! Please try again.")

if __name__ == "__main__":
    main()


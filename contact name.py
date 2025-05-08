class Contact:
    def __init__(self, name, phone, email, address):
        self.name = name
        self.phone = phone
        self.email = email
        self.address = address

    def __str__(self):
        return f"Name: {self.name}\nPhone: {self.phone}\nEmail: {self.email}\nAddress: {self.address}\n"

class ContactBook:
    def __init__(self):
        self.contacts = []

    def add_contact(self, contact):
        self.contacts.append(contact)
        print(f"Contact {contact.name} added.")

    def view_contact(self, name):
         for contact in self.contacts:
            if contact.name == name:
                print(contact)
                return
         print(f"Contact {name} not found.")

    def delete_contact(self, name):
        for contact in self.contacts:
            if contact.name == name:
                self.contacts.remove(contact)
                print(f"Contact {name} deleted.")
                return
        print(f"Contact {name} not found.")
    
    def view_all_contacts(self):
        if not self.contacts:
            print("No contacts found.")
            return
        for contact in self.contacts:
            print(contact)

def main():
    contact_book = ContactBook()

    while True:
        print("\nContact Book Menu:")
        print("1. View all the Contacts")
        print("2. Add the Contact")
        print("3. View Contacts")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice: ")

        if choice == '1':
            name = input("Enter name: ")
            phone = input("Enter phone number: ")
            email = input("Enter email: ")
            address = input("Enter address: ")
            new_contact = Contact(name, phone, email, address)
            contact_book.add_contact(new_contact)

        elif choice == '2':
            name = input("Enter name to view: ")
            contact_book.view_contact(name)

        elif choice == '3':
            contact_book.view_all_contacts()
        
        elif choice == '4':
            name = input("Enter name to delete: ")
            contact_book.delete_contact(name)

        elif choice == '5':
            print("Exiting Contact Book.")
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()

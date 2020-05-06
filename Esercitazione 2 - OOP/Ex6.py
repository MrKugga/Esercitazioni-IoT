import json
import os

class Contact:
    def __init__(self, person):
        self.name = person["name"]
        self.surname = person["surname"]
        self.email = person["email"]

    # alla fine non serve
    def update(name= None, surname= None, email= None):
        if name is not None: self.name = name
        if surname is not None: self.surname = surname
        if email is not None: self.email = email


class AddressBook:
    def __init__(self, filename= None):
        self.contacts = []
        if filename is None: filename = "files/contacts.json"
        try:
            with open(filename, "rb") as fp:
                dict = json.load(fp)
                for person in dict:
                    self.contacts.append(Contact(person))

        except:
            raise FileNotFoundError

    def show(self):
        for contact in self.contacts:
            print(f'Name: {contact.name}, Surname: {contact.surname}, email: {contact.email}')

    def findByName(self, name):
        print("I found the following results:")
        found = False
        for contact in self.contacts:
            if contact.name == name:
                print(f'Name: {contact.name}, Surname: {contact.surname}, email: {contact.email}')
                found = True
        if found == False:
            print("Contact not found!")

    def removeContact(self, name, surname= None):

        count = 0
        for contact, counter in zip(self.contacts, range(len(self.contacts))):
            if contact.name == name:
                count += 1
                index = counter

        if count == 1:
            self.contacts.pop(index)
            print("Contact deleted!")

        elif count > 1 and surname is not None:
            for contact, index in zip(self.contacts, range(len(self.contacts))):
                if contact.name == name and contact.surname == surname:
                    self.contacts.pop(index)
                    print("Contact deleted!")
                    break

        elif count > 1 and surname is None:
            print(f"Mutliple contact with name '{name}'. Please specify a surname with 'Name Surname'.")

        else:
            print("Non ho capito come sono finito qui")

    def addContact(self, name, surname, email):
        person = {
            "name": name,
            "surname": surname,
            "email": email
        }

        self.contacts.append(Contact(person))
        print("Contact added!")

if __name__ == "__main__":
    book = AddressBook()
    print("""Welcome to the application to manage your contacts!
Press 's' to show the list of contacts
Press 'n' to add a contact
Press 'f' to find a contact
Press 'd' to delete a contact
Press 'q' to quit""")
    while True:
        command = input("-> ").casefold()

        if command == 's':
            book.show()

        elif command == 'n':
            name = input("Name? -> ")
            surname = input("Surname? -> ")
            email = input("Email? -> ")

            book.addContact(name, surname, email)

        elif command == 'f':
            name = input("Name? -> ")

            book.findByName(name)

        elif command == 'd':
            person = input("Contact? -> ").split()

            if len(person) > 1:
                book.removeContact(person[0], person[1])
            else:
                book.removeContact(person[0])

        elif command == 'q':
            break

        else:
            print("Command not available!")

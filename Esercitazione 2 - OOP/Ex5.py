

class Contact:
    def __init__(self, name, surname, email= None):
        self.name = name
        self.surname = surname
        if email is not None:
            self.email = email
        else:
            email = f"{name}.{surname}@polito.it"

    def __str__(self):
        return f'Name: {self.name}, Surname: {self.surname}, Email: {self.email}'


class AddressBook:
    def __init__(self):
        self.contacts = []
        try:
            with open('files/contacts.txt', 'r') as fp:
                lines = fp.readlines()
                for line in lines:
                    words = line.split(',')
                    for word in range(0, len(words)):
                        words[word] = words[word].strip()
                    self.contacts.append(Contact(words[0], words[1], words[2]))

        except FileNotFoundError:
            self.contacts = []

    def create(self, contact):
        self.contacts.append(contact)

    def read(self):
        for contact in self.contacts:
            print(contact)

    def update(self):
        print("Quale contatto vuoi aggiornare? (digita il numero)\n")
        for contact, i in zip(self.contacts, range(0, len(self.contacts))):
            print(f'{i} - {contact}')

        while True:
            index = int(input('-> '))
            if index >= 0 and index < len(self.contacts):
                break
            else:
                print("Valore non valido, per favore inserisci un valore valido.")

        name = input('Qual è il nuovo nome? -> ')
        surname = input('Qual è il nuovo cognome? -> ')
        email = input('Qual è la nuova email? -> ')
        self.contacts[index].name = name
        self.contacts[index].surname = surname
        self.contacts[index].email = email
        print("Contatto aggiornato!")

    def delete(self):
        print("Quale contatto vuoi eliminare? (digita il numero, digita 'annulla' per annullare)\n")
        for contact, i in zip(self.contacts, range(0, len(self.contacts))):
            print(f'{i} - {contact}')

        while True:
            user_input = input('-> ')
            if user_input == "annulla":
                print('Annullato!')
                break
            try:
                index = int(user_input)
                if index >= 0 and index < len(self.contacts):
                    self.contacts.pop(index)
                    print('Eliminato!')
                    break
                else:
                    print("Valore non valido, per favore inserisci un valore valido.")
            except:
                print('Digita un numero, cretino.')



if __name__ == "__main__":
    print("Scegli un'opzione:\nc -> create\nr -> read\nu -> update\nd -> delete")

    pippo_franco = AddressBook()

    while True:
        user_input = input("-> ")
        if user_input == "c":
            name = input("Nome? ")
            surname = input("Cognome? ")
            email = input("Email? ")
            pippo_franco.contacts.append(Contact(name, surname, email))
            print('Contatto creato!')
        elif user_input == "r":
            pippo_franco.read()
        elif user_input == "u":
            pippo_franco.update()
        elif user_input == "d":
            pippo_franco.delete()
        elif user_input == "q":
            break
        else:
            print("Comando non riconosciuto!")

    print("Goodbye!")

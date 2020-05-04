import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value

class Deck:
    def __init__(self):
        suits = ("Cuori", "Diamanti", "Quadri", "Picche")
        values = ("A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K")
        self.cards = []
        self.howManyCards = 0
        for suit in suits:
            for value in values:
                card = Card(suit, value)
                self.cards.append(card)
                self.howManyCards += 1

        random.shuffle(self.cards)

    def deal(self):
        if self.howManyCards != 0:
            dealed = self.cards.pop(0)
            self.howManyCards -= 1
            return f'Hai pescato: {dealed.value} di {dealed.suit}'
        else:
            return ("Non ci sono più carte!")

    def shuffle(self):
        random.shuffle(self.cards)

if __name__ == "__main__":
    print("deck -> crea un mazzo\nshuffle -> mischia le carte\ndraw -> pesca una carta\nq -> esci")
    while True:

        user_input = input("Dai un comando -> ")

        if user_input == "deck":
            deck = Deck()
            print("Mazzo creato!")

        elif user_input == "shuffle":
            deck.shuffle()
            print("Mazzo mischiato")

        elif user_input == "draw":
            print(deck.deal())

        elif user_input == "q":
            break

        else:
            print("Comando non riconosciuto")

        print(deck.howManyCards)

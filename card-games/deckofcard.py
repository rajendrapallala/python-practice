import random

class Card:
    def __init__(self, suit, value):
        self.suit = suit
        self.value = value
    def show(self):
        print(f'{self.value} of {self.suit}')
    def __str__(self):
        return f'{self.value} of {self.suit}'

class Deck:
    def __init__(self):
        self.cards = []
    
    def build(self):
        for suit in ['Dimonds', 'Spades', 'Harts', 'Clubs']:
            for value in range(1,14):
                self.cards.append(Card(suit,value))
    
    def display_deck(self):
        for card in self.cards:
            print(card)
    
    def shuffle_deck(self):
        random.shuffle(self.cards)

    def draw_card(self):
        return self.cards.pop()

class Person:
    def __init__(self, name):
        self.name = name
        self.hand = []
    
    def draw(self, deck):
        self.hand.append(deck.draw_card())
    
    def show_hand(self):
        for card in self.hand:
            print(card)

d = Deck()
d.build()
#d.display_deck()
d.shuffle_deck()
#d.display_deck()
#c = d.draw_card()
#print(c)
#c.show()
p = Person("Raj")
for i in range(13):
    p.draw(d)
p.show_hand()

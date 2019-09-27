import random

suits=["spades","harts","dimonds","clubs"]
ranks=["one","two","three","four","five","six","seven","eight","nine","ten","jack","queen",\
"king","ace"]
values={"one":"1","two":"2","three":"3","four":"4","five":"5","six":"6","seven":"7",\
"eight":"8","nine":"9","ten":"10","jack":"10","queen":"10","king":"10","ace":"11"}

class Card():
    def __init__(self, suit, rank):
        self.suit=suit
        self.rank=rank
    def __str__(self):
        return self.suit+" "+self.rank

class Deck:
    def __init__(self):
        self.deck_of_cards=[]
        for suit in suits:
            for rank in ranks:
                c=Card(suit,rank)
                self.deck_of_cards.append(c)
    def __str__(self):
        complete_deck=""
        for card in self.deck_of_cards:
            complete_deck += "\n" + card.__str__()
        return complete_deck
    def shuffle(self):
        random.shuffle(self.deck_of_cards)

    def draw_13_cards(self):
        self.shuffle()
        for i in range(0,12):
            print(self.deck_of_cards.pop(i))
    def hit(self):
        self.shuffle()
        return self.deck_of_cards.pop()

if __name__=="__main__":
    d=Deck()
  #  print(d)
    print("========================================================")
    d.shuffle()
   # print(d)

    d.draw_13_cards()
    print(d.hit())
    print(*d.deck_of_cards)
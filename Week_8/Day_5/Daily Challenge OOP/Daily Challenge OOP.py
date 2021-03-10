import random

class Card():

    def __init__(self,suit,value):
        self.suit = suit
        self.value = value

    def show(self):
        print(f"{self.value} of {self.suit}")
    

class Deck():
    def __init__(self):
        self.cards = []
        self.build()
    
    def build(self):
        for suit in ["Spades","Clubs","Diamonds","Heart"]:
            for value in range(1,14):
                if value == 1:
                    self.cards.append(Card(suit,"A"))
                elif value == 10:
                    self.cards.append(Card(suit,"J"))
                elif value == 11:
                    self.cards.append(Card(suit,"Q"))
                elif value == 12:
                    self.cards.append(Card(suit,"K"))
                else:
                    self.cards.append(Card(suit,value))

    def show(self):
        for card in self.cards:
            card.show()

    def shuffle(self):
        for i in range(len(self.cards) -1, 0 , -1):
            r = random.randint(0,i)
            self.cards[i],self.cards[r] = self.cards[r],self.cards[i]

    def deal(self):
        lastCard = self.cards[len(self.cards)-1]
        self.cards.pop()
        return lastCard.show()

deck = Deck()
deck.shuffle()
deck.show()
print("-------deal--------")
deck.deal()
print("--------dealt-------")
deck.show()



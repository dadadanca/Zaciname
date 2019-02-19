class Card:
    suits = ["spades", "hearts", "diamonds", "clubs" ]
    values = [None, None, "2", "3", "4", "5", "6", "7", "8", "9", "10", "Jack", "Queen", "King", "Ace"]

    def __init__(self, v, s):
        self.value = v
        self.suit = s

    def __lt__(self, other):
        if self.value < other.value:
            return True
        if self.value == other.value:
            if self.suit < other.suit:
                return True
            else: return False
        else: return False

    def __gt__(self, other):
        return self.value > other.value or (self.value == other.value and self.suit > other.suit)

    def __repr__(self):
        return self.values[self.value] + " of " + self.suits[self.suit]


card1= Card(11,0)
card2= Card(3, 2)

print(card1)
print(card1<card2)

from random import shuffle

class Deck:
    def __init__(self):
        self.cards = []
        for i in range (2,15):
            for j in range (4):
                self.cards.append(Card(i,j))
        shuffle(self.cards)

    def remove_card(self):
        if len(self.cards)== 0:
            return None
        return self.cards.pop()

    def jsem_prazdny(self):
        return len(self.cards) < 2

deck = Deck()
for card in deck.cards:
    print(card)


class Player:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.card = None

class Game:
    def __init__(self):
        name1=input("Zadej jmeno prvniho hrace")
        name2=input("Zadej jmeno druheho hrace")
        self.p1 = Player(name1)
        self.p2 = Player(name2)
        self.deck = Deck()

    def wins (self, winner):
        w = "{} vyhral toto kolo".format(winner.name)
        print(w)

    def draw (self, p1n, p1c, p2n, p2c):
        d = "{} drew {} : {} drew {}".format(p1n, p1c, p2n, p2c)
        print(d)

    def winner (self, p1, p2):
        if p1.wins > p2.wins:
            return p1.name
        if p1.wins == p2.wins:
            return "remiza"
        if p1.wins < p2.wins:
            return p2.name

    def Play_Game(self):
        print("Valka zacina")
        while not self.deck.jsem_prazdny():
            response = input("Chcete pokracovat?")
            if response.upper() == "NE":
                break
            p1c = self.deck.remove_card()
            p2c = self.deck.remove_card()
            self.draw(self.p1.name, p1c, self.p2.name, p2c)
            if p1c < p2c:
                self.wins(self.p2)
                self.p2.wins += 1
            else:
                self.wins(self.p1)
                self.p1.wins += 1


        win = self.winner(self.p1, self.p2)
        print("Valka je u konce. {} je vitez".format(win))


game = Game()
game.Play_Game()







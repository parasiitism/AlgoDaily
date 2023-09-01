import random
from enum import Enum

"""
    In the 1st half of the below code, 
    we have implemented Deck with generics but restricted the type of T to Card. 
    We have also implemented Card as an abstract class, 
    since methods like value() don't make much sense without a specific game attached to them
"""


class Suit(Enum):
    DIAMOND = 0  # smallest in big two
    CLUBS = 1
    HEART = 2
    SPADE = 3


class Card(object):
    def __init__(self, suit, value, isAvailable=True):
        self.suit = suit
        self.value = value
        # self.isAvailable = isAvailable


class Hand(object):

    def __init__(self, cards):
        self.cards = cards

    def addCard(self, card):
        self.cards.append(card)

    def score(self):
        total = 0
        for card in self.cards:
            total += card.value
        return total


class Deck(object):
    def __init__(self):
        # suits = ["Clubs", "Diamonds", "Hearts", "Spades"]
        values = ["A", "2", "3", "4", "5", "6",
                  "7", "8", "9", "10", "J", "Q", "K"]

        cards = []
        for i in range(len(Suit)):
            for j in range(len(values)):
                card = Card(i, values[j])
                cards.append(card)
        self.cards = cards
        self.shuffled = []

    def shuffle(self):
        clone = []
        for card in self.cards:
            clone.append(Card(card.suit, card.value))

        for i in range(len(clone)):
            j = random.randint(i, len(clone)-1)
            clone[i], clone[j] = clone[j], clone[i]
        self.shuffled = clone
        return clone

    def getCardFromShuffle(self):
        if len(self.shuffled) == 0:
            raise Exception('please shuffle first')
        return self.shuffled.pop()


deck = Deck()
for c in deck.cards:
    print(c.suit, c.value)
print("-----")
deck.shuffle()
for c in deck.shuffled:
    print(c.suit, c.value)
print("-----")

"""
    Now based on the above base implementation of the Card, Hand, Deck,
    we can extend it to the blackjack game(21)
"""


class BlackJackHand(Hand):

    def __init__(self, cards):
        self.BLACKJACK = 21
        # python2.7
        super(BlackJackHand, self).__init__(cards)
        # python3
        # super().__init__(cards)

    def score(self):
        minOver = sys.maxsize
        maxUnder = -sys.maxsize
        for score in self.possibleScores(self.cards):
            if self.BLACKJACK < score < minOver:
                minOver = score
            elif maxUnder < score <= self.BLACKJACK:
                maxUnder = score
        if maxUnder == -sys.maxsize:
            return minOver
        return maxUnder

    def possibleScores(self, cards):
        """
            Score of the non-digit:
            ace = either 1 or 11, J = 10, Q = 10, K = 10

            idea: Combinations
        """
        res = []

        def dfs(cands, total):
            if len(cands) == 0:
                res.append(total)
                return
            card = cands[0]
            if card.value.isdigit():
                dfs(cands[1:], total + int(card.value))
            elif card.value in 'JQK':
                dfs(cands[1:], total + 10)
            elif card.value == 'A':
                dfs(cands[1:], total + 1)
                dfs(cands[1:], total + 11)
        dfs(cards, 0)
        return res

    def isBusted(self):
        return self.score() > self.BLACKJACK

    def isBlackJacke(self):
        return self.score() == self.BLACKJACK


bkh = BlackJackHand([])

cards = [
    Card(0, 'A'),
    Card(0, '1'),
    Card(0, '3'),
]
print(bkh.possibleScores(cards))

cards = [
    Card(0, 'A'),
    Card(0, '2'),
    Card(0, 'J'),
]
print(bkh.possibleScores(cards))

cards = [
    Card(0, 'A'),
    Card(0, '2'),
    Card(0, 'J'),
    Card(0, 'A'),
]
print(bkh.possibleScores(cards))

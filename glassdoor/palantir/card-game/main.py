import random
from enum import Enum

"""
    Given 52 cards to N players 
    
    When the game starts, every player has a deck of cards.
    1. In rvery round, every player can only take 1 card from the deck at the top.
    2. The one who has the biggest card will win and s/he will take all other 3 cards from other players.
    3. If tie? no tie
    4. The game ends when there is a player who lose all cards
"""


class Card:
    def __init__(self, suit, rank) -> None:
        self.suit = suit
        self.rank = rank

    def __str__(self):
        return f"{self.suit}.{self.rank}"


class Player:
    def __init__(self, name) -> None:
        self.name = name
        self.hand = []

    def getCard(self, card):
        self.hand.append(card)

    def drawCard(self):
        card = self.hand.pop()
        return card

    def hasCard(self):
        return len(self.hand) > 0

    def __str__(self):
        return f"{self.name}: {', '.join(str(card) for card in self.hand)}"


class CardGame:
    def __init__(self, N) -> None:
        self.N = N
        self.players = [Player(f"Player {i}") for i in range(N)]
        self.deck = []
        self.suits_mapping = {
            "spade": 0,
            "heart": 1,
            "club": 2,
            "diamond": 3
        }
        self.rank_mapping = {
            "2": 0,
            "3": 1,
            "4": 2,
            "5": 3,
            "6": 4,
            "7": 5,
            "8": 6,
            "9": 7,
            "10": 8,
            "jack": 9,
            "queen": 10,
            "king": 11,
            "ace": 12
        }

    def initialize_deck(self):
        suits = ["spade", "heart", "club", "diamond"]
        ranks = ["2", "3", "4", "5", "6", "7", "8",
                 "9", "10", "jack", "queen", "king", "ace"]
        deck = []
        for r in ranks:
            for s in suits:
                deck.append(Card(s, r))
        random.shuffle(deck)
        return deck

    def play_game(self):
        deck = self.initialize_deck()
        cards_to_distribute = self.N * (52 // self.N)
        while cards_to_distribute > 0:
            for p in self.players:
                p.getCard(deck.pop())
                cards_to_distribute -= 1

        while all(player.hasCard() for player in self.players):
            self.play_round()

        for player in self.players:
            if not player.hasCard():
                print(f"{player.name} lost")

    def play_round(self):
        cards_in_round = []
        for player in self.players:
            card = player.drawCard()
            cards_in_round.append((player, card))

        cards_in_round.sort(key=lambda c: (
            self.rank_mapping[c[1].rank], self.suits_mapping[c[1].suit]), reverse=True)

        winner, winner_card = cards_in_round[0]
        for player, card in cards_in_round:
            # add to the back of the playe's hand
            winner.hand.insert(0, card)
        # print(f"winner = {winner.name} who has {len(winner.hand)} cards")


game = CardGame(4)
game.play_game()

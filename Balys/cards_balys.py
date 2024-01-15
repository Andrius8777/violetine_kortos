import random

class Card:
    def __init__(self, rank, suit):
        self.rank = rank
        self.suit = suit
        self.sign = f"{suit} {rank}"
        self.weight = self._get_weight()

    def _get_weight(self):
        ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
        return ranks.get(self.rank, 0)

    def __eq__(self, other):
        return self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __gt__(self, other):
        return self.weight > other.weight

class Deck:
    def __init__(self):
        self.cards = self._generate_deck()

    def _generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        deck = [Card(rank, suit) for rank in ranks for suit in suits]
        return deck

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            print("Deck is empty!")

def play_war(deck):
    a_cards = deck.cards[:len(deck.cards)//2]
    b_cards = deck.cards[len(deck.cards)//2:]
    a_stash = []
    b_stash = []

    round_number = 1
    while a_cards and b_cards:
        a_card = a_cards.pop()
        b_card = b_cards.pop()

        if a_card == b_card:
            a_stash.extend([a_card] + a_cards[-3:])
            a_cards = a_cards[:-3]
            a_cards.append(a_stash.pop())

            b_stash.extend([b_card] + b_cards[-3:])
            b_cards = b_cards[:-3]
            b_cards.append(b_stash.pop())
        elif a_card > b_card:
            a_cards = [a_card, b_card] + a_stash + b_stash + a_cards
            a_stash = []
            b_stash = []
        elif b_card > a_card:
            b_cards = [b_card, a_card] + b_stash + a_stash + b_cards
            a_stash = []
            b_stash = []

        print(f"round {round_number}: a_cards: {len(a_cards)}, a_stash {len(a_stash)}, b_cards {len(b_cards)}, b_stash {len(b_stash)}")
        round_number += 1

def play_one_round(a_cards, b_cards, a_stash, b_stash):
    a_card = a_cards.pop()
    b_card = b_cards.pop()

    if a_card == b_card:
        a_stash.extend([a_card] + a_cards[-3:])
        a_cards = a_cards[:-3]
        a_cards.append(a_stash.pop())

        b_stash.extend([b_card] + b_cards[-3:])
        b_cards = b_cards[:-3]
        b_cards.append(b_stash.pop())
    elif a_card > b_card:
        a_cards = [a_card, b_card] + a_stash + b_stash + a_cards
        a_stash = []
        b_stash = []
    elif b_card > a_card:
        b_cards = [b_card, a_card] + b_stash + a_stash + b_cards
        a_stash = []
        b_stash = []

    return a_cards, b_cards, a_stash, b_stash

def main():
    deck = Deck()
    deck.shuffle()
    
    a_cards = deck.cards[:len(deck.cards)//2]
    b_cards = deck.cards[len(deck.cards)//2:]
    a_stash = []
    b_stash = []

    exit_flag = False

    while not exit_flag:
        print("""
            0 - exit
            1 - play round
            2 - play all game
              """)
        user_choice = input("Your choice: ")
        
        if user_choice == "0":
            exit_flag = True
        elif user_choice == "1":
            a_cards, b_cards, a_stash, b_stash = play_one_round(a_cards, b_cards, a_stash, b_stash)
            print(f"A cards:{len(a_cards)}, B cards:{len(b_cards)}")
        elif user_choice == "2":
            play_war(deck)
            exit_flag = True

if __name__ == "__main__":
    main()

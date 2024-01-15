# import random

# class Card:
#     def __init__(self, rank, suit):
#         self.rank = rank
#         self.suit = suit
#         self.sign = f"{suit} {rank}"
#         self.weight = self._get_weight()

#     def _get_weight(self):
#         ranks = {'2': 2, '3': 3, '4': 4, '5': 5, '6': 6, '7': 7, '8': 8, '9': 9, 'T': 10, 'J': 11, 'Q': 12, 'K': 13, 'A': 14}
#         return ranks.get(self.rank, 0)

# class Player:
#     def __init__(self, name):
#         self.name = name
#         self.hand = []

#     def take_card(self, card):
#         self.hand.append(card)

#     def show_hand(self):
#         return [card.sign for card in self.hand]

# class Deck:
#     def __init__(self):
#         self.cards = self._generate_deck()

#     def _generate_deck(self):
#         ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
#         suits = ['spades', 'clubs', 'hearts', 'diamonds']
#         return [Card(rank, suit) for rank in ranks for suit in suits]

#     def shuffle(self):
#         random.shuffle(self.cards)

#     def take_from_top(self):
#         if self.cards:
#             return self.cards.pop(0)
#         else:
#             print("Deck is empty!")

# # Vartotojo sąsaja
# def main():
#     deck = Deck()
#     deck.shuffle()

#     players = [Player(f"Player {i + 1}") for i in range(4)]

#     while True:
#         print("\n1 - Shuffle deck")
#         print("2 - Deal cards")
#         print("3 - Show hands")
#         print("0 - Exit")
#         choice = input("Enter your choice: ")

#         if choice == '1':
#             deck.shuffle()
#             print("Deck shuffled.")
#         elif choice == '2':
#             for player in players:
#                 card = deck.take_from_top()
#                 if card:
#                     player.take_card(card)
#                     print(f"{player.name} took {card.sign}")
#         elif choice == '3':
#             for player in players:
#                 print(f"{player.name}'s hand: {', '.join(player.show_hand())}")
#         elif choice == '0':
#             print("Exiting program. Goodbye!")
#             break
#         else:
#             print("Invalid choice. Please enter a valid option.")

# if __name__ == "__main__":
#     main()

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

class Player:
    def __init__(self, name):
        self.name = name
        self.hand = []

    def take_card(self, card):
        self.hand.append(card)

    def play_card(self):
        if self.hand:
            return self.hand.pop(0)
        else:
            print(f"{self.name}'s hand is empty.")
            return None

    def show_hand(self):
        return [card.sign for card in self.hand]

class Deck:
    def __init__(self):
        self.cards = self._generate_deck()

    def _generate_deck(self):
        ranks = ['2', '3', '4', '5', '6', '7', '8', '9', 'T', 'J', 'Q', 'K', 'A']
        suits = ['spades', 'clubs', 'hearts', 'diamonds']
        return [Card(rank, suit) for rank in ranks for suit in suits]

    def shuffle(self):
        random.shuffle(self.cards)

    def take_from_top(self):
        if self.cards:
            return self.cards.pop(0)
        else:
            print("Deck is empty!")

def compare_cards(cards):
    return max(cards, key=lambda x: x.weight)

def main():
    deck = Deck()
    deck.shuffle()

    players = [Player(f"Player {i + 1}") for i in range(4)]

    while True:
        print("\n1 - Shuffle deck")
        print("2 - Deal cards")
        print("3 - Show hands")
        print("4 - Play round")
        print("0 - Exit")
        choice = input("Enter your choice: ")

        if choice == '1':
            deck.shuffle()
            print("Deck shuffled.")
        elif choice == '2':
            for player in players:
                card = deck.take_from_top()
                if card:
                    player.take_card(card)
                    print(f"{player.name} took {card.sign}")
        elif choice == '3':
            for player in players:
                print(f"{player.name}'s hand: {', '.join(player.show_hand())}")
        elif choice == '4':
            round_cards = [player.play_card() for player in players]
            round_winner = compare_cards(round_cards)
            print(f"Round winner: {round_winner.sign}")
        elif choice == '0':
            print("Exiting program. Goodbye!")
            break
        else:
            print("Invalid choice. Please enter a valid option.")

if __name__ == "__main__":
    main()




# class Card:
#     def __init__(self) -> None:
#         pass

# class Deck:
#     cards = []

#     def __init__(self) -> None:
#         pass
    
# def play_war(deck):
#     a_cards = deck[:len(deck)/2]
#     b_cards = deck[len(deck)/2:]
#     a_stash = []
#     b_stash = []

# Kort kaladė
# Korta: objektas
# -- rank (2-9, T, J, Q, K, A)
# -- suit (spades, clubs, hearts, diamonds)
# -- sign (suit + rank)
# -- weight
# Kortų kaladė
# -- cards - sąrašas kortų
# -- shuffle
# -- take from top
# -- take from bottom
# -- take random
# mastom apie žaidimą

#startas
#BALIO PAKEITIMAI

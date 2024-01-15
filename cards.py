class Card:
    def __init__(self) -> None:
        pass

class Deck:
    cards = []

def play_war(deck):
    a_cards = deck[:len(deck)/2]
    b_cards = deck[len(deck)/2:]
    a_stash = []
    b_stash = []

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
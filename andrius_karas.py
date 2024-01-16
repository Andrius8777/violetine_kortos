import random

ranks = [2, 3, 4, 5, 6, 7, 8, 9, 10, 'Bartukas', 'Karalius', 'Tuzas', 'Karaliene']
suits = ['♠', '♡', '♢', '♣']

class Deck:
    def __init__(self):
        self.cards = []
        for suit in suits:
            for rank in ranks:
                self.cards.append((suit, rank))


    def shuffle(self):
        random.shuffle(self.cards)


    def half_split(self):
        return self.cards[:26], self.cards[26:]
    

class Hand:
    def __init__(self, cards):
        self.cards = cards


    def __str__(self):
        return str(len(self.cards))
    

    def add(self, added_cards):
        self.cards.extend(added_cards)


    def remove(self):
        return self.cards.pop()
    

class Player:
    def __init__(self, name, hand):
        self.name = name
        self.hand = hand


    def play_card(self):
        drawn_card = self.hand.remove()
        print(f"{self.name} ismete: {drawn_card}\n")
        return drawn_card
    

    def remove_war_cards(self):
        war_cards = self.hand.cards[-3:]
        self.hand.cards = self.hand.cards[:-3]
        return war_cards
    

    def still_has_cards(self):
        return len(self.hand.cards) != 0
    

def main():
    print("♠♡ KORTU ZAIDIMAS ♢♣\n")
    print("World War 4 - Ai Edition v.0.1\n")

    d = Deck()
    d.shuffle()
    part1, part2 = d.half_split()

    robot = Player("ChatGPT", Hand(part1))
    name = input("Iveskite savo varda: ")
    humanoyd = Player(name.capitalize(), Hand(part2))

    total_rounds = 0
    war_count = 0
    print(f'Zaidimas prasideda!\n')
    print(f'Karas tarp {name.capitalize()} ir ChatGPT\n')

    while humanoyd.still_has_cards() and robot.still_has_cards():
        total_rounds += 1
        table_cards = [robot.play_card(), humanoyd.play_card()]
        if table_cards[0][1] == table_cards[1][1]:
            war_count += 1
            table_cards.extend(humanoyd.remove_war_cards())
            table_cards.extend(robot.remove_war_cards())
            winner = humanoyd if ranks.index(table_cards[0][1]) > ranks.index(table_cards[1][1]) else robot
            winner.hand.add(table_cards)
        else:
            winner = humanoyd if ranks.index(table_cards[0][1]) > ranks.index(table_cards[1][1]) else robot
            winner.hand.add(table_cards)
    if len(humanoyd.hand.cards) > len(robot.hand.cards):
        print(f" ====== Sveikinu! ======= {humanoyd.name} tapo nugaletoju!!!\n")
    elif len(humanoyd.hand.cards) < len(robot.hand.cards):
        print(f"Prakeiktas {robot.name} laimejo kova!\n")
    else:
        print("Lygiosios!\n")
    print('STATISTIKA:\n')
    print(f'Karas tarp {name.capitalize()} ir ChatGPT ivyko {war_count} kartu!!')
    print(f'Metimu skaicius: {total_rounds}!')

if __name__ == "__main__":
    main()
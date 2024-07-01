# Poker.py

'''
Notes:
Create a poker bot that can respond to a given game depending on the current hand and the flop
Percent calculator
@ decorater as factorial for functions
'''
# probability Files: https://en.wikipedia.org/wiki/Poker_probability
# All starting Hands ranked: https://www.gamblingsites.org/poker/texas-holdem/starting-hand-rankings/

'''
4 Stages of Poker:
1. Pre-flop
There is a round of betting once all players have received their 2 hole cards. This round of betting is initiated by 2 mandatory bets called blinds put into the pot by the 2 players to the left of the dealer. There's no need to confuse yourself here, they're mandatory so there is an incentive (a pot to win) for people to play.
2. Flop
3 cards are then dealt face up. This is called the flop. Another round of betting proceeds, starting with the player on the left of the dealer. (The dealer is just a position)
3. Turn
1 more card is then dealt face up. This is called the turn. Again, there is another round of betting, starting with the player on the left of the dealer.
4. River
The 5th and last card is then dealt face up. This is called the river. There is one final round of betting before all cards are turned face up – the showdown.
-> Results: Winning the pot
'''
from math import comb as C
from random import randint
import Poker.Evaluation as Evaluation

face_values = {
    "J": "Jack", "Q": "Queen", "K": "King", "A": "Ace"
}

suits = {
    "H": "Hearts", "D": "Diamonds", "S": "Spades", "C": "Clubs"
}

dealt_cards = []
pre_flop_hand = []

def get_card(dealt_cards):
    print("Pick a Card")
    print('[2|3|4|5|6|7|8|9|10|J|Q|K|A]')
    while True:
        card = input(">").upper()
        if card in face_values or card in [str(n) for n in range(2, 11)]:
            while True:
                suit = get_suit()
                if suit in suits:
                    if (card, suit) not in dealt_cards:
                        dealt_cards.append((card, suit))
                        return face_values.get(card, card), suits[suit]
                    else:
                        print('Error: This card has already been picked. Pick another card.')
                else:
                    print('Error: Please pick a valid suit')
        else:
            print('Error: Please pick a valid card')
def get_suit():
    print('[Pick a Suit]')
    print('[H]earts | [D]iamonds | [S]pades | [C]lubs')
    while True:
        suit = input(">").upper()
        if suit in suits:
            return suit
        else:
            print('Please pick a valid suit')

def display_card(*args):
    print("---STATUS---")
    for i, (card, suit) in enumerate(args, start=1):
        print(f"Card: {card} of {suit}")


def prompt_use_pre_flop():
    if pre_flop_hand:
        print("Use Pre-Flop Hand?")
        while True:
            choice = input("[Y]es | [N]o >").strip().lower()
            if choice == "y":
                return choice == 'y'
            else:
                return False
    return False
def get_round():
    print("Select the index of the current round of the game:")
    print('''1. Pre-flop (CENTER[0])
2. Flop (CENTER[3])
3. Turn (CENTER[4]) 
4. River (CENTER[5])''')
    round_choice = input(">").strip().lower()
    if round_choice == '1':
        return Pre_Flop()
    elif round_choice == '2':
        return Flop()
    elif round_choice == '3':
        return Turn()
    elif round_choice == '4':
        return River()
    else:
        print("Invalid round choice. Please select again.")
        return get_round()


def Pre_Flop():
    global pre_flop_hand
    print("Pre-flop phase")
    if prompt_use_pre_flop():
        cards = pre_flop_hand
    else:
        cards = []
        for _ in range(2):
            card, suit = get_card(dealt_cards)
            cards.append((card, suit))
        pre_flop_hand = cards  # Save the pre-flop hand
    display_card(*cards)

    # Display the rank of the hand
    Evaluation.display_hand_rank(cards)
    return cards


def Flop():
    print("Flop phase")
    if not pre_flop_hand:
        print("Error: Pre-flop hand not set. Please complete the pre-flop phase first.")
        return None

    community_cards = []
    for _ in range(3):
        card, suit = get_card(dealt_cards)
        community_cards.append((card, suit))

    display_card(*pre_flop_hand, *community_cards)
    return community_cards


def Turn():
    print("Turn phase")
    if not pre_flop_hand:
        print("Error: Pre-flop hand not set. Please complete the pre-flop phase first.")
        return None

    community_cards = Flop()
    if community_cards is None:
        return None

    card, suit = get_card(dealt_cards)
    community_cards.append((card, suit))
    display_card(*pre_flop_hand, *community_cards)
    return community_cards


def River():
    print("River phase")
    if not pre_flop_hand:
        print("Error: Pre-flop hand not set. Please complete the pre-flop phase first.")
        return None

    community_cards = Turn()
    if community_cards is None:
        return None

    card, suit = get_card(dealt_cards)
    community_cards.append((card, suit))
    display_card(*pre_flop_hand, *community_cards)
    return community_cards

def main():
    while True:
        get_round()


if __name__ == '__main__':
    main()




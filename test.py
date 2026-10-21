import random
from helperfuncties import bet_placement

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]




def create_deck():
    deck = [(suit, rank) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

deck = create_deck()
print(deck)

def deal_cards(deck):
    hand_player = [deck.pop(0), deck.pop(0)]
    hand_dealer = [deck.pop(0), deck.pop(0)]
    return hand_player, hand_dealer

hand_player, hand_dealer = deal_cards(deck)


def calculate_hand_value(hand):
    totaal = 0
    aantal_azen = 0

    for kaart in hand:
        rank = kaart[1]
        if rank in ["J", "Q", "K"]:
            totaal += 10
        elif rank == "A":
            totaal += 11
            aantal_azen +=1
        else:
            totaal += int(rank)

    while totaal > 21 and aantal_azen > 0:
        totaal -= 10
        aantal_azen -= 1

    return totaal

def hand_as_string(hand):
    return ", ".join([f"{kaart[0]}{kaart[1]}" for kaart in hand])


def show_cards(hand_dealer, hand_player):
    print("")
    print(f"Je hand is {hand_as_string(hand_player)}")
    print(f"Dealer hand is {hand_as_string(hand_dealer)}")
    print(f"\nJe score is {calculate_hand_value(hand_player)}")





continue_playing = True
while continue_playing:
    show_cards(hand_dealer, hand_player)
    score_player = calculate_hand_value(hand_player)

    bet_amount, budget = bet_placement(budget)

    if calculate_hand_value(hand_player) == 21:
        budget = budget + (bet_amount * 1.5)
        print(f"Je hebt Blackjack! Je wint {bet_amount * 1.5:.2f}. Je budget is nu {budget:.2f}")
        continue_playing = False
        break

    if calculate_hand_value(hand_player) > 21:
        print("Bust! Je beurt is over.")
        continue_playing = False
        break

    choice = input("Kies hit of stand: ").capitalize()
    while choice not in ("Hit", "Stand"):
        choice = input("Ongeldige invoer. Kies hit of stand ").capitalize()
    if choice == "Hit":
        hand_player.append(deck.pop(0))
        show_cards(hand_dealer, hand_player)
    elif choice == ("Stand"):
        if calculate_hand_value(hand_dealer) <= 16:
            hand_dealer.append(deck.pop(0))
            print(f"Dealer trekt {hand_dealer[-1]}")
        elif calculate_hand_value(hand_dealer) > 17:
            print(f"Dealer hand: {hand_dealer}")
            print(f"Jouw totaal: {calculate_hand_value(hand_player)}")
            print(f"Dealer totaal: {calculate_hand_value(hand_dealer)}")



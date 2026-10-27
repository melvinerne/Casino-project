from rich import print
from rich.panel import Panel
import random
from helperfuncties import bet_placement

SUITS = ["♠", "♥", "♦", "♣"]
RANKS = ["A", "2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K"]

def play_blackjack(budget):
    print("\nLaten we blackjack spelen!\n")

    continue_playing = True
    while continue_playing == True:

        bet_amount, budget = bet_placement(budget)

        deck = create_deck()

        hand_player, hand_dealer = deal_cards(deck)

        show_cards(hand_dealer, hand_player, reveal=False)

        calculate_hand_value(hand_player)

        player_is_bust = False

        if calculate_hand_value(hand_player) == 21:
            budget = budget + (bet_amount * 1.5)
            show_cards(hand_dealer, hand_player, reveal=True)
            print(f"[bold green]Je hebt Blackjack! Je wint {bet_amount * 1.5:.2f}.[/bold green] Je budget is nu {budget:.2f}")
        else:
            while calculate_hand_value(hand_player) < 21:
                choice = input("Kies hit of stand: ").capitalize()

                while choice not in ("Hit", "Stand"):
                    choice = input("Ongeldige invoer. Kies hit of stand ").capitalize()

                if choice == "Hit":
                    draw_card = deck.pop(0)
                    hand_player.append(draw_card)
                    print(f"\nJe pakt {draw_card[0]}{draw_card[1]}")
                    show_cards(hand_dealer, hand_player, reveal=False)

                    if calculate_hand_value(hand_player) > 21:
                        show_cards(hand_dealer, hand_player, reveal=True)
                        print(f"[bold red]Bust![/bold red] Je bent over de 21. Je resterend budget is nu {budget:.2f}")
                        player_is_bust = True
                        break

                elif choice == ("Stand"):
                    break

            if not player_is_bust:
                print(f"{"-" * 20}")
                print("De dealer is aan de beurt")
                print(f"Dealer hand is: {hand_as_string(hand_dealer)}")

                while calculate_hand_value(hand_dealer) < 17:
                    card = deck.pop(0)
                    hand_dealer.append(card)
                    print(f"Dealer trekt {card[0]}{card[1]}")
                    print(f"Dealer hand is: {hand_as_string(hand_dealer)}")

        print(Panel.fit(f"Dealer eindstand: {calculate_hand_value(hand_dealer)}\n"
                        f"Jouw eindstand: {calculate_hand_value(hand_player)}",
                        title="Eindscore"))

        if calculate_hand_value(hand_dealer) > 21:
            budget = budget + (bet_amount * 2)
            print(f"[bold green]Dealer is bust! Je wint {bet_amount * 2:.2f}.[/bold green] Je budget is nu {budget:.2f}")
        elif not player_is_bust and calculate_hand_value(hand_player) > calculate_hand_value(hand_dealer):
            budget = budget + (bet_amount * 1.5)
            print(f"[bold green]Je wint {bet_amount * 1.5:.2f}![/bold green] Je budget is nu {budget:.2f}")
        elif not player_is_bust and calculate_hand_value(hand_player) == calculate_hand_value(hand_dealer):
            budget = budget + (bet_amount * 1)
            print(f"[bold yellow]Gelijkspel![/bold yellow] Je krijgt je inzet terug. Je budget is nu {budget:.2f}")
        elif not player_is_bust:
            print(f"[bold red]Dealer wint.[/bold red] Je verliest je inzet. Je budget is nu {budget:.2f}")

        keep_on_going = input("\nWil je nog een ronde spelen? (ja/nee): ").lower()
        if keep_on_going != "ja":
            continue_playing = False

    print(f"Bedankt voor het spelen. Je budget is {budget}\n")
    return budget



def create_deck():
    deck = [(suit, rank) for suit in SUITS for rank in RANKS]
    random.shuffle(deck)
    return deck

def deal_cards(deck):
    hand_player = [deck.pop(0),deck.pop(0)]
    hand_dealer = [deck.pop(0), deck.pop(0)]
    return hand_player, hand_dealer

def hand_as_string(hand):
    return ", ".join([f"{kaart[0]}{kaart[1]}" for kaart in hand])

def show_cards(hand_dealer, hand_player, reveal):
    print(f"Je hand is {hand_as_string(hand_player)}")

    if reveal:
        print(f"Dealer hand is {hand_as_string(hand_dealer)}, score: {calculate_hand_value(hand_dealer)}")
    else:
        eerste_kaart = f"{hand_dealer[0][0]}{hand_dealer[0][1]}"
        print(f"Dealer hand is {eerste_kaart}, ??")

    print(f"Je score is {calculate_hand_value(hand_player)}\n")

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







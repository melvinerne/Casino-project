import random

def play_roulette(budget, starting_budget):
    print("\nLaten we roulette spelen!\n")

    continue_playing = True
    while continue_playing == True:
        print(
            "Je kan kiezen uit de volgende opties:\n1: rood\n2: zwart\n3: even\n4: oneven\n5: specifiek nummer\n0: stop")

        choice = input("Kies waar je op wilt inzetten. Kies uit 0 t/m 5. ")
        if choice == "0":
            print("Tot de volgende keer.")
            break
        elif choice == "5":
            while specific_number_choice not in range(0, 37):
                specific_number_choice = int(input("Ongeldige invoer. Je kan kiezen uit 0 t/m 36. "))
            specific_number_choice = int(input("Kies je nummer. Je kan kiezen uit 0 t/m 36. "))
        while choice not in ("0", "1", "2", "3", "4", "5"):
            choice = input("Ongeldige invoer. Kies 0 t/m 5. ")

        bet_amount = float(input("Hoeveel wil je inzetten? "))

        while bet_amount <= 0 or bet_amount > budget:
            bet_amount = float(
                input("Je moet minimaal 1 inzetten. En niet hoger dan je budget. Hoeveel wil je inzetten? "))

        budget = budget - bet_amount
        print(f"Je hebt {bet_amount:.2f} ingezet. Je resterend budget is {budget:.2f}")

        spin = random.randint(0, 37)

        if spin % 2 == 0:
            odd_even = "even"
        else:
            odd_even = "odd"

        if spin <= 18 and odd_even == "even":
            color = "zwart"
        elif spin > 18 and odd_even == "even":
            color = "rood"
        elif spin <= 18 and odd_even == "odd":
            color = "rood"
        else:
            color = "zwart"

        if spin == 0:
            print(f"Je hebt {spin} gegooid. Helaas verlies je deze keer. Je resterend budget is nu {budget:.2f}")
        elif choice == "1" and color == "rood":
            budget = budget + (bet_amount * 2)
            print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
        elif choice == "2" and color == "zwart":
            budget = budget + (bet_amount * 2)
            print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
        elif choice == "3" and odd_even == "even":
            budget = budget + (bet_amount * 2)
            print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
        elif choice == "4" and odd_even == "odd":
            budget = budget + (bet_amount * 2)
            print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 2:.2f}. Je budget is nu {budget:.2f}")
        elif choice == "5" and spin == specific_number_choice:
            budget = budget + (bet_amount * 35)
            print(f"Je hebt {spin} {color} gegooid. Je wint {bet_amount * 35:.2f}. Je budget is nu {budget:.2f}")
        else:
            print(
                f"Je hebt {spin} {color} gegooid. Helaas, je verliest deze keer. Je resterend budget is nu {budget:.2f}")

        keep_on_playing = input("Wil je doorspelen? Kies ja of nee. ")
        if keep_on_playing == "ja":
            continue
        elif keep_on_playing == "nee":
           return budget


    return budget
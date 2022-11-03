import random

logo = '''
 _     _            _    _            _    
| |   | |          | |  (_)          | |   
| |__ | | __ _  ___| | ___  __ _  ___| | __
| '_ \| |/ _` |/ __| |/ / |/ _` |/ __| |/ /
| |_) | | (_| | (__|   <| | (_| | (__|   < 
|_.__/|_|\__,_|\___|_|\_\ |\__,_|\___|_|\_\\
                       _/ |                
                      |__/         
'''

cards = [2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10, 11]

while True:
    blackjack = input("Do you want to play? 'y' or 'n' ").lower()
    if blackjack == 'y':
        GAME = True
        break
    elif blackjack == 'n':
        print("Buy! Buy!")
        GAME = False
        break
    else:
        print("Unknown command.")


def card_distribution(count, score):
    random_card = []
    global cards
    for card in range(count):
        new = random.choice(cards)
        if new == 11 and score + new > 21:
            new = 1
        random_card.append(new)
    if len(random_card) == 1:
        return random_card[0]
    else:
        return random_card

def dealer_cards(player_score, dealer_score):
    global diller
    while dealer_score < 17:
        new = card_distribution(1, dealer_score)
        dealer_score += new
        diller.append(new)
    if dealer_score <= 21:
        print(f"Your score {player_score}.Dealer score {dealer_score}. You lose.")
    elif dealer_score >= player_score:
        print(f"Your score {player_score}.Dealer score {dealer_score}. Draw.")

while GAME:
    distribution = True
    player_score = 0
    diller_score = 0
    player = card_distribution(2, player_score)
    diller = card_distribution(2, diller_score)

    for x in player:
        if x == 11:
            if player[0] + player[1] > 21:
                x = 1
        player_score+=x

    for x in diller:
        if x == 11:
            if diller[0] + diller[1] > 21:
                x = 1
        diller_score+=x

    print(logo)
    print(f"Your cards: {player}. Score: {player_score}")
    print(f"Dealer's first card: {diller[0]}")


    while distribution:
        if player_score > 21 and diller_score > 21:
            print(f"Your score {player_score} and dealer score {diller_score}. Draw")
        elif player_score > 21:
            while diller_score < 17:
                new = card_distribution(1, diller_score)
                diller_score += new
                diller.append(new)
            if diller_score <= 21:
                print(f"Your score {player_score}. Dealer score {diller_score}. You lose.")
            elif diller_score > 21:
                print(f"Your score {player_score}. Dealer score {diller_score}. Draw.")
            distribution = False
        elif diller_score > 21:
            print(f"Dealer score {diller_score}. You win!")
            distribution = False
        elif player_score == 21 and diller_score == 21:
            print(f"Your score {player_score} and dealer score {diller_score}. Draw")
            distribution = False
        elif player_score == 21:
            while diller_score < 17:
                new = card_distribution(1, diller_score)
                diller_score += new
                diller.append(new)
            if player_score == diller_score:
                print(f"Your score {player_score}. Dealer score {diller_score}. Draw")
            else:
                print(f"Your score {player_score}. Dealer score {diller_score}. You win!")
            distribution = False
        elif diller_score == 21:
            print(f"Dealer score {diller_score}. You lose!")
            distribution = False
        else:
            more_cards = input("Do you want to take 1 more card? 'y' or 'n' ").lower()
            print("\n")
            if more_cards == "y":
                new = card_distribution(1, player_score)
                player_score += new
                player.append(new)
                print(f"New card {new}. Your score: {player_score}")
            elif more_cards == "n":
                while diller_score < 17:
                    new = card_distribution(1, diller_score)
                    if new == 11 and diller_score + new > 21:
                        new = 1
                    diller_score += new
                    diller.append(new)
                if diller_score < 21:
                    if player_score > diller_score:
                        print(f"Your score {player_score}.Dealer score {diller_score}. You win.")
                        distribution = False
                    elif diller_score > player_score:
                        print(f"Your score {player_score}.Dealer score {diller_score}. You lose.")
                        distribution = False
                    elif player_score == diller_score:
                        print(f"Your score {player_score}.Dealer score {diller_score}. Draw.")
                        distribution = False
            else:
                print("Unknown command.")
    print(f"Your cards {player}")
    print(f"Dealer cards {diller}")
    while True:
        play_again = input("Do you want to play again? 'y' or 'n' ").lower()
        if play_again == 'y':
            break
        elif play_again == 'n':
            print("Buy! Buy!")
            GAME = False
            break
        else:
            print("Unknown command")



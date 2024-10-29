import random

ranks = (1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, "Jack", "Queen", "King")
suits = ("Spades", "Clubs", "Diamonds", "Hearts")

deck = [(rank, suit) for rank in ranks for suit in suits]


def start_game():
    # First Index is the player's deck, second index is the player's won cards
    random.shuffle(deck)
    p1 = [deck[:26], []]
    p2 = [deck[26:52], []]

    # Optional referencial dialogue just for fun
    optional_dialogue = input("- Greetings professor Falken, shall we play a game? (Yes or No)")
    if optional_dialogue == "No":
        print("Goodbye")
        return

    optional_dialogue2 = int(input("- Great, you have two options \n 1) Global thermonuclear war \n 2) War (the card game) \n"))
    if optional_dialogue2 == 1:
        print("- How about a nice game of war (the card game) instead. You have no other choice.")
    else:
        print("- Lovely, let's play war (the card game).")

    input_required = int(input("- Do you wish to watch computers play (1) or play for yourself against a computer (2) or play against another player (3)")) - 1
    main_loop(p1, p2, input_required)


def main_loop(p1, p2, input_required):
    cards_on_table = []
    turn_amount = 0
    while (len(p1[0]) + len(p1[1])) > 0 and (len(p2[0]) + len(p2[1])) > 0:
        turn_amount += 1

        if input_required == 1 or input_required == 2: input("P1, Input anything to put down a card")
        p1Card = pop_with_renew(p1)

        if input_required == 2: input("P2, Input anything to put down a card")
        p2Card = pop_with_renew(p2)

        print("P1 has put down: " + str(p1Card) + " P2 has put down: " + str(p2Card))

        if ranks.index(p1Card[0]) > ranks.index(p2Card[0]):
            print("P1 wins the exchange !")
            p1[1] = p1[1] + [p1Card] + [p2Card] + cards_on_table
            cards_on_table = []

        elif ranks.index(p2Card[0]) > ranks.index(p1Card[0]):
            print("P2 wins the exchange !")
            p2[1] = p2[1] + [p1Card] + [p2Card] + cards_on_table
            cards_on_table = []

        else:
            print("WAR")
            cards_on_table += [p1Card] + [p2Card]
            print("Both players put down 3 face down cards")
            for i in range(0, 3):
                cards_on_table.append(pop_with_renew(p1))
                cards_on_table.append(pop_with_renew(p2))

        print("P1 currently has " + str(len(p1[0])) + " cards in his deck and " + str(len(p1[1])) + " cards in the won pile " + "For a total of: " + str(len(p1[1]) + len(p1[0])))
        print("P2 currently has " + str(len(p2[0])) + " cards in his deck and " + str(len(p2[1])) + " cards in the won pile " + "For a total of: " + str(len(p2[1]) + len(p2[0])))
        print("There are " + str(len(cards_on_table)) + " cards on the table")
        print("----------------------------------------------------")

    if (len(p1[0]) + len(p1[1])) == 0:
        print("P2 has won the game !")
    else:
        print("P1 has won the game !")

    print("The game took a total of " + str(turn_amount) + " turns !")


def renew_player_deck(player):
    print("Player Deck Renewed")
    player[0] = player[1]
    player[1] = []
    random.shuffle(player[0])


def pop_with_renew(player):
    if len(player[0]) == 0:
        renew_player_deck(player)

    if len(player[0]) > 0:
        return player[0].pop(0)


start_game()
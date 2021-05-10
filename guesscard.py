import random
import time  # delay show cards



# import numpy as np
# Antonis Papadakis

numbers = ["2", "3", "4", "5", "6", "7", "8", "9", "10", "J", "Q", "K", "A"]
shades = ["♠", "♥", "♦", "♣"]

deck = []  # create deck
cardgame = []  # 21 random cards from deck

gcol1 = []  # each column for the game
gcol2 = []
gcol3 = []

listprintcards = [
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""],
    ["", "", ""]
]


def createdeck():  # create deck
    for shade in shades:
        for num in numbers:
            deck.append(num + shade)


def pickrandomcards():  # add unique cards until we got 21 uniques cards
    random.seed()
    while True:
        rnd = random.choice(deck)
        if rnd not in cardgame:
            cardgame.append(rnd)
        if len(cardgame) == 21:
            break


def add_in_2d_cards():  # add the 21 cards in 2d list
    count = 0  # count until 21, 7*3 loops = 21 cards
    for x in range(7):
        for y in range(3):
            listprintcards[x][y] = cardgame[count]
            count += 1


def add_col_to_2d():  # shuffle the cards when choose card
    count1 = 0
    count2 = -1
    count3 = -1
    count4 = 0
    for x in range(7):  # add the columns to 2d from the printing
        for y in range(3):  # totally 21 times count
            if count1 < 7:  # add first all the cards from the first list
                listprintcards[x][y] = gcol1[count1]
                count1 += 1
                if count1 == 6:  # activate the second if
                    count2 += 1
            elif -1 < count2 < 7:  # after all from the second
                listprintcards[x][y] = gcol2[count2]
                count2 += 1
                if count2 == 6:  # activate the third, else
                    count3 += 1
            else:  # at the end add all from the last list
                listprintcards[x][y] = gcol3[count3]
                count3 += 1

    # add the new 2d to cardgame list for the calculation, from shuffle(col)
    for x in range(7):
        for y in range(3):
            cardgame[count4] = listprintcards[x][y]
            count4 += 1

    gcol1.clear()
    gcol2.clear()
    gcol3.clear()


def shuffle(col):
    if col == 1:
        for i1 in range(0, 21, 3):  # the column1 that the card is goes to the middle
            gcol2.append(cardgame[i1])
        for i2 in range(1, 21, 3):  # the column2  goes to the the first list
            gcol1.append(cardgame[i2])
        for i3 in range(2, 21, 3):  # the column3 goes to the third list
            gcol3.append(cardgame[i3])
    elif col == 2:
        for i2 in range(1, 21, 3):  # the column that the card is goes to the middle
            gcol2.append(cardgame[i2])
        for i3 in range(2, 21, 3):  # the column3 goes to the third list
            gcol3.append(cardgame[i3])
        for i1 in range(0, 21, 3):  # the column1 goes to the first list
            gcol1.append(cardgame[i1])
    else:
        for i3 in range(2, 21, 3):  # the column that the card is goes to the middle
            gcol2.append(cardgame[i3])
        for i1 in range(0, 21, 3):  # the column1 goes to the first list
            gcol1.append(cardgame[i1])
        for i2 in range(1, 21, 3):  # the column3 goes to the third list
            gcol3.append(cardgame[i2])
    # print(gcol1)
    # print(gcol2)
    # print(gcol3)


def maingame():
    createdeck()
    pickrandomcards()
    add_in_2d_cards()
    # print("Create Deck: " + str(deck))
    # print("Random cards for the game: " + str(cardgame))
    print("\n\t****Welcome to Mind reader Game****")
    print("Choose one card, and keep it in to your mind\n")

    for row in listprintcards:  # print the 2d list to user with out [] and ,
        print("\t\t" + "\t".join(map(str, row)))
        time.sleep(0.4)

    gamemenu()


def gamemenu():
    count = 0
    while True:
        if count == 3:
            break
        else:
            col = int(input("\nIn witch column is your card? 1, 2 or 3?: "))
            shuffle(col)  # split the 2d in 3 lists as the columns
            add_col_to_2d()  # add cards from the 3 lists to 2d after the shuffle
            count += 1
             # clear terminal in the future
            if count <= 2:  # display only 3 times the 2d list, to not see the last result
                # print("\n" + str(np.matrix(listprintcards)))  # print the matrix for the user to choose
                for row in listprintcards:  # print the 2d list to user with out [] and ,
                    print("\t\t" + "\t".join(map(str, row)))
                    time.sleep(0.4)

    # print("Final Matrix list :\n" + str(np.matrix(listprintcards)))
    your_card = str(listprintcards[3][1])
    print(" I am reading your MIND NOW!!!!!\n press enter to see your card!!!!!")
    input()
    print("YOUR CARD IS: " + your_card)
    print("I was right!!!")
    input("Created by Papadakis Antonis")


maingame()

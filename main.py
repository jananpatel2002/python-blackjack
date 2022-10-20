import random
from art import logo
from replit import clear
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
###  FUNCTIONS  ###
def drawCard():
    """Draws a random number from the deck"""
    return cards[random.randint(0, len(cards) - 1)]


def addToDealer(dealerCardList):
    dealerCardNew = dealerCardList
    dealerValue = sum(dealerCardNew)
    while dealerValue < 17:
        newDealerCard = drawCard()
        if newDealerCard == 11 and (newDealerCard + dealerValue) > 21:
            newDealerCard = 1
        dealerValue += newDealerCard
        dealerCardNew.append(newDealerCard)
    return dealerCardNew


def blackjack():
    print(logo)
    userValue = 0
    dealerValue = 0
    userCardList = []
    dealerCardLists = []
    n1 = drawCard()
    n2 = drawCard()
    if (n1 == 11 and n2 == 11):
        n1 = 1
    userCardList.extend([n1, n2])

    dealerCardLists.append(drawCard())

    for number in userCardList:
        userValue += number
    for number in dealerCardLists:
        dealerValue += number

    print(
        f"    Your current cards are {userCardList} which makes a total of {userValue}"
    )

    print(f"    The dealer is currently at a value of {dealerCardLists[0]}")
    choice = 'y'
    while (userValue < 21 and dealerValue < 21 and choice == 'y'):
    
        choice = input("Would you like to pick another card? 'y' or 'n' ")

        if (choice == 'y' and userValue < 21):
            newCard = drawCard()
            if newCard == 11 and (newCard + userValue) > 21:
                newCard = 1
            userValue += newCard
            userCardList.append(newCard)
            print(f"    Your cards {userCardList}, current score {userValue}")

    
    dealerCardLists = (addToDealer(dealerCardLists)) #Updates the cardlist for the dealer so that it has the max amount of hits
    
    x = sum(dealerCardLists)

    print(
        f"    Your final Hand is {userCardList} which makes a total of {userValue}"
    )
    print(
        f"    Dealer Final Hand is {dealerCardLists} which makes a total of {x}"
    )

    if (userValue == x and userValue <= 21 and x <= 21):
        print("\n        It was a Tie!")
    elif (userValue > 21):
        print(" \n        You Lose! You went over 21")
    elif userValue < x and x <= 21 and userValue <= 21:
        print(" \n        You Lose, the dealer has a higher number!")
    else:
        print(" \n        You Win!!!")

    if (input("\nWould you like to try again? Yes or No? ").lower() == 'yes'):
        clear()
        blackjack()


###  MAIN  ###
playBlackjack= input("Would you like to play a game of blackjack: Yes or No: ").lower()
if playBlackjack=="yes":
    
    blackjack()

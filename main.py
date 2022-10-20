import random
from art import logo
from replit import clear
############### Blackjack Project #####################

#Difficulty Normal 😎: Use all Hints below to complete the project.
#Difficulty Hard 🤔: Use only Hints 1, 2, 3 to complete the project.
#Difficulty Extra Hard 😭: Only use Hints 1 & 2 to complete the project.
#Difficulty Expert 🤯: Only use Hint 1 to complete the project.

############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The Ace can count as 11 or 1.
## Use the following list as the deck of cards:
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt


###  FUNCTIONS  ###
def drawCard():
    """Draws a random number from the deck"""
    return cards[random.randint(0, len(cards) - 1)]


def addToDealer(dealerCardList):
    dealerValue = sum(dealerCardList)
    while dealerValue < 17:
        newDealerCard = drawCard()
        if newDealerCard == 11 and (newDealerCard + dealerValue) > 21:
            newDealerCard = 1
        dealerValue += newDealerCard
        dealerCardList.append(newDealerCard)
    return dealerCardList


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

    dealerCardLists = addToDealer(dealerCardLists)
    x = sum(dealerCardLists)
    print(
        f"    Your final Hand is {userCardList} which makes a total of {userValue}"
    )
    print(
        f"    Dealer Final Hand is {dealerCardLists} which makes a total of {x}"
    )

    if (userValue == x and userValue <= 21 and x <= 21):
        print("It was a Tie!")
    elif (userValue > 21):
        print("You Lose! You went over 21")
    elif userValue < x and x <= 21 and userValue <= 21:
        print("You Lose, the dealer has a higher number!")
    else:
        print("You Win!!!")

    if (input("\nWould you like to try again? Yes or No? ").lower() == 'yes'):
        clear()
        blackjack()


###  MAIN  ###

blackjack()

import random
from art import logo
############### Blackjack Project #####################
print(logo)
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


userValue = 0
dealerValue = 0
userCardList = []
dealerCardList = []

userCardList.extend([drawCard(), drawCard()])
print(userCardList)

for number in userCardList:
    userValue += number

print(
    f"Your current cards are {userCardList} which makes a total of {userValue}"
)

while (userValue < 21 and dealerValue < 21):
    choice = input("Would you like to pick another card? 'y' or 'n' ")
    while (choice == 'y' and userValue < 21):
        newCard = drawCard()
        userValue += newCard
        userCardList.append(newCard)
        print(userCardList)
        print(f"Total Value: {userValue}")
    if dealerValue < 17:
        dealerValue += drawCard()
        print(dealerValue)

if (userValue > 21):
    print(userValue)
    print(dealerValue)
    print("You Lose")
else:
    print("You Win")

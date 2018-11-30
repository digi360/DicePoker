# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point, Rectangle, Text

from button import Button
from dieview import DieView

from collections import Counter

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500

playerAmount = 100
roundCost = 10

global scoreText
hand = []

def rollDice():
	# for k in range(5):
	# 	hand[k].setValue(randrange(1, 7))
	hand[0].setValue(2)
	hand[1].setValue(1)
	hand[2].setValue(3)
	hand[3].setValue(1)
	hand[4].setValue(5)
	helpText.setText("Rolling cost: -$10")

def playHand():
	global playerAmount
	playerAmount -= roundCost
	rollDice()
	checkHand()

def checkHand():
	global playerAmount
	output = helpText.getText() + "\n"
	output += str(hand[0].getValue()) + " | " + str(hand[1].getValue()) + " | " + str(hand[2].getValue()) + " | " + str(hand[3].getValue()) + " | " + str(hand[4].getValue()) + "\n"

	# if isFiveOfAKind():
	# 	output += "Five of a kind: You win $30"
	# 	playerAmount += 30
	# elif isFourOfAKind():
	# 	output += "Four of a kind: You win $15"
	# 	playerAmount += 15
	# elif isFullHouse():
	# 	output += "Full House: You win $12"
	# 	playerAmount += 15
	# elif isStraight():
	# 	output += "Straight: You win $20"
	# 	playerAmount += 15
	# elif isThreeOfAKind():
	# 	output += "Three Of A Kind: You win $8"
	# 	playerAmount += 15
	# elif isTwoPair():
	# 	output += "Two Pairs: You win $5"
	# 	playerAmount += 15
	# elif isOnePair():
	# 	output += "One Pair: You win $0"
	# 	playerAmount += 15
	# else:
	# 	output += "No wins in this roll."

	output += "isOnePair() = " + isOnePair()

	helpText.setText(output)

def isFiveOfAKind():
	return (Counter(handValues()).values() == [5])

def isFourOfAKind():
	return ( 4 in Counter(handValues()).values() )

def isFullHouse():
	return ( (3 in Counter(handValues()).values()) and (2 in Counter(handValues()).values()))

def isStraight():
	return (sorted(handValues()) == range(min(handValues()), max(handValues())+1))

def isThreeOfAKind():
	return ( (3 in Counter(handValues()).values()) and (1 in Counter(handValues()).values()))

def isTwoPair():
	return ( Counter(Counter(sorted(handValues())).values()).values() == [1, 2])

def isOnePair():
	return str( Counter(sorted(handValues())).values() ) # == [1, 1, 1, 2])

def handValues():
	return [hand[0].getValue(), hand[1].getValue(), hand[2].getValue(), hand[3].getValue(), hand[4].getValue()]

def updateScreen(scoreText):
	scoreText.setText("Score: $" + str(playerAmount))

def main():
	# create the application window
	win = GraphWin("Dice Poker", WINDOW_WIDTH, WINDOW_HEIGHT)
	win.setBackground("black")

	# draw the interface widgets
	centerPoint = Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
	quit = Button(win, Point(WINDOW_WIDTH - 50, WINDOW_HEIGHT - 50), 75, 50, 'Quit')
	quit.activate()

	roll = Button(win, Point(WINDOW_WIDTH - 125, WINDOW_HEIGHT - 50), 75, 50, 'Roll')
	roll.activate()

	m = (WINDOW_WIDTH / 5) + (5*25)
	for k in range(5):
		hand.append(DieView(win, Point(WINDOW_WIDTH / 2 - m, WINDOW_HEIGHT / 2), 100))
		m -= 125

	scoreText = Text(Point(50, 25), "Score Text Goes Here...")
	scoreText.setTextColor("white")
	scoreText.draw(win)

	global helpText
	helpText = Text(Point(WINDOW_WIDTH - 200, 25), "Help Text Goes Here...")
	helpText.setTextColor("white")
	helpText.draw(win)

	playHand()

	# event loop
	run = True
	while run:
		updateScreen(scoreText)
		clickPoint = win.getMouse()
		if (roll.clicked(clickPoint)):
			playHand()
		run = ( (not quit.clicked(clickPoint)) and (playerAmount > 0) )

	# close the window
	win.close()

main()
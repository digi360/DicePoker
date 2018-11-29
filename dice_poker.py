# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point, Rectangle, Text

from button import Button
from dieview import DieView

WINDOW_WIDTH, WINDOW_HEIGHT = 800, 500

playerAmount = 100
roundCost = 10

global scoreText
hand = []

def rollDice(cheat=0):
	if (cheat == 0):
		for k in range(5):
			hand[k].setValue(randrange(1, 7))
	else:
		for k in range(4):
			hand[k].setValue(cheat)
		hand[-1].setValue(cheat-1)

def playHand():
	global playerAmount
	playerAmount -= roundCost
	rollDice(6)
	checkHand()

def checkHand():
	output = str(hand[0].getValue()) + " | " + str(hand[1].getValue()) + " | " + str(hand[2].getValue()) + " | " + str(hand[3].getValue()) + " | " + str(hand[4].getValue())
	output += "\nFive Of A Kind = " + str(isFiveOfAKind())
	helpText.setText(output)

def isFiveOfAKind():
	firstElement = hand[0].getValue()
	for die in hand:
		if (firstElement != die.getValue()):
			return False
	return True

def isFourOfAKind():
	pass

def payOut(matches):
	if (matches == 2):
		playerAmount += 5
	if (matches == 3):
		playerAmount += 8
	if (matches == 4):
		playerAmount += 12
	if (matches == 5):
		playerAmount += 20

def countPairs():
	matches = 0
	

	return matches

def updateScreen(scoreText):
	scoreText.setText("Score: " + str(playerAmount))

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

	scoreText = Text(Point(40, 25), "Score Text Goes Here...")
	scoreText.setTextColor("white")
	scoreText.draw(win)

	global helpText
	helpText = Text(Point(WINDOW_WIDTH - 75, 25), "Help Text Goes Here...")
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
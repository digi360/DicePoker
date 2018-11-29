# Graphics program to roll a pair of dice. Uses custom widgets
# Button and DieView

from random import randrange
from graphics import GraphWin, Point, Rectangle, Text

from button import Button
from dieview import DieView

WINDOW_WIDTH, WINDOW_HEIGHT = 750, 500

def main():

	# create the application window
	win = GraphWin("Dice Roller", WINDOW_WIDTH, WINDOW_HEIGHT)
	win.setBackground("black")

	# draw the interface widgets
	centerPoint = Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
	quit = Button(win, Point(WINDOW_WIDTH - 75, WINDOW_HEIGHT - 50), 75, 50, 'Quit')
	quit.activate()

	roll = Button(win, Point(WINDOW_WIDTH - 150, WINDOW_HEIGHT - 50), 75, 50, 'Roll')
	roll.activate()

	die1 = DieView(win, Point(WINDOW_WIDTH / 2 - 50, WINDOW_HEIGHT / 2), 50)
	die2 = DieView(win, Point(WINDOW_WIDTH / 2 + 50, WINDOW_HEIGHT / 2), 50)

	# event loop
	run = True
	while run:
		clickPoint = win.getMouse()
		if (roll.clicked(clickPoint)):
			die1.setValue(randrange(1, 7))
			die2.setValue(randrange(1, 7))
		run = not quit.clicked(clickPoint)

	# close the window
	win.close()

main()
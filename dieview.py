from graphics import *

class DieView:
	"""DieView is a widget that displays a graphical representation of a standard six-sided die."""

	value = 1

	def __init__(self, win, center, size):
		""" create a view of a die e.g: d1 = DieView (myWin, Point(40,50), 20). This creates a die centered at (40,50) with length 20. """

	# define standard values for drawing the die
		self.win = win 				#for drawing the pips
		self.background = "white"	#colour of die face
		self.foreground = "black"	#colour of pips
		self.psize = 0.1 * size 	#radius of each pip
		hsize = size/2				#half the size of the die
		offset = 0.6 * hsize		#distance from centre to outer pips

		# create a square for the face
		cx, cy = center.getX(), center.getY()
		p1 = Point(cx - hsize, cy - hsize)
		p2 = Point(cx + hsize, cy + hsize)
		rect = Rectangle(p1, p2)
		rect.draw(win)
		rect.setFill(self.background)

		# create 7 circles for standard pip locations
		self.pips = [self.__makePip(cx - offset, cy - offset),
		self.__makePip(cx - offset, cy),
		self.__makePip(cx - offset, cy + offset),
		self.__makePip(cx, cy),
		self.__makePip(cx + offset, cy - offset),
		self.__makePip(cx + offset, cy),
		self.__makePip(cx + offset, cy + offset)]
		
		# Create a table of which pips are on for each value
		self.onTable = [[], [3], [2, 4], [2, 3, 4], [0, 2, 4, 6], [0, 2, 3, 4, 6], [0, 1, 2, 4, 5, 6]]

		# Draw an initial value		
		self.setValue(1)

	def __makePip(self, x, y):
		""" Internal helper method to draw a pip at (x,y)"""
		pip = Circle(Point(x, y), self.psize)
		pip.setFill(self.background)
		pip.setOutline(self.background)
		pip.draw(self.win)
		return pip

	def setValue(self, value):
		"""Set this die to display value. """

		self.value = value

		#turn all pips off
		for pip in self.pips:
			pip.setFill(self.background)

		# turn correct pips on
		for i in self.onTable[value]:
			self.pips[i].setFill(self.foreground)


	def getValue(self):
		return self.value

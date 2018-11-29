from graphics import *

WINDOW_WIDTH, WINDOW_HEIGHT = 200, 150

win = GraphWin("Simple Breakout", WINDOW_WIDTH, WINDOW_HEIGHT)

centerPoint = Point(WINDOW_WIDTH / 2, WINDOW_HEIGHT / 2)
text = Text(centerPoint, "Test Text")
text.draw(win)

while True:
    clickPoint = win.getMouse()

    if clickPoint is None:  # so we can substitute checkMouse() for getMouse()
        text.setText(str(clickPoint))
    else:
        text.setText(str(clickPoint))

win.close()
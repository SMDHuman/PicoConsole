import ConsoleAPI as cs 
import time

win = cs.LCD(3)

win.pixel(1,1)
win.pixel(0,0, "red")

win.pixel(4, 4, "blue")
win.pixel(45, 4, "blue")
win.rectangle(5, 5, 40, 40, outLine="red", inFill = "green",  outLineWidth = 4)

win.line(30, 50, 100, 100, "gray")

while(1):
	win.update()
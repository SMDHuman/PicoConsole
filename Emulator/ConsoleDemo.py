import ConsoleAPI_EMU as cs 
import time

win = cs.LCD(3)

win.pixel(1,1)
win.pixel(0,0, (1, 0, 0))

for i in range(0, 12, 2):
	win.pixel(4 + i, 4, "white")
	win.pixel(5 + i, 4, "grey")
win.rectangle(5, 5, 10, 10, outLine=(1, 0, 0), inFill = (0, 0, 1))


print(win.getPixel(7, 7))

win.circle(50, 50, 14, outLine="red", outLineWidth = 1, inFill = "yellow")
win.update()
points = [[100, 100], [150, 100], [150, 150], [125, 140], [120, 150]]
win.polygon(points)

win.bucketFill(120, 120, "brown")

while(1):
	win.update()

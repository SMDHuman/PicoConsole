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

start = time.time()
win.circle(50, 50, 10, outLine="red", outLineWidth = 1, inFill = "yellow")
end = time.time()
print(end - start)

win.update()

points = [[100, 100], [125, 90], [150, 100], [170, 170], [125, 140], [120, 150]]



start = time.time()
win.polygon(points, inFill = "brown")
end = time.time()
print(end - start)

while(1):
	win.update()

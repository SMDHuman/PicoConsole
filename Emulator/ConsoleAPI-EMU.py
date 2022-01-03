from graphics import *
import keyboard, webcolors
from itertools import permutations

class LCD:
	def __init__(self, scale = 1):
		self.scale = scale
		self.winX = 240
		self.winY = 240
		self.win = GraphWin("Pico Console", self.winX * scale, self.winY * scale, autoflush = False)
		self.win.setCoords(0, self.winY, self.winX, 0)
		self.win.setBackground("black")


	def clear(self, win):
		for item in win.items[:]:
			item.undraw()

	def fill(self, color = "black"):
		# Ekranı belirli bir renkle doldur
		color = self._color(color)
		self.clear(self.win)
		self.win.setBackground(color)
		return(0)

	def rectangle(self, x, y, width, height, outLine = "white", inFill = "black", outLineWidth = 1):
		outLine = self._color(outLine)
		inFill = self._color(inFill)
		ri = Rectangle(Point(x + outLineWidth, y + outLineWidth), 
					   Point(x + width - outLineWidth, y + height - outLineWidth))
		ro = Rectangle(Point(x, y), 
					   Point(x + width, y + height))
		ri.setOutline(inFill)
		ri.setFill(inFill)
		ro.setOutline(outLine)
		ro.setFill(outLine)
		ro.draw(self.win)
		ri.draw(self.win)
		return(0)

	def _drawLine(self, x1, y1, x2, y2, color = "white"):
		# Çizgi çiz
		dx, dy = (x2 - x1), (y2 - y1)
		step = [abs(dy), abs(dx)][abs(dx) >= abs(dy)]
		dx, dy = dx / step, dy / step
		for i in range(step):
			self.pixel(x1, y1)
			x1 += dx
			y1 += dy

	def _color(self, color):
		if(type(color) == tuple):
			color = color_rgb(int(color[0] * 255), int(color[1] * 255), int(color[2] * 255))
		return(color)

	def _drawCircle(self, xc, yc, r, color, outLineWidth):
		rs = r*(r-1)
		for y2 in range(yc - r, yc + r + 1):
			for x2 in range(xc - r, xc + r + 1):
				d = (x2 - xc)**2 + (y2 - yc)**2
				if(rs + r >= d >= rs - r*outLineWidth):
					self.pixel(x2, y2, color)

	def _circleFill(self, xc, yc, r, color, outLineWidth):
		rs = r*(r-outLineWidth)
		for y2 in range(yc - r, yc + r):
			for x2 in range(xc - r, xc + r):
				x0, y0 = x2 - xc, y2 - yc
				if(x0**2 + y0**2 < rs):
					self.pixel(x2, y2, color)

	def _areaTri(self, tri):
		return(abs(tri[0][0]*tri[1][1] + tri[1][0]*tri[2][1] + tri[2][0]*tri[0][1] - tri[0][0]*tri[2][1] - tri[1][0]*tri[0][1] - tri[2][0]*tri[1][1])/2)

	def _drawTriagnle(self, points, color):
		tArea = self._areaTri(points)
		xs = [p[0] for p in points]
		ys = [p[1] for p in points]
		minX = min(xs)
		maxX = max(xs)
		minY = min(ys)
		maxY = max(ys)
		for y in range(minY, maxY+1):
			for x in range(minX, maxX+1):
				ds = [self._areaTri([[x, y], t[0], t[1]]) for t in permutations(points, 2)]
				#print(sum(ds), tArea)
				if(sum(ds)/2 == tArea):
					self.pixel(x, y, color)

	def getPixel(self, x, y):
		# İnstenilen noktanın renk değerini döndürür
		x, y = self.win.trans.screen(x, y)
		ids = self.win.find_overlapping(x, y, x, y)

		if len(ids) > 0:
			index = ids[-1]
			color = self.win.itemcget(index, "fill")
			if(color != ''):
				if(color[0] == '#'):
					return color
				else:
					return webcolors.name_to_hex(color)

		return self.win.configure("bg")[-1].lower()

	def line(self, x1, y1, x2, y2, color = "white", width = 1):
		# Çizgi çiz
		color = self._color(color)
		if(width == 1):
			self._drawLine(x1, y1, x2, y2, color)
		else:
			pass

	def pixel(self, x, y, color = "white"):
		# Bir pixelin rengini değiştir
		color = self._color(color)
		x, y = int(x), int(y)
		if(self.scale == 1):
			self.win.plot(x, y, color)
		else:
			p = Rectangle(Point(x, y), Point(x + 1 - 1/self.scale, y + 1 - 1/self.scale))
			p.setOutline(color)
			p.setFill(color)
			p.draw(self.win)

		return(0)

	def bucketFill(self, x, y, color = "white"):
		# Belirli bir alanı istenen renkte doldurur
		color = self._color(color)
		mainColor = self.getPixel(x, y)
		pixels = [[x, y]]

		for pixel in pixels:
			self.pixel(pixel[0], pixel[1], color)
			if(not([pixel[0] + 1, pixel[1]] in pixels)):
				if(pixel[0] + 1 < self.winX):
					if(self.getPixel(pixel[0] + 1, pixel[1]) == mainColor):
						pixels.append([pixel[0] + 1, pixel[1]])
			if(not([pixel[0] - 1, pixel[1]] in pixels)):
				if(pixel[0] - 1 >= 0):
					if(self.getPixel(pixel[0] - 1, pixel[1]) == mainColor):
						pixels.append([pixel[0] - 1, pixel[1]])
			if(not([pixel[0], pixel[1] + 1] in pixels)):
				if(pixel[1] + 1 < self.winY):
					if(self.getPixel(pixel[0], pixel[1] + 1) == mainColor):
						pixels.append([pixel[0], pixel[1] + 1])
			if(not([pixel[0], pixel[1] - 1] in pixels)):
				if(pixel[1] - 1 >= 0):
					if(self.getPixel(pixel[0], pixel[1] - 1) == mainColor):
						pixels.append([pixel[0], pixel[1] - 1])
		return(0)

	def circle(self, xc, yc, r, outLine = "white", inFill = "black", outLineWidth = 1):
		outLine = self._color(outLine)
		inFill = self._color(inFill)
		self._circleFill(xc, yc, r, inFill, outLineWidth)
		self._drawCircle(xc, yc, r, outLine, outLineWidth)
		return(0)

	def update(self):
		if(self.win.isClosed()):
			self.win.close()
			exit()
		self.win.update()
		return(0)

	def text(self, x, y, c, color = "white", backColor = "black", size = 8):
		# Ekrana yazı yaz
		return(0)

	def drawImage(self, x, y, name):
		# Ekrana imaj çiz
		return(0)

	def resizeImage(self, name, sizeX, sizeY):
		# İstenen imaj istenilen boylarda uzat
		return(0)

	def setBrightness(self, value):
		# Ekran parlaklığını değiştir
		return(0)

	def polygon(self, points, outLine = "white", inFill = "black"):
		# Verilen boktalar arasında çizgi çekerek çokgen oluşturma
		triangles = [[points[0], points[i + 1], points[i + 2]] for i in range(len(points) - 2)]
		for triangle in triangles:
			self._drawTriagnle(triangle, inFill)

		for i in range(len(points)):
			self.line(points[i-1][0], points[i-1][1], points[i][0], points[i][1], outLine)

class Inputs:
	def __init__(self):
		pass

	def getDirect(self):
		# Yön tuşlarında veri gelene kadar bekler ve geri döndürür
		return(directionByNum)

	def checkDirect(self): 
		# Yön tuşlarıda ki okuduğu yönü geri döndürür
		return(directionByNum)

	def getButton(self, button, wanted = 1):
		# İstenilen butonun durumu 1 olana kadar bekler
		return(0)

	def checkButton(self, button):
		# İstenilen butonun durumunu geri döndürür s
		return(boolStat)

	def checkButtonHold(self, button, hold):
		# İstenilen butonun, istenilen zaman kadar basılı tutulması gerek
		return(0)

	def checkButtonHold(self, button, hold):
		# İstenilen butonun ne kadar basılı kaldığına göre geri dönüş ver
		return(boolStat)


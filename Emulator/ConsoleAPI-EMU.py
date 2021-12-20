from graphics import *

class LCD:
	def __init__(self, scale = 1):
		self.scale = scale
		self.winX = 240
		self.winY = 240
		self.win = GraphWin("Pico Console", self.winX * scale, self.winY * scale, autoflush = False)
		self.win.setCoords(0, self.winY, self.winX, 0)
		self.win.setBackground("black")

	def fill(self, color = "white"):
		# Ekranı belirli bir renkle doldur
		self.win.clear()
		self.win.setBackground(color)
		return(0)

	def rectangle(self, x, y, width, height, outLine = "white", inFill = "black", outLineWidth = 1):
		r = Rectangle(Point(x + (1/2) * outLineWidth, y + (1/2) * outLineWidth), Point(x + width - (1/2) * outLineWidth, y + height - (1/2) * outLineWidth))
		r.setOutline(outLine)
		r.setFill(inFill)
		r.setWidth(outLineWidth * self.scale)
		r.draw(self.win)
		return(0)

	def _drawLine(self, x1, y1, x2, y2, color = "white"):
		# Çizgi çiz
		dx = (x2 - x1)
		dy = (y2 - y1)
		if (abs(dx) >= abs(dy)):
			step = abs(dx)
		else:
			step = abs(dy)
		dx = dx / step
		dy = dy / step
		x = x1
		y = y1
		i = 1
		while (i <= step):
			self.pixel(x, y)
			x = x + dx
			y = y + dy
			i = i + 1
	
		return(0)

	def line(self, x1, y1, x2, y2, color = "white", width = 1):
		# Çizgi çiz
		if(width == 1):
			self._drawLine(x1, y1, x2, y2, color)
		else:
			pass
	
		return(0)

	def pixel(self, x, y, color = "white"):
		x, y = int(x), int(y)
		# Bir pixelin rengini değiştir
		if(self.scale == 1):
			self.win.plot(x, y, color)
		else:
			p = Rectangle(Point(x, y), Point(x + 1 - 1/self.scale, y + 1 - 1/self.scale))
			p.setOutline(color)
			p.setFill(color)
			p.draw(self.win)

		return(0)

	def bucketFill(self, x, y, color):
		# Belirli bir alanı istenen renkte doldurur
		return(0)

	def circle(self, x, y, r , outLine = "white", inFill = "black", outLineWidth = 1):
		# Bir daire çiz
		return(0)

	def update(self):
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


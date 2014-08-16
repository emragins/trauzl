from data import data
import ika ##should probably move this and make all the map data accessible from a central location in my code
import utility
##camera class to be updated independently while game runs

class Camera:
	def __init__(self):
		ika.SetCameraTarget(None)
		self.maxX = ika.Map.width
		self.maxY = ika.Map.height
		self.adjustmentX = int(ika.Video.xres/2)
		self.adjustmentY = int(ika.Video.yres/2)
		
	def Update(self):
		x, y = data.player.GetPosition()
		x -= self.adjustmentX
		y -= self.adjustmentY
		if x <0:
			x = 0
		if y <0:
			y = 0
		ika.Map.xwin = x
		ika.Map.ywin = y
		
	
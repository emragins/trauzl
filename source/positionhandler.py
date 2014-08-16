import sprite

class MovingEntity(object):
	def __init__(self, x, y, direction):
		self.posHandler = PositionHandler(self)
		self.sprite = sprite.Sprite(self)
		
		self.direction = direction
		self.x = x
		self.y = y
		
		
	def Update(self):
		self.sprite.Update()
		
	def Render(self):
		self.sprite.Render()
		
class PositionHandler(object):
	def __init__(self, parent):
		
	
	def Update(self):
	
	def Render(self):
	
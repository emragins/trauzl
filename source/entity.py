import sprite
import ika

class Entity(object):
	def __init__(self):
		self.dead = False
		self.sprite = sprite.Sprite(self)
		
	def Update(self):
		self.sprite.Update()
		
	def Render(self):
		self.sprite.Render()
		
	def IsAlive(self):
		if self.dead == False:
			return True
		return False
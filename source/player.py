import entity
import ika

class Player(object):
	def __init__(self, x, y):
		self.entity = entity.Entity()
		
	def Update(self):
		self.entity.Update()
		kb = ika.Input.keyboard
		
		if kb['LEFT'].Position():
			self.x -= 1
			##check collisions
		
		if kb['RIGHT'].Position():
			self.x += 1
			##check collisions
		
		
		#fall
		##add code... should make seperate so as to be more more accessable
		
	def Render(self):
		self.entity.Render()
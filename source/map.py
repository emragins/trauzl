import ika

class Map(object):
	def __init__(self, map):
		self.map = map
		ika.Map.Switch(self.map)
		
		
	def Update(self):
		pass
		
	def Render(self):
		pass
		
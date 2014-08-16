from data import data

"""
class to manage which order groups of things need to be updated and displayed
ie. player always comes last when being displayed

"""
import timeit


def Blocks():
	for obj in data.blocks:
		#obj.Update()
		obj.ApplyGravity()
def Objects():
	for obj in data.objects:
		obj.Update()
def Passives():	
	for obj in data.passives:
		obj.Update()

##will have to add map specific with layers in correct order to render
class Manager:
	def __init__(self):
		pass
		self.player = timeit.Timer("data.player.Update()", "from data import data")
		self.passives = timeit.Timer("manager.Passives()", "import manager")
		self.objects = timeit.Timer("manager.Objects()","import manager")
		self.blocks = timeit.Timer("manager.Blocks()", "import manager")
	def Update(self):
		data.player.Update()
		#print 'player', self.player.timeit(1)
		#print 'blocks', self.blocks.timeit(1)
		#print 'objects', self.objects.timeit(1)
		#print 'passives', self.passives.timeit(1)
		
		
		for obj in data.blocks:
			obj.Update()
			
		for obj in data.objects:
			obj.Update()
		
		for obj in data.passives:
			obj.Update()
		
		for obj in data.hud:
			obj.Update()
		
	def Render(self):
		
		for obj in data.blocks:
			obj.Render()
			
		for obj in data.objects:
			obj.Render()
			
		data.player.Render()
		
		for obj in data.hud:
			obj.Render()
manager = Manager()
			
			
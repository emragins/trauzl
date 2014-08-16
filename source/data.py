
class Data(object):
	def __init__(self):
		self.objects = []
		self.player = None
		self.passives = []
		self.hud = []
		self.blocks = []
		
	def AddObject(self, obj):
		self.objects.append(obj)

	def AddPassive(self, obj):
		self.passives.append(obj)
	
	def AssignPlayer(self, obj):
		self.player = obj
	
##maybe class will stay, maybe not
class ConfigurationData(object):
	def __init__(self):
		self.soundOn = True
		self.tilesize = 16
		
	
data = Data()
configdata = ConfigurationData()
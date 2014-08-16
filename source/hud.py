import ika #for ika.Video.xres/yres

class HUD:
	def __init__(self, position):
		self.dockPosition = position
		self.height = 0
		self.width = 0
		self.screenX = ika.Video.xres##
		self.screenY = ika.Video.yres##
		self.x = 0
		self.y = 0
		self.margin = 5
		self.duration = 0 #100 = 1 second
		self.timeLeft = self.duration
		self.visible = True
		
	def Update(self):
		if self.duration is 0:	
			pass
		elif self.timeLeft is 0:
			self.visible = False
		else:
			self.timeLeft -= 1
			
			
	def Render(self):
		pass
		
	def Show(self):
		self.visible = True
		
		if self.duration != 0:
			self.timeLeft = self.duration
		
	def EstablishXY(self):
		if self.dockPosition is 'TopLeft':
			self.x = self.margin
			self.y = self.margin
		elif self.dockPosition is 'TopRight':
			self.x = self.screenX - self.width - self.margin
			self.y = self.margin
		elif self.dockPosition is 'BottomLeft':
			self.x = self.margin
			self.y = self.screenY - self.height - self.margin
		elif self.dockPosition is 'BottomRight':
			self.x = self.screenX - self.width - self.margin
			self.y = self.screenY - self.height - self.margin
		else: #shouldn't happen, so shove stuff on mid-screen
			self.x = 100
			self.y = 100
		
class TestHUD(HUD):
	def __init__(self):
		HUD.__init__(self, 'TopLeft')
		self.height = 10
		self.width = 100
		self.duration = 500
		
		self.EstablishXY()
		self.Show()	#so that will show when initialized... not needed if duration is 0
		
	def Render(self):
		if self.visible:
			ika.Video.DrawRect(self.x, self.y, self.x + self.width, self.y + self.height, ika.RGB(10,255,100),1)
	
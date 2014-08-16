"""
Initial Backbone of code written by SDHawk... though heavily altered
"""

"""
Visual representation of an entity. Contains animation and walk scripts to control its apperance.
"""

#from animationscript import AnimationScript
#from movescript import MoveScript
import ika
#import engine
#from collision import *
import utility
import frames

class Sprite:
	
	
	Scale = 0
	Rotation = 0
	SpriteCollisions = 0
	TileCollisions = 0
	Alpha = 255
	
	x = 0
	y = 0
	HotX =0
	HotY = 0
	HotW = 16
	HotH = 16
	Width = 32
	Height = 32
	Map = 1
	
	Animations =   { 
					
					"Down_Walk" : "z6 w8 z7 w8 z8 w8 z7 w8 /0",
					"Up_Walk" : "z9 w8 z10 w8 z11 w8 z10 w8 /0",
					"Right_Walk" : "z3 w8 z4 w8 z5 w8 z4 w8 /0",
					"Left_Walk" : "z0 w8 z1 w8 z2 w8 z1 w8 /0",
						
					"Up_Stand" : "z10",
					"Down_Stand" : "z7",
					"Left_Stand" : "z1",
					"Right_Stand" : "z4",
						
					"Up_Attack" : "z1 w4 z2 w4 z3 w4 z0 w4",
					"Down_Attack" : "z3 w2 z0 w2 z1 w2 z2 w2",
					"Left_Attack" : "z0 w2 z1 w2 z2 w2 z3 w2",
					"Right_Attack" : "z2 w2 z3 w2 z0 w2 z1 w2",

					"Up_Hurt" : "rgba255,255,255,255,255,0,0,100,35 w3 rgba255,0,0,100,255,255,255,255,35 w3 /2",
					"Down_Hurt" : "rgba255,255,255,255,255,0,0,100,35 w3 rgba255,0,0,100,255,255,255,255,35 w3 /2",
					"Left_Hurt" : "rgba255,255,255,255,255,0,0,100,35 w3 rgba255,0,0,100,255,255,255,255,35 w3 /2",
					"Right_Hurt" : "rgba255,255,255,255,255,0,0,100,35 w3 rgba255,0,0,100,255,255,255,255,35 w3 /2",
						
					"Up_Dead" : "rgba255,255,255,255,0,0,0,0,5 w4",
					"Down_Dead" : "rgba255,255,255,255,0,0,0,0,5 w4",
					"Left_Dead" : "rgba255,255,255,255,0,0,0,0,5 w4",
					"Right_Dead" : "rgba255,255,255,255,0,0,0,0,5 w4"

				}
	
	def __init__(self, parent):
	
		self.parent = parent
		
		frames = {} # Contains the sprite images. Note: Later iterations should store all 
			#sprite data in a single container for reference, as opposed to having multiple 
			#copies of every sprite floating around.
		self.currentFrame = 0 #Current displayed image
		self.layer = 0
		self.animationSpeed = 1
		
		'''
		self.MoveScript = MoveScript(self)
		self.AnimationScript = AnimationScript(self)	
		self.MoveScript.PixelMovement = 0
		'''

		#Note: later add a fancy multi-frame loader.
		#self.frames.append(ika.Image("art\knight.png"))
		#self.frames.append(ika.Image("art\knight2.png"))
		#self.frames.append(ika.Image("art\knight3.png"))
		
		#self.frames = frames.LoadFrames(212,22,"art\knight.png",20,36,3,0,4,12)+frames.LoadFrames(290,21,"art\knight.png",20,36,3,0,4,8)+frames.LoadFrames(334,101,"art\knight.png",28,36,3,0,4,1)+frames.LoadFrames(290,144,"art\knight.png",20,36,3,0,4,2)+frames.LoadFrames(333,144,"art\knight.png",30,36,3,0,4,2)
		
		#self.frames = frames.LoadFrames(0,0,"images\urgan.png",16,16,1,0,0,4)
		self.frames = frames.LoadFrames(0,0,"images\\hero.png",32,32,3,0,0,12)
		
		#self.frames.append(  )
		
	def LoadSprite(self, sprite):
		
		self.frames = frames.LoadFrames(0,0,sprite,16,16,1,0,0,4)
		
	def LoadSpriteXL(self, sprite):
		
		self.frames = frames.LoadFrames(0,0,sprite,32,32,1,0,0,4)		
	
	Color = ika.RGB(255,255,255,255)
	
	def Render(self):
		#Draws the sprite. 
		#Note: Add future optimizations to only draw it if it's in viewing distance.
		if self.Map:
			xy = utility.MapToScreen([self.parent.x, self.parent.y])
		else:
			xy = [self.parent.x,self.parent.y]
		
		#if Alpha == 255:
		#	self.frames[self.currentFrame].Blit(xy[0], xy[1])
		#else:
		ika.Video.TintBlit(self.frames[self.currentFrame], xy[0], xy[1], self.Color)
		
	def Update(self):
		#Processess animation
		dir = self.parent.direction
		
		if dir is 'left':
			pass
			
		elif dir is 'right':
			pass
			
		else:
			pass
		
		'''
		self.MoveScript.Update()
		self.AnimationScript.Update()
		'''
	'''	
	def CheckLadder(self):
		
		CurTileX = self.parent.x/ika.Map.tilewidth
		CurTileY = self.parent.y/ika.Map.tileheight
		
		for Layer in range(0,4):
			OnTile = ika.Map.GetTile(CurTileX, CurTileY, Layer)
			OnObs = engine.GetObs(OnTile)
			
			if OnObs is not None and OnObs.Ladder:
				return 1
				
		return 0
	'''		
	'''	
	def CheckTileCollision(self, x, y, treasure=0):
		#NOTE: Add a case for if the map isn't the active map.
		
		#HotW = self.Width-self.HotX
		#HotH = self.Height-self.HotY
		
		if x < 0 or y< 0:
			return 1
			
		if x >= ika.Map.GetLayerProperties(self.Layer)[1]*ika.Map.tilewidth or y >= ika.Map.GetLayerProperties(self.Layer)[2]*ika.Map.tileheight:
			return 1	

		Obstructed = 0
		OnObstructed = 0
		OffObstructed = 0
		
		COnObs = 1
		COffObs = 1
		self.Ladder = 0
		
		for Layer in range(0,6):
		
			CurTileX = self.parent.x/ika.Map.tilewidth
			CurTileY = self.parent.y/ika.Map.tileheight
			
			OnTile = ika.Map.GetTile(CurTileX, CurTileY, Layer)
			
			if x > self.parent.x: #Going right
				OffTile = ika.Map.GetTile(CurTileX+1, CurTileY, Layer)
				NextTileX = CurTileX+1
				NextTileY = CurTileY
			elif x < self.parent.x: #Going left
				OffTile = ika.Map.GetTile(CurTileX-1, CurTileY, Layer)
				NextTileX = CurTileX-1
				NextTileY = CurTileY			
			elif y > self.parent.y: #going down
				OffTile = ika.Map.GetTile(CurTileX, CurTileY+1, Layer)
				NextTileX = CurTileX
				NextTileY = CurTileY+1
			elif y < self.parent.y: #going up
				OffTile = ika.Map.GetTile(CurTileX, CurTileY-1, Layer)
				NextTileX = CurTileX
				NextTileY = CurTileY-1
			
			OnObs = engine.GetObs(OnTile)
			OffObs = engine.GetObs(OffTile)
			
			if OffObs is not None and OffObs.Ladder:
				return 0
			
			if OnObs is not None and OnObs.Ladder:
				OnObstructed = 0
				COnObs = 0
			
			if COnObs and OnObs is not None and OnObs.CheckCollision(NextTileX, NextTileY, CurTileX, CurTileY,0):
				OnObstructed = 1
			if COffObs and OffObs is not None and OffObs.CheckCollision(CurTileX, CurTileY, NextTileX, NextTileY,1):
				OffObstructed = 1
			
		
		if not treasure:	
			
			if OnObstructed or OffObstructed:
				return 1
			else:
				return 0	
		else:
			#Only check on obstructions if we're only checking to make sure there isn't an obstruction between us and a treasure chest.
			if OnObstructed:
				return 1
			else:
				return 0		
		
		#xy = [ [ x+self.HotX, y+self.HotY], 
		#	   [ x+self.HotX+self.HotW, y+self.HotY],
		#	   [ x+self.HotX, y+self.HotY+self.HotH],
		#	   [ x+self.HotX+self.HotW, y+self.HotY+self.HotH]]
		
		#if self.TileCollisions:
		#	if x+16 <= 0 or y+16 <= 0:
		#		return 1
				
		#	if x >= ika.Map.GetLayerProperties(self.Layer)[1]*ika.Map.tilewidth or y >= ika.Map.GetLayerProperties(self.Layer)[2]*ika.Map.tileheight:
		#		return 1
				
		#	for z in xy:
		#		z[0] = z[0]/ika.Map.tilewidth
		#		z[1] = z[1]/ika.Map.tileheight
				
		#	#xy = utility.PixelToTile([x,y])
			
		#	Obs = 0
			
		#	for z in xy:
		#		Obs += ika.Map.GetObs(z[0],z[1],self.Layer)
			
		#	return Obs
		#	#return ika.Map.GetObs(x/ika.Map.tilewidth,y/ika.Map.tileheight,self.Layer)
		#else:
		#	return 0
	'''
	
	def IsInArea(self,x,y,w,h):	
		
		ThisEntity = Box(self.parent.x+self.HotX, self.parent.y+self.HotY, self.HotW, self.HotH)
		
		if ThisEntity.CollidesWith(Box(x,y,w,h)):
			return 1
			
		return 0
		
	def IsInAreaNoHotSpots(self,x,y,w,h):	
		
		ThisEntity = Box(self.parent.x, self.parent.y, self.Width, self.Height)
		OtherEntity = Box(x,y,w,h)
		
		#print "["+str(self.parent.x)+"-"+str(self.parent.y)+"-"+str(self.Width)+"-"+str(self.Height)+"]---"+"["+str(x)+"-"+str(y)+"-"+str(w)+"-"+str(h)+"]"
		
		if OtherEntity.CollidesWith(ThisEntity):
			return 1
			
		return 0
	'''	
	def CheckCustomCollision(self, x, y, w, h):
	
		ThisEntity = Box(x,y,w,h)
			
		for map in engine.Maps:
			if self.Parent in map.Entities:
				for entity in map.Entities:
					s = entity.Sprite
						
					if entity != self.Parent and s.Layer == self.Layer and s.SpriteCollisions and ThisEntity.CollidesWith(Box(s.x+s.HotX,s.y+s.HotY,s.HotW,s.HotH)):
							
						return entity
							
		return 0	
	'''
	'''
	def CheckSpriteCollision(self, x, y):
		#HEY LET'S TRY TO BE MORE UNEFFICENT, OKAY?
		
		if self.SpriteCollisions:
		
			ThisEntity = Box(x+self.HotX, y+self.HotY, self.HotW, self.HotH)
			
			Collision = 0
			
			for map in engine.Maps:
				if self.Parent in map.Entities:
					for entity in map.Entities:
						s = entity.Sprite
						
						if entity != self.Parent and s.Layer == self.Layer and s.SpriteCollisions and ThisEntity.CollidesWith(Box(s.x+s.HotX,s.y+s.HotY,s.HotW,s.HotH)):
							

							entity.OnTouch(self.Parent)
							Collision = 1
							
			return Collision
			
		else:
			
			return 0
	'''
class BuildingSprite(Sprite):
	
	def __init__(self, parent, image, w, h, hx, hy, hw, hh):
		
		self.Parent = parent
		self.MoveScript = MoveScript(self)
		self.AnimationScript = AnimationScript(self)
		
		self.frames = [ utility.GetImage(image) ] 
		
		self.HotX =hx
		self.HotY = hy
		self.HotW = hw
		self.HotH = hh
		self.Width = w
		self.Height = h
		
		self.Animations =   { 
						
						"Down_Walk" : "z0 /0",
						"Up_Walk" : "z0 /0",
						"Right_Walk" : "z0 /0",
						"Left_Walk" : "z0 /0",
							
						"Up_Stand" : "z0 /0",
						"Down_Stand" : "z0 /0",
						"Left_Stand" : "z0 /0",
						"Right_Stand" : "z0 /0",
					}		
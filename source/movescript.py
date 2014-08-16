from animationscript import *
from basescript import BaseScript
import direction
import ika	
	
class MoveUp:

	String = "u" #The string the command is interpeted as. ie, "u" for up.
	Progress = 0 #How far the sprite has moved thus far.
	NewX = 0
	NewY = 0
	
	def Execute(self, sprite, parent, arguments):
		
		self.ApplyMove(sprite, parent, 32)
		
		if parent.Progress > 0 or (not sprite.CheckTileCollision(self.NewX, self.NewY) and not sprite.CheckSpriteCollision(self.NewX, self.NewY)):
			
			self.ApplyMove(sprite, parent, sprite.Speed)
			
			sprite.x = self.NewX
			sprite.y = self.NewY
			
			parent.Progress += sprite.Speed
			
			if parent.PixelMovement:
				if parent.Progress >= arguments[0]:
					parent.Progress = 0
					parent.Position += 1
			else:
				#Note: Tile based movement will break if tile width isn't the same as tile height.
				#A year from now I'm going to make a tile based game and spend 5 hours trying to fix this.
				if parent.Progress >= arguments[0]*ika.Map.tilewidth:
					parent.Progress = 0
					parent.Position += 1				
		else:
			parent.Progress = 0
			parent.Position += 1
			
	def ApplyMove(self, sprite, parent, speed):
		
		self.NewX = sprite.x
		self.NewY = sprite.y-speed
			
class MoveDown(MoveUp):
	
	String = "d"
	
	def ApplyMove(self, sprite, parent,speed):
		
		self.NewX = sprite.x
		self.NewY = sprite.y+speed
			
class MoveLeft(MoveUp):
	
	String = "l"
	
	def ApplyMove(self, sprite, parent, speed):
		
		self.NewX = sprite.x-speed
		self.NewY = sprite.y
			
			
class MoveRight(MoveUp):
	
	String = "r"
	
	def ApplyMove(self, sprite, parent, speed):
		
		self.NewX = sprite.x+speed
		self.NewY = sprite.y
		
class MoveUpLeft(MoveUp):
	
	String = "ul"
	
	def ApplyMove(self, sprite, parent, speed):
		
		self.NewX = sprite.x-speed
		self.NewY = sprite.y-speed
		
class MoveUpRight(MoveUp):
	
	String = "ur"
	
	def ApplyMove(self, sprite, parent, speed):
		
		self.NewX = sprite.x+speed
		self.NewY = sprite.y-speed
		
class MoveDownLeft(MoveUp):
	
	String = "dl"
	
	def ApplyMove(self, sprite, parent, speed):
		
		self.NewX = sprite.x-speed
		self.NewY = sprite.y+speed
			
class MoveDownRight(MoveUp):
	
	String = "dr"
	
	def ApplyMove(self, sprite, parent, speed):
		
		self.NewX = sprite.x+speed
		self.NewY = sprite.y+speed

class MoveRandom(MoveUp):
	
	String = "o"
	Direction = 0
	
	def ApplyMove(self, sprite, parent):
		
		if self.Progress == 0:
			self.Direction = ika.Random(0,3)
		
		if self.Direction == 0:
		
			self.NewX = sprite.x+sprite.Speed
			self.NewY = sprite.y
			
		elif self.Direction == 1:
			
			self.NewX = sprite.x-sprite.Speed
			self.NewY = sprite.y
			
		elif self.Direction == 2:
			
			self.NewX = sprite.x
			self.NewY = sprite.y+sprite.Speed
			
		elif self.Direction == 3:
			
			self.NewX = sprite.x
			self.NewY = sprite.y-sprite.Speed
			
class MoveType:

	String = "p" #The string the command is interpeted as. ie, "u" for up.
	
	def Execute(self, grandparent, parent, arguments):	

		parent.PixelMovement = arguments[0]
		
		parent.Position += 1
		
class MoveAnimation:
	
	String = "a"
	
	def Execute(self, sprite, parent, arguments):	

		sprite.Parent.AnimationScript.Active = arguments[0]
		
		parent.Position += 1
		
class MoveSpeed:
	
	String = "s"
	
	def Execute(self, sprite, parent, arguments):	

		sprite.Speed = arguments[0]
		
		parent.Position += 1

class SetX:
	
	String = "x"
	
	def Execute(self, sprite, parent, arguments):	

		sprite.x = arguments[0]
		
		parent.Position += 1
		
class SetY:
	
	String = "y"
	
	def Execute(self, sprite, parent, arguments):	

		sprite.y = arguments[0]
		
		parent.Position += 1
		
class SetXY:
	
	String = "xy"
	
	def Execute(self, sprite, parent, arguments):	

		sprite.x = arguments[0]
		sprite.y = arguments[1]
		
		parent.Position += 1
		
class SetDirection:
	
	String = "i"
	
	def Execute(self, sprite, parent, arguments):	
		
		if arguments[0] == 0:
	
			sprite.Direction = direction.direction["Up"]
			
		elif arguments[0] == 1:
			
			sprite.Direction = direction.direction["Down"]
			
		elif arguments[0] == 2:
			
			sprite.Direction = direction.direction["Left"]
			
		elif arguments[0] == 3:
	
			sprite.Direction = direction.direction["Right"]
			
		parent.Position += 1
	
			
class MoveScript(BaseScript):
	
	#TileBased = 0 #Whether to move in a tile-based fashion or a pixel-based.
	PixelMovement = 0
	"""
		Move script command list. [x] denotes being functional.

		u<x> - Move up x pixels/tiles [x]
		d<x> - Move down x pixels/tiles [x]
		l<x> - Move left x pixels/tiles [x]
		r<x> - Move right x pixels/tiles [x]
		ul<x> - Move up left x pixels/tiles [x]
		ur<x> - Move up right x pixels/tiles [x]
		dl<x> - Move down left x pixels/tiles [x]
		dr<x> - Move down right x pixels/tiles [x]
		o<x> - Move random direction x pixels/tiles (only uses up/left/right/down, not diagonal) [x]
		
		i<x> - Set facing direction. 0 = up, 1 = down, 2 = left, 3 = right [x]
		p<x> - Set whether to move in pixels or tiles. 0 = tile, 1 = pixel [x]
		s<x> - Set walking speed [x]
		
		x<x> - Set entity's X position to x (Dangerous, doesn't collision detect) [x]
		
		y<y> - Sets entity's Y position to y (Dangerous, doesn't collision detect) [x]
		xy<x>,<y> Sets entity's x and y positions. (Dangerous, doesn't collision detect) [x]
		
		a<x> - Enables/disables sprite animation while moving. 0 = off, 1 = on [x]

		z<x> - Change sprite's frame to x. [x]
		w<x> - Wait for x amount of time before proceeding. [x]
		/<x> - Repeat. x = 0 indefintley, x > 0, that many times. [x] 		
	"""
	
	PixelMovement = 1
	CommandList = [ChangeFrame(), Wait(), Repeat(), MoveUp(), MoveDown(), MoveRight(), MoveLeft(),
				  MoveUpLeft(), MoveUpRight(), MoveDownLeft(), MoveDownRight(), MoveRandom(),
				  MoveType(), MoveAnimation(), MoveSpeed(), SetX(), SetY(), SetXY(), SetDirection()]
		
	
"""class ScriptCommand:

	String = "" #The string the command is interpeted as. ie, "u" for up.
	
	def Execute(self, grandparent, parent, arguments):"""
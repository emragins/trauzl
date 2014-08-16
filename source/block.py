import movingentity
import collisions

"""
Note: Blocks are dumb... they shouldn't know whether or not they're being grabbed. 
	Blocks are moving entities only in the sense that they are affected by gravity.
"""

class Block(movingentity.MovingEntity):
	def __init__(self, x, y, type = 'standardBlock'):
		movingentity.MovingEntity.__init__(self,x,y, type)
		
	def Update(self):
		movingentity.MovingEntity.Update(self)
		
	def BeMovedLeft(self, speed):
		self.MoveLeftBy(speed)
		
	def BeMovedRight(self, speed):
		self.MoveRightBy(speed)
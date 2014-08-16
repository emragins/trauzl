import movingentity
import stats
import ika #for input
import blockmanager


class Player(movingentity.MovingEntity):
	def __init__(self, x, y):
		movingentity.MovingEntity.__init__(self, x, y, type = 'player')
		
		self.grabbedBlock = None
		self.collidesWithBlock = None #used in positionhandler, which will set block object when appropriate
		self.blockMoveSpeed = 1
		
	def Update(self):
		kb = ika.Input.keyboard
			
		if kb['LEFT'].Position():
			self.SetState('MoveLeft')
		elif kb['RIGHT'].Position():
			self.SetState('MoveRight')
		else:
			self.SetState('Wait')
			
		if kb['UP'].Pressed():
			if not self.IsFalling():
				self.AddState('Jump')
				self.StartFalling()
		
		#'grab' button
		if kb['DOWN'].Position(): 
			if self.collidesWithBlock:
				if self.grabbedBlock is not self.collidesWithBlock:
					self.grabbedBlock = self.collidesWithBlock
					if self.direction is 'Left':
						self.AddState("GrabLeft")
					else:
						self.AddState("GrabRight")
		else:	#if not 'grabbing'
			self.DropBlock()
	
		movingentity.MovingEntity.Update(self)
	
	
		if kb['1'].Pressed():
			x,y = self.GetBlockMakingCoords()
			block = blockmanager.MakeBlock(x,y, 'standard') ##crappy. knows too much info
			##adjust for inventory count
			##add animation???
			
	
		
		if self.grabbedBlock:
			
			if self.currentState is "MoveLeft":
				self.grabbedBlock.BeMovedLeft(self.blockMoveSpeed)
			elif self.currentState is "MoveRight":
				self.grabbedBlock.BeMovedRight(self.blockMoveSpeed)
				
			
			"""this code adjusts the player's position so that it remains next to the slower-moving block"""
			#check x distance from player - needed for pulling the block because it moves slower
			if "GrabLeft" in self.extraStates: #block on left of player
				#if not in the right spot...
				if self.realX + self.hotX is not self.grabbedBlock.realX + self.grabbedBlock.hotW + 1:
					#adjust position...
					collided = self.MoveLeftBy(self.moveSpeed - self.blockMoveSpeed) ##might break if sum is negative.. probably won't happen
					#if still not in the right spot..
					##maybe don't need to check 'collided' as well
					if collided or self.realX + self.hotX is not self.grabbedBlock.realX + self.grabbedBlock.hotW + 1:
						self.DropBlock()
					
			elif "GrabRight" in self.extraStates: #block on right
				if self.realX + self.hotX + self.hotW + 1 is not self.grabbedBlock.realX:
					collided = self.MoveRightBy(self.moveSpeed - self.blockMoveSpeed) ##might break if sum is negative
					if collided or self.realX + self.hotX + self.hotW + 1 is not self.grabbedBlock.realX:
						self.DropBlock()
					
			
			#check y distance from player - needed in case block on ledge or falls too far from player
			elif self.grabbedBlock.realY < self.realY or self.grabbedBlock.realY >= self.realY + 32: ##fix... height
				self.DropBlock()
			
			
				
		
		
		##crude, adjust to add collision detection before making a block
		##also ajust to add movement to make room for making a block
	def GetBlockMakingCoords(self):
		if self.direction is 'Left':
			x = self.realX + self.hotX - 17#for block size
		else:
			x = self.realX + self.hotX + self.hotW + 1 #do not need width of block, just width of player
			
		y = self.realY
		
		return x,y
		#leftQuads = self.GetOpenQuadrantsLeft() #return lists of number of open quadrants/tiles
		#rightQuads = self.GetOpenQuadrantsRight()
		#if leftQuads + rightQuads is not []:
			
		##incomplete
		#topQuads = self.GetOpenQuadrantsTop()
		#bottomQuads = self.GetOpenQuadrantsBottom() #probably will never be used
		#return x,y
	
	def DropBlock(self):
		self.RemoveState("GrabLeft")
		self.RemoveState("GrabRight")
		self.grabbedBlock = None
		
	
	
	
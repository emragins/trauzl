import ika
import utility #(for translating pixel to tile)
from data import data

"""
object: whatever (player, enemy, block, etc.)
iheretance order: object -> moving entity -> entity -> box.  Box has realX/Y, hotX/Y/W/H
	or object -> entity -> box for objects which defy gravity yet still need to be solid
"""

def CheckSolidCollisionsForGravity(obj):
	if hasattr(obj.lastGravityCollision, 'realX'):	#if not None or a wall...
		#print obj, 'CHECKING AGAINST', obj.lastGravityCollision
		if obj.CollidesWith(obj.lastGravityCollision):
			print 'returning in quick check' 
			return obj.lastGravityCollision
	wallCollision = CheckCollisionsWalls(obj)
	if wallCollision: #should be true so long as 'wall != None'
		print 'returning wall'
		return wallCollision
	blockCollision = CheckCollisionsBlocks(obj)
	if blockCollision:
		'returning block'
		return blockCollision
	return None

def CheckSolidCollisionsForMovement(obj):
	wallCollision = CheckCollisionsWalls(obj)
	if wallCollision: #should be true so long as 'wall != None'
		return wallCollision
	blockCollision = CheckCollisionsBlocks(obj)
	if blockCollision:
		return blockCollision
	playerCollision = CheckCollisionsPlayer(obj) #needed for when pushing/pulling blocks... or if something falls on player
	if playerCollision:
		return playerCollision
	

	return None
	
def CheckCollisionsPlayer(obj):
	if obj is data.player:
		return None
	if obj.CollidesWith(data.player):
		return data.player
	return None
def CheckCollisionsBlocks(obj):
	for block in reversed(data.blocks):		
		if obj.CollidesWith(block) and obj is not block: 
			return block
	
	return None
	
def CheckCollisionsWalls(obj):
		"""
	This works in the following way:
	Corners of hotspot are tested:
		The map/tile realX's and realY's are established first, and tested immediately to maybe spare about 10 lines of code.
			This is seen in topleft and topright.
		Then the other two corners are tested.
	Sides of hotspot tested:
		Premise: if corner tiles are established, and there is a gap between these tiles, then these gaps are in the hotspot
		Test gaps on sides with variable realY (do this first since more sprites are taller than they are wide)
		Test gaps on top and bottom.
	Return True as soon as possible in order to save code.
	
	**Consider moving the 'guts' portion into its own function that would accept bounds and layer as args.**
	
	Note: This also only works for tiles that are 100% obstructed (or effectively so.)
		"""
		
		wallLayerIndex = ika.Map.FindLayerByName("Walls")
		
		hotx, hoty, hotw, hoth = obj.hotX, obj.hotY, obj.hotW, obj.hotH
		
		#bottomright (and establish bounds)
		RtileX, BtileY = utility.PixelToTile(obj.realX + hotx + hotw, obj.realY + hoty + hoth)
		obs = ika.Map.GetObs(RtileX, BtileY, wallLayerIndex)
		if obs:
			return 'bottomright'	
		#topleft (and establish bounds)
		LtileX, TtileY = utility.PixelToTile(obj.realX + hotx, obj.realY + hoty)
		obs = ika.Map.GetObs(LtileX, TtileY, wallLayerIndex)
		if obs:
			return 'topleft'
		#topright
		obs = ika.Map.GetObs(RtileX, TtileY, wallLayerIndex)
		if obs:
			return 'topright'
		#bottomleft
		obs = ika.Map.GetObs(LtileX, BtileY, wallLayerIndex)
		if obs:
			return 'bottomleft'
			
		#check to see if any gaps between tiles
		dx = RtileX - LtileX
		dy = BtileY - TtileY
		
		##next section mostly untested
		for i in range(dy-1): #aka, while dy > 1
			#left
			obs = ika.Map.GetObs(LtileX, TtileY + (i+1), wallLayerIndex)
			if obs:
				return 'leftside'
			#right
			obs = ika.Map.GetObs(RtileX, TtileY + (i+1), wallLayerIndex)
			if obs:
				return 'rightside'
				
		for i in range(dx-1): #aka, while dx > 1
			#top
			obs = ika.Map.GetObs(LtileX + (i+1), TtileY, wallLayerIndex)
			if obs:
				return 'top'
			#bottom
			obs = ika.Map.GetObs(LtileX + (i+1), BtileY, wallLayerIndex)
			if obs:
				return 'bottom'
				
		return None
#numbers are counted starting with 0, not with 1

def GetAnimationScript(type):
	if type is 'player':
		data = Player()
		return data
		
		
	else:
		return {}

def Player():
	animation = {
		'MoveLeft': [0,1,0,2],
		'MoveRight': [5,7,6,7],
		'WaitLeft': [3], 
		'WaitRight': [4],
		'JumpLeft': [8], #not really
		'JumpRight': [8]
	}
	return animation
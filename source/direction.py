"""#SDHawk
class dir: #Simple struct-like class for storing constants of the directions. Also contains lists for other purposes
	
	Up = 0
	Down = 1
	Left = 2
	Right = 3
	UpLeft = 4
	UpRight = 5
	DownLeft = 6
	DownRight = 7
	
	Move = ["u","d","l","r","b","c","e","f"] #For translating dirction numbers into move codes
	Animate = ['up','down','left','right','left','right','left','right'] #For translating direction numbers into animation directions.
	
Dir = dir()"""

class Direction:
	def __init__ (self, movescript, animation):
		self.movescript = movescript
		self.animation = animation

direction =	{
			"Up": Direction("u", "Up"),
			"Down": Direction("d", "Down"),
			"Left": Direction("l", "Left"),
			"Right": Direction("r", "Right"),
			"UpLeft": Direction("ul", "Left"),
			"UpRight": Direction("ur", "Right"),
			"DownLeft": Direction("dl", "Left"),
			"DownRight": Direction("dr", "Right")
		}
		
direction["Up"].opposite = direction["Down"]
direction["Down"].opposite = direction["Up"]
direction["Left"].opposite = direction["Right"]
direction["Right"].opposite = direction["Left"]

direction["UpLeft"].opposite = direction["DownRight"]
direction["UpRight"].opposite = direction["DownLeft"]
direction["DownLeft"].opposite = direction["UpRight"]
direction["DownRight"].opposite = direction["UpLeft"]
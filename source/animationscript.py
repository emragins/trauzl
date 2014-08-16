from basescript import BaseScript
import ika

class ChangeFrame:

	String = "z" #The string the command is interpeted as. ie, "u" for up.
	
	def Execute(self, grandparent, parent, arguments):
		grandparent.Frame = arguments[0]
		parent.Position += 1
		
class Wait:

	String = "w" #The string the command is interpeted as. ie, "u" for up.
	
	def Execute(self, grandparent, parent, arguments):
		
		Delay = arguments[0]+4
		
		if parent.Progress < Delay:
			parent.Progress += 1
		else:
			parent.Progress = 0
			parent.Position += 1
		
class Repeat:

	String = "/" #The string the command is interpeted as. ie, "u" for up.
	
	def Execute(self, grandparent, parent, arguments):
		if arguments[0] == 0:
			parent.Position = 0
			
		else:
			if len(arguments) < 2: #We stuff the custom time data into arguments since it's unique to this instance of repeat.
				arguments.append(0)
			
			arguments[1] += 1 
			if arguments[1] < arguments[0]:
				parent.Position = 0
			else:
				parent.Position += 1
				
class AdjustXY:
	
	String = "xy" #The string the command is interpeted as. ie, "u" for up.
	
	def Execute(self, grandparent, parent, arguments):
		
		grandparent.x += arguments[0]
		grandparent.y += arguments[1]

		parent.Position += 1	
		
		parent.Update()
		
class AdjustRGBA:
	
	String = "rgba"
	
	def Execute(self, sprite, script, arguments):
		
		r, g, b, a = ika.GetRGB(sprite.Color)
		
		if script.Progress == 0:
			r = arguments[0]
			g = arguments[1]
			b = arguments[2]
			a = arguments[3]
			script.Progress += 1
		
		nr = arguments[4]
		ng = arguments[5]
		nb = arguments[6]
		na = arguments[7]
		speed = arguments[8]
		
		r = self.AlterColor(r, nr, speed)
		g = self.AlterColor(g, ng, speed)
		b = self.AlterColor(b, nb, speed)
		a = self.AlterColor(a, na, speed)

		sprite.Color = ika.RGB(r,g,b,a)
		
		if r==nr and g==ng and b==nb and a==na:
			script.Position+=1
		
	def AlterColor(self, color, newcolor, speed):
		if color < newcolor:
			n = 0
			while color < newcolor and n < speed:
				color += 1
				n+=1
		elif color > newcolor:
			n = 0
			while color > newcolor and n < speed:
				color -= 1
				n+=1		

		return color
		
class AnimationScript(BaseScript):
	"""
		Animation script command list. [x] denotes being functional.
		
		xy<x><y> - Instantly alters the sprite's xys by <x> and <y>. This is relative to its current position, not absolute. (Used for adjusting extra-large frames)
		
		rgba<or><og><ob><oa><nr><ng><nb><na><speed> - Converts the sprite's colors from the o values to the n values at the rate of speed.


		z<x> - Change sprite's frame to x.  [x]
		w<x> - Wait for x amount of time before proceeding. [x]
		/<x> - Repeat. x = 0 indefintley, x > 0, that many times. [x]


	"""
	
	CommandList = [ChangeFrame(), Wait(), Repeat(), AdjustXY(), AdjustRGBA()]

"""
#Basic animation script test.

class DummySprite:
	
	Frame = 0

sprite = DummySprite()
script = AnimationScript(sprite)

script.SetScript("z1 z5 /5 z12 /3 z14 /0")

x = 0

while x < 35:
	script.Update()
	print "Update #: "+str(x)
	print "Command: "+str(script.CommandList[script.Commands[script.Position]["Command"]].String)
	print "Arguments: "+str(script.Commands[script.Position]["Arguments"])
	print "Position: "+str(script.Position)
	print "Progress: "+str(script.Progress)
	print "Frame: "+str(sprite.Frame)
	print "Finished: "+str(script.Finished)
	print "---------------------"
	x+=1
"""

		
		
"""class ScriptCommand:

	String = "" #The string the command is interpeted as. ie, "u" for up.
	
	def Execute(self, grandparent, parent, arguments):"""

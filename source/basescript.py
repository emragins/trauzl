lowercase = 'abcdefghijklmnopqrstuvwxyz'
uppercase = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
letters = lowercase + uppercase + "/"
digits = '-0123456789.'

class BaseScript:
	
	Commands = [] #List of the current commands.
	CommandList = [] #Command vocabularly for the script type.
	String = "" #A copy of the old string, used for comparisons.
	Position = 0 #Command currently being executed.
	Progress = 0 #Used for timing reference within the command.
	Finished = 1 #Used to indicate a script is finished.
	Active = 1 #Used to disable/enable a script.
	
	def __init__(self, parent):
		
		self.Parent = parent #Used for modifying the parent sprite for animation frames, position, etc.
		
	#--------------------------------------------------------------------------------------------------------------------------------------------
	
	def Update(self):
		"""
			Updates a generic script type by executing its current command list. If the command list is empty, it does nothing.
			The actual flow control is done by the commands themselves.
		"""
		
		if self.Active:
		
			if len(self.Commands) > 0 and self.Finished == False:
				
				if len(self.Commands) <= self.Position:
					
					self.Finished = 1
				
				else:
				
					self.CommandList[self.Commands[self.Position]["Command"]].Execute(self.Parent, self, self.Commands[self.Position]["Arguments"])
	
	#--------------------------------------------------------------------------------------------------------------------------------------------
	
	def SetScript(self, string): #Completley resets the script with a new one, unless the same script is running already.
		
		#same script and not finished, pass.
		if self.String == string:
			pass
		else:
			self.Commands = []
			self.Position = 0
			self.Progress = 0
			self.Finished = 0
			
			self.TranslateString(string)
			
	def SetScriptF(self, string): #Completley resets the script with a new one, unless the same script is running already or the current one isn't finished.
		
		#Same script OR not finished, pass.
		if self.String == string or self.Finished == 0:
			pass
		else:
			self.Commands = []
			self.Position = 0
			self.Progress = 0
			self.Finished = 0
			
			self.TranslateString(string)
			
	def SetScriptW(self, string): #Completley resets the script with a new one, unless the same script is running already or the current one isn't finished.
		
		#Same script OR not finished, pass.
		if self.Finished == 0:
			return 0
		else:
			self.Commands = []
			self.Position = 0
			self.Progress = 0
			self.Finished = 0
			
			self.TranslateString(string)
			return 1
			
	def ForceSetScript(self, string): #Completley resets the script with a new one, even if the same one is already running.
	
		self.Commands = []
		self.Position = 0
		self.Progress = 0
		self.Finished = 0
			
		self.TranslateString(string)

	def ChangeScript(self, string): #Alters the script without modifying the state values. Dangerous.
		
		self.TranslateString(string)
		
	#--------------------------------------------------------------------------------------------------------------------------------------------

	def FindCommand(self, command):
		"""
			Finds the string form of a command within the script type's command list.
		"""
		for i,x in enumerate(self.CommandList):
			if x.String == command:
				return i
		
		print "Invalid command: "+command
		return -1
	
	def TranslateString(self, string):
		"""
			Converts a string to a list of commands and their properties.
			Works by intrepeting letters as commands while numbers are always arguments.
			u5d1 is as valid as u5 d1, since it ignores spaces and simply considers the character shift.
			Additionally, it is capable of intrepeting ,s to seperate arguments to have multiple for a single command.
		"""
		string = string.lower() #Converts the string to lower-case for command comparisons.
		self.String = string
		string += "END" #Forces it to process the end of the string. Kinda hackish, but it works.
		
		Type = 0 #Whether it's reading number or letter data. 
		LETTER = 0
		NUMBER = 1
		Command = "" #Current command being read.
		Arguments = [""] #Current arguments being read.
		CurrentArgument = 0 #The position in the argument array currently.
		
		for x in string:
			
			if x in letters: #If the character is a letter.
				
				if Type == LETTER: #If we're currently reading letters, then add it to the command.
					Command += x
					
				elif Type == NUMBER: #But if we're currently reading numbers, then a new command has started.
					#Convert the arguments to actual numbers.
					for i, y in enumerate(Arguments):
						y = int(y)
						Arguments[i] = y
					
					#Find the command in the command list and add it to the command list.
					com = self.FindCommand(Command)
					if com != -1:						
						self.Commands.append({'Command' : com, 'Arguments' : Arguments})
					
					#Clear the command/argument variables for the next command.
					Command = ""
					Arguments = [""]
					CurrentArgument = 0
					
					#We're reading letters now.
					Type = LETTER
					
					#Add the character to the command
					Command += x
					
			elif x in digits: #If the character is a number
				
				if Type == NUMBER:
					#Add it to the argument.
					Arguments[CurrentArgument] += x
				
				elif Type == LETTER:
					#We're reading numbers now.
					Type = NUMBER
					
					#Add it to the argument.
					Arguments[CurrentArgument] += x
				
			elif x in ',': #If the character is a comma, indicating multiple arguments.
				#We're doing a new argument now.
				CurrentArgument += 1
				Arguments.append("")

#--------------------------------------------------------------------------------------------------------------------------------------------

class ScriptCommand:
	"""
		Defines a command for a script type.
	"""
	
	String = "" #The string the command is interpeted as. ie, "u" for up.
	
	def Execute(self, grandparent, parent, arguments):
		"""
			Function to execute when the command is called.
			Grandparent is the parent sprite executing the script.
			Parent is the core script container.
			Arguments are the numerical arguments provided in the script.
		"""
		
		pass 

"""
Basic basescript translation test.

class CommandTest(ScriptCommand):
	
	String = "t"
	
class CommandTest2(ScriptCommand):
		
	String = "testo"
	
Test = BaseScript()
Test.CommandList = [CommandTest, CommandTest2] 
Test.TranslateString("t4 testo2,5,3")
print Test.Commands

"""
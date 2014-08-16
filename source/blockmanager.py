from data import data
import block

def MakeBlock(x,y, type):
	if type is 'standard':
		newBlock = block.Block(x,y)
		data.blocks.append(newBlock)		
		return newBlock
	else:
		pass
		##do standardBlock stuff, I guess
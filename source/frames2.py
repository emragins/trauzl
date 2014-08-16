import ika
"""
Portions of the code originally created by Hatchet.
Other portions orginally created by SDHawk.
Turned into returning a dict by Sal
	-more picky on image format but less code outside frame creation
"""

"""
Row One: Move Left
Row Two: Move Right
Row Three: Standing and any waiting animations
Other rows: one complete animation per row... even if only one or two frames

One pixel of padding.

This can be changed by altering labelList.
"""

def LoadFrames(x,y,img, tileWidth, tileHeight, xdist,ydist):    
	"""
	This is a simple function that takes any image that's formatted like a tileset and rips the tiles into a
	list which is then returned. 
	img: image to rip from
	width/height: width and height of a single tile
	span: how many tiles per row
	numtiles: number of tiles to rip
	"""
	tiles=[]
	bigImage = ika.Canvas(img)
	#i2 = 0
	#i3 = 0
	
	x = 1 #for padding
	y = 1
	numFramesWide = int(bigImage.width /(tileWidth + 1)) 
	numFramesTall = int(bigImage.height/(tileHeight + 1)
	##labelList = ["left", "right", "standing", "other"]
	
	for i in numFramesTall:
		##framelist = []
		for j in numFramesWide:
			#pull frame
			frame = bigImage.Clip(x, y, x + tileWidth, y + tileHeight)
			
			#test if frame all same color
			color = frame.GetPixel(0,0)
			testX, testY = 1, 0
			same = False
			while frame.GetPixel(testX, testY) == color:
				if testX != tileWidth - 1:
					testX +=1
				else:
					testX = 0
					if testY != tileHeight - 1:
						testY += 1
					else:
						#conclude that every pixel has been checked and all same color
						same = True
						break
			
			if same is True:	#if every pixel in new frame same color
				break

			#add frame - only reached if all pixels not same color
			tiles.append(frame)
			
			'''
			if i > len(labelList):
				num = i - len(labelList)
			label = labelList[len(labelList)] + str(num)
			else:
				label = labelList[i]
			
			tileDict[label] = framelist
			'''
			x += tileWidth + 1 #1 for padding 
			
		y += height + 1
		
	return tiles
	
	##come up with a way to dump useless trailing frames--
	##probably just see if every pixel for frame is same color as top left pixel in same frame
	'''
	OLD CODE:
	
	for i in range(numtiles):
		tile = ika.Canvas(width, height)
		bigImage.Clip((x+((i2*width)+(i2*xdist))),(y+((i3*height)+(i3*ydist))),width,height)
		#bigImage.Blit(tile, -1-((width+1)*(i%span)), -1-((height+1)*(i%span)), ika.Opaque)
		bigImage.Blit(tile, 0, 0, ika.Opaque)
		tiles.append(ika.Image(tile))
		
		i2+=1
		if i2 >= span:
			i3+=1
			i2=0
			
			
	#ika.Exit(str(tiles))
	return tiles
	'''
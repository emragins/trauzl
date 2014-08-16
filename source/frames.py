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
	tiles={}
	bigImage = ika.Canvas(img)
	i2 = 0
	i3 = 0
	'''
	PSUEDOCODE:
	x = 1 #for padding
	y = 1
	image.gettotalwidth
	image.gettotalheight
	num frames wide
	num frames tall
	labelList = ["left", "right", "standing"]
	
	for i in numframestall:
		framelist = []
		for j in numframeswide:
			frame = cut out frame of width/height
			framelist.append(frame)
			x += width + 1 #1 for padding 
			
		if i > len(labelList):
			num = i - len(labelList)
			label = "other" + str(num)
		else:
			label = labelList[i]
			
		tileDict[label] = framelist
		
		y += height + 1
		
	return tileDict
	
	##come up with a way to dump useless trailing frames--
	##probably just see if every pixel for frame is same color as top left pixel in same frame
	'''
	
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
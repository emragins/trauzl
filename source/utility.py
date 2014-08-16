import ika
import engine

def MapToScreen(pos):
    return (pos[0] - ika.Map.xwin, pos[1] - ika.Map.ywin)

def ScreenToMap(pos):
    return (pos[0] + ika.Map.xwin, pos[1] + ika.Map.ywin)

def PixelToTile(pos):
	
	x = pos[0]
	y = pos[1]
	
	i = 0
	
	while x > i*ika.Map.tilewidth:
		i+=1
	x = i-1
		
	i = 0	
		
	while y > i*ika.Map.tileheight:
		i+=1
	y = i-1
	
	#ika.Exit(str([x,y,pos]))

	return [x, y]
	
"""	function PixelToTile(x,y)
{
	for (var i = 0; x > i*32; i++) {}
	x = i-1
	for (var i = 0; y > i*32; i++) {}
	y = i-1	
	return [x,y];
}"""

MAX_IMAGES = 20

ImageCache = { }

def GetImage(name):
	
	if not name in ImageCache:
	
		if len(ImageCache) < MAX_IMAGES:
			
			ImageCache[name] = ika.Image(name)
			
		else:
			
			ImageCache.popitem()
			
			ImageCache[name] = ika.Image(name)
		
	return ImageCache[name]
	

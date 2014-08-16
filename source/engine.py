
from data import data
import ika
#data

last_fps = 0

def UpdateList():
	for obj in data.objects:
		obj.Update()
	
def RenderList():
	ika.Render()	#map
	
	for obj in data.objects:
		obj.Render()


def MainLoop():
	last_update = 0
	
	while 1:
		if ika.GetTime() > last_update + 1:
			last_update = ika.GetTime()            

			global last_fps

			if last_fps != ika.GetFrameRate():
				ika.SetCaption( str("NEEDNAME    FPS(" + str(last_fps) + ")"))
				last_fps = ika.GetFrameRate()

			ika.Input.Update()
			UpdateList()
			
			last_update = ika.GetTime()+1
			
		RenderList()
		
		ika.Video.ShowPage()
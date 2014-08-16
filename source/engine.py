
from manager import manager
import ika
last_fps = 0

import fps
#fpsManager = fps.FPSManager(60)



def MainLoop():
	last_update = 0
	
	while 1:
		if ika.GetTime() > last_update + 1:
			last_update = ika.GetTime()            

			global last_fps

			if last_fps != ika.GetFrameRate():
				ika.SetCaption( str("Trauzl    FPS(" + str(last_fps) + ")"))
				last_fps = ika.GetFrameRate()

			ika.Input.Update()
			manager.Update()
			
			last_update = ika.GetTime()+1
			
			
		##will need to remove this when outputting map layer by layer in Manager	
		ika.Render()	#map
		#fpsManager.Render(manager.Render)		
		manager.Render()
		
		
		ika.Video.ShowPage()
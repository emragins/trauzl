import sys
sys.path = ['','source', 'python'] 

import engine
import map

map.Map("maps\\test.ika-map")

##map should be telling player where to initialize
##will need to consider how to make static player movable instead of making a new player object
##this is to allow the player to grow...
import player
player = player.Player(16*5, 16*4)
from data import data

data.AssignPlayer(player)
import camera
camera = camera.Camera()
data.AddPassive(camera)
import hud
testHUD = hud.TestHUD()
data.hud.append(testHUD)




engine.MainLoop()
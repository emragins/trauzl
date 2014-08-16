import sys
sys.path = ['','source', 'python'] 

import engine

'''


import game
game.StartScreen()
'''


import ika

ika.Map.Switch("maps\\test.ika-map")

ent = ika.Entity(80, 80, 0, "maps\\test.ika-sprite")
ika.Map.SetPlayer(ent)

#import player
#player = player.Player(16*5, 16*4)
from data import data
#data.AddObject(player)




engine.MainLoop()
import ika
import xi.movescript

def PlayerScript():
	ika.SetPlayer(Player)
	
PlayerMove = (xi.movescript.Script().MoveDown(1).Loop())
'''
	Castle Defense Router

	Handles communication between various computers

	By Paulo and Katie
'''

class Router:
	def __init__(self,grid,local_player):
		self.grid = grid
		self.local_player = local_player

	def set_action(self,x,y,action):
		''' 
			Sets the given action on the coordinate of the grid. 
			Assumes the action comes from the local player.
		'''
		self.grid.set_action(x,y,action,self.local_player)


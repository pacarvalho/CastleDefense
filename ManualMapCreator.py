'''
	Castle Defense Manual Map Creator	

	Allows the programmer to create a map by placing entities on cellArray

	By Paulo and Katie
'''
from entities.Tree import Tree
from entities.Peasant import Peasant
from Cell import Cell

class ManualMapCreator:
	def __init__(self):

		# Maps are always square
		self.map_size = 200

		# Stores the map
		self.cellArray = [[Cell() for x in range(self.map_size)] for y in range(self.map_size)]

		# Create a map border with an unpassable object
		# Nothing should be able to leave the map
		# TODO: Change this from trees!
		for i in range(self.map_size):
			self.cellArray[i][0].set_entity(Tree())
			self.cellArray[0][i].set_entity(Tree())
			self.cellArray[self.map_size-1][i].set_entity(Tree())
			self.cellArray[i][self.map_size-1].set_entity(Tree())

		self.cellArray[5][5].set_entity(Peasant())

	'''
		Returns the cell array
	'''
	def get_cell_array(self):
		return self.cellArray

'''
	Castle Defense Manual Map Creator	

	Allows the programmer to create a map by placing entities on cellArray

	By Paulo and Katie
'''
from entities.Default import Default
from entities.Tree import Tree
from entities.Peasant import Peasant
from entities.Wall import Wall
from Cell import Cell
from Player import Player
from Team import Team

class ManualMapCreator:
	def __init__(self):

		# Create Players and teams
		teamN = Team('Neutral',[Player('Neutral')])
		team1 = Team('Team 1',[Player('Player 1')])
		self.team1 = team1
		team2 = Team('Team 2',[Player('Player 2')])
		self.teams = [teamN,team2]

		# Maps are always square
		self.map_size = 100

		# Stores the map
		self.cellArray = [[Cell() for x in range(self.map_size)] for y in range(self.map_size)]

		# Create a map border with an unpassable object
		# Nothing should be able to leave the map
		# TODO: Change this from trees!
		for i in range(self.map_size):
			self.cellArray[i][0].set_entity(Tree(Player()))
			self.cellArray[0][i].set_entity(Tree(Player()))
			self.cellArray[self.map_size-1][i].set_entity(Tree(Player()))
			self.cellArray[i][self.map_size-1].set_entity(Tree(Player()))



		# Add a square of trees with a peasant in the center and one exit
		for i in range(10,21):
			self.cellArray[i][10].set_entity(Tree(Player()))
			self.cellArray[10][i].set_entity(Tree(Player()))
			self.cellArray[20][i].set_entity(Tree(Player()))
			self.cellArray[i][20].set_entity(Tree(Player()))
		self.cellArray[10][15].set_entity(Default(Player()))
		self.cellArray[13][13].set_entity(Peasant(team1.get_first_player()))

		# Add a line of wall
		for i in range(5,30):
			self.cellArray[22][i].set_entity(Wall(Player()))


		# Add some peasants
		self.cellArray[5][5].set_entity(Peasant(team2.get_first_player()))
		self.cellArray[7][7].set_entity(Peasant(team2.get_first_player()))

	'''
		Returns the cell array
	'''
	def get_cell_array(self):
		return self.cellArray

	'''
		Returns the players
	'''
	def get_teams(self):
		return self.teams

	'''
		Returns the local player
	'''
	def get_local_player(self):
		return self.team1.get_first_player()

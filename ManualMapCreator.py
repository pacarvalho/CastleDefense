'''
	Castle Defense Manual Map Creator	

	Allows the programmer to create a map by placing entities on cellArray

	By Paulo and Katie
'''

from Cell import Cell
from Player import Player
from Team import Team
from entities.Entity import Entity
import json

class ManualMapCreator:
	def __init__(self):

		# Create Players and teams
		teamN = Team('Neutral',[Player('Neutral')])
		team1 = Team('Team 1',[Player('Player 1')])
		self.team1 = team1
		team2 = Team('Team 2',[Player('Player 2')])
		self.teams = [teamN,team1,team2]

		# Maps are always square
		self.map_size = 100

		# Stores the map
		self.cellArray = [[Cell() for x in range(self.map_size)] for y in range(self.map_size)]


		# Import JSON Definition File
		with open('entities/entities.json', 'r') as data_file:
			entities = json.load(data_file)

		# Create a map border with an unpassable object
		# Nothing should be able to leave the map
		# TODO: Change this from trees!
		for i in range(self.map_size):
			self.cellArray[i][0].set_entity(Entity(Player(),entities['tree']))
			self.cellArray[0][i].set_entity(Entity(Player(),entities['tree']))
			self.cellArray[self.map_size-1][i].set_entity(Entity(Player(),entities['tree']))
			self.cellArray[i][self.map_size-1].set_entity(Entity(Player(),entities['tree']))



		# Add a square of trees with a peasant in the center and one exit
		for i in range(10,21):
			self.cellArray[i][10].set_entity(Entity(Player(),entities['tree']))
			self.cellArray[10][i].set_entity(Entity(Player(),entities['tree']))
			self.cellArray[20][i].set_entity(Entity(Player(),entities['tree']))
			self.cellArray[i][20].set_entity(Entity(Player(),entities['tree']))
		self.cellArray[10][15].set_entity(Entity(Player(),entities['default']))
		self.cellArray[13][13].set_entity(Entity(team1.get_first_player(),entities['peasant']))
		self.cellArray[14][14].set_entity(Entity(team1.get_first_player(),entities['peasant']))

		# Add a line of wall
		for i in range(5,30):
			self.cellArray[22][i].set_entity(Entity(Player(),entities['wall']))


		# Add some peasants
		self.cellArray[5][5].set_entity(Entity(team2.get_first_player(),entities['peasant']))
		self.cellArray[7][7].set_entity(Entity(team2.get_first_player(),entities['peasant']))

		# Add a tower
		self.cellArray[30][30].set_entity(Entity(team2.get_first_player(),entities['scout tower']))


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

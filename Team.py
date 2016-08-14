'''
	Castle Defense Team

	A team has players.

	By Paulo and Katie
'''

class Team:
	def __init__(self,name,players):
		# Team Name
		self.name = name

		# List of players
		self.players = players

	def get_players(self):
		''' Returns a list of players in this team '''
		return self.players

	def get_first_player(self):
		''' Gets the first player in the team '''
		return self.players[0]

	def get_are_allies(self, player1, player2):
		''' If both players are in the team returns true '''
		return (player1 in self.players) and (player2 in self.players)



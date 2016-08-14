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


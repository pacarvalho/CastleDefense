'''
	Castle Defense Entity - Peasant

	Peasant

	By Katie and Paulo
'''
from PIL import ImageTk

class Peasant:
	def __init__(self):
		# Does this cell block others from stepping on it or going through?
		self.blocking = True

		# self.icon_path = 'entities/icons/grass.gif'

		self.icon = ImageTk.PhotoImage(file='entities/icons/peasant.gif')

	# Returns the action range of this entity
	def get_range(self):
		return 1

	# Returns the image of the current state
	def get_icon(self):
		return self.icon



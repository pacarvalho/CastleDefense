'''
	Castle Defense Entity - Tree

	Tree terrain

	By Paulo and Katie
'''
from PIL import ImageTk

class Tree:
	def __init__(self):
		# Does this cell block others from stepping on it or going through?
		self.blocking = True

		# self.icon_path = 'entities/icons/grass.gif'

		self.icon = ImageTk.PhotoImage(file='entities/icons/tree.gif')

	# Returns the action range of this entity
	def get_range(self):
		return 0

	# Returns the image of the current state
	def get_icon(self):
		return self.icon



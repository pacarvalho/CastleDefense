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

		# default icon
		self.default_icon = ImageTk.PhotoImage(file='entities/icons/peasant.gif')

		# highlight icon
		self.highlight_icon = ImageTk.PhotoImage(file='entities/icons/peasant_highlight.gif')

	# Returns the action range of this entity
	def get_range(self):
		return 1

	# Returns the image of the current state
	def get_default_icon(self):
		return self.default_icon

	# Returns the image of the current state
	def get_highlight_icon(self):
		return self.highlight_icon



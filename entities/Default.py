'''
	Castle Defense Entity - Default

	Unnocopied terrain

	By Katie and Paulo
'''
from PIL import ImageTk

class Default:
	def __init__(self):
		# Does this cell block others from stepping on it or going through?
		self.blocking = False

		# default icon
		self.default_icon = ImageTk.PhotoImage(file='entities/icons/grass.gif')

	# Returns the action range of this entity
	def get_range(self):
		return 0

	# Returns the image of the current state
	def get_default_icon(self):
		return self.default_icon

	# Returns the image of the current state
	def get_highlight_icon(self):
		return self.default_icon



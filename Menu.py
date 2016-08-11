'''
	Castle Defense Menu

	Setups central game controls for user

	by Katie and Paulo
'''
from PIL import ImageTk

class Menu	:
	def __init__(self):
		self.minimap = None
		self.description = None
		self.menu_icon = ImageTk.PhotoImage(file='entities/icons/menu.gif')
		print 'menu'
		print self.menu_icon

	def get_icon(self):
		return self.menu_icon

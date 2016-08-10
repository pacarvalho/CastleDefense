'''
	Castle Defense Keyboard Handler

	By Katie and Paulo
'''

class KeyHandler:
	def __init__(self, screen):
		self.screen = screen

		self.screen.bind("<Key>", self.handler)

	def handler(self,event):
		# Pressing forward should move field of vision up
		if (event.keycode == 8255233):
			self.screen.move_screen('up')
		elif (event.keycode == 8320768):
			self.screen.move_screen('down')
		elif (event.keycode == 8189699):
			self.screen.move_screen('left')
		elif (event.keycode == 8124162):
			self.screen.move_screen('right')

		# Call the update graphics
		self.screen.update_graphics()


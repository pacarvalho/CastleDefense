'''
	Castle Defense Keyboard Handler

	By Katie and Paulo
'''

class KeyHandler:
	def __init__(self, screen):
		self.screen = screen

		self.screen.bind("<Key>", self.handler)
		self.screen.bind("<Button-1>", self.left_click_handler)
		self.screen.bind("<Button-2>", self.right_click_handler) # Right Click

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

	def left_click_handler(self,event):
		location = self.screen.get_clicked_cell(event.x, event.y)
		self.screen.set_clicked_cell(location[0],location[1])
		
		# Call the update graphics
		self.screen.update_graphics()

	def right_click_handler(self,event):
		location = self.screen.get_clicked_cell(event.x, event.y)
		self.screen.set_action_cell(location[0],location[1])
		









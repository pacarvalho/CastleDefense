'''
	Castle Defense Keyboard Handler

	By Katie and Paulo
'''

class KeyHandler:
	def __init__(self, screen):
		self.screen = screen

		self.screen.bind("<Key>", self.handler)
		self.screen.canvas.bind("<Button-1>", self.left_click_handler)
		self.screen.canvas.bind("<Shift-Button-1>", self.left_shift_click_handler)
		self.screen.canvas.bind("<Button-2>", self.right_click_handler) # Right Click

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
		# Standard click (Without Shift Key)
		location = self.screen.get_clicked_cell(event.x, event.y)
		self.screen.get_grid().set_selected(location[0],location[1], False)
		
		# Call the update graphics
		self.screen.update_graphics()

	def left_shift_click_handler(self,event):
		# Standard click (With Shift Key)
		location = self.screen.get_clicked_cell(event.x, event.y)
		self.screen.get_grid().set_selected(location[0],location[1], True)
		
		# Call the update graphics
		self.screen.update_graphics()

	def right_click_handler(self,event):
		location = self.screen.get_clicked_cell(event.x, event.y)

		# Get the currently selected action
		action = self.screen.get_control_menu().get_current_action()

		# Set this cell in the grid to be highlighted
		self.screen.get_grid().set_action(location[0],location[1], action)
		









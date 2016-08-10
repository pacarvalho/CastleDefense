'''
	Castle Defense Screen

	Displays the game screen

	By Katie and Paulo
'''

import Tkinter as tk


class Screen(tk.Tk):
	def __init__(self, *args, **kwargs):
		# Set up the drawing environment
		tk.Tk.__init__(self, *args, **kwargs)
		self.title('Castle Defense - By Paulo and Katie')

		# Size of the screen
		self.screen_width = 900
		self.screen_height = 500

		# Create a frame
		self.frame = tk.Frame(self, width=self.screen_width, height=self.screen_height)
		self.frame.pack()

		# Create the canvas to draw on
		self.canvas = tk.Canvas(self.frame, width=self.screen_width, height=self.screen_height)
		self.canvas.place(x=-1, y=-1)

		# Current viewing location
		self.current_view_x = 0
		self.current_view_y = 10

		# Number cells in sight
		self.num_cells_view_x = 25
		self.num_cells_view_y = 20


	'''
		Sets the grid for the game
	'''
	def set_grid(self, grid):
		self.grid = grid

	'''
		Updates the game graphics with the correct icons
	'''
	def update_graphics(self):
		count_x = -1
		for x in range(self.current_view_x,self.current_view_x+self.num_cells_view_x):
			count_x += 1
			count_y = -1
			for y in range(self.current_view_y,self.current_view_y+self.num_cells_view_y):
				count_y += 1
				# TODO: Change this so that it creates on the first run and then updates it. 
				self.canvas.create_image(count_x*32, count_y*32, anchor=tk.NW, image=self.grid.get_icon(x,y))

	'''
		Moves the screen in the given direction by x cells
	'''
	def move_screen(self, direction):
		if (direction == 'up'):
			self.current_view_y += 2
		elif (direction == 'down'):
			self.current_view_y -= 2
		elif (direction == 'left'):
			self.current_view_x += 2
		elif (direction == 'right'):
			self.current_view_x -= 2

		# Keep the view within bounds
		if (self.current_view_y < 0):
			self.current_view_y = 0
		if (self.current_view_y > self.grid.num_cells_y-self.num_cells_view_y):
			self.current_view_y = self.grid.num_cells_y-self.num_cells_view_y
		if (self.current_view_x < 0):
			self.current_view_x = 0
		if (self.current_view_x > self.grid.num_cells_x-self.num_cells_view_x):
			self.current_view_x = self.grid.num_cells_x-self.num_cells_view_x










'''
	Castle Defense Screen

	Displays the game screen

	By Katie and Paulo
'''

import Tkinter as tk


class Screen(tk.Tk):
	def __init__(self, *args, **kwargs):

		########## Important Variables ############
		# Current viewing location
		self.current_view_x = 0
		self.current_view_y = 10
		# Number cells in sight
		self.num_cells_view_x = 25
		self.num_cells_view_y = 20
		# Size of a cell in pixels
		self.cell_size = 32

		# Set up the drawing environment
		tk.Tk.__init__(self, *args, **kwargs)
		self.title('Castle Defense - By Paulo and Katie')

		# Size of the screen
		self.screen_width = 1000
		self.screen_height = 600

		# Create a frame
		self.frame = tk.Frame(self, width=self.screen_width, height=self.screen_height)
		self.frame.pack()

		# Create the canvas to draw on
		self.canvas = tk.Canvas(self.frame, width=self.screen_width, height=self.screen_height)
		self.canvas.place(x=self.screen_width/2 - (self.num_cells_view_x*self.cell_size)/2, y=50)

	'''
		Sets the grid for the game
	'''
	def set_grid(self, grid):
		self.grid = grid

		# Keep references to all images that can appear on the screen
		self.canvas_image = [[self.canvas.create_image(x*self.cell_size, y*self.cell_size, anchor=tk.NW, image=self.grid.get_icon(x,y)) for y in range(self.num_cells_view_y)] for x in range(self.num_cells_view_x)]

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
				self.canvas.itemconfig(self.canvas_image[count_x][count_y],image=self.grid.get_icon(x,y))


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










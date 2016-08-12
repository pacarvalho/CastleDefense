'''
	Castle Defense Screen

	Displays the game screen

	By Katie and Paulo
'''

import Tkinter as tk
import math 

class Screen(tk.Tk):
	def __init__(self, *args, **kwargs):

		########## Important Variables ############
		# Current viewing location
		self.current_view_x = 0
		self.current_view_y = 10
		# Number cells in sight
		self.num_cells_view_x = 25
		self.num_cells_view_y = 17
		# Size of a cell in pixels
		self.cell_size = 32

		# Set up the drawing environment
		tk.Tk.__init__(self, *args, **kwargs)
		self.title('Castle Defense - By Paulo and Katie')

		# Size of the screen
		self.screen_width = 1000
		self.screen_height = 800

		# Create a frame
		self.frame = tk.Frame(self, width=self.screen_width, height=self.screen_height)
		self.frame.pack()

		# Create the canvas to draw on
		self.canvas = tk.Canvas(self.frame, width=self.screen_width, height=self.screen_height)
		self.canvas.place(x=self.screen_width/2 - (self.num_cells_view_x*self.cell_size)/2, y=7)


	'''
		Sets the grid for the game
	'''
	def set_grid(self, grid):
		self.grid = grid

		# Keep references to all images that can appear on the screen
		self.canvas_image = [[self.canvas.create_image(x*self.cell_size, y*self.cell_size, anchor=tk.NW, image=self.grid.get_icon(x,y)) for y in range(self.num_cells_view_y)] for x in range(self.num_cells_view_x)]

	'''
		Sets the grid for the game
	'''
	def set_menu(self, menu):
		self.menu = menu

		# Keep references to all images that can appear on the screen
		self.canvas_menu = self.canvas.create_image(0, self.num_cells_view_y*32, anchor=tk.NW, image=self.menu.get_icon())
		
		# Set initial menu text
		self.menu_text = self.canvas.create_text(self.screen_width/2.7, self.num_cells_view_y*self.cell_size + 20, anchor=tk.NW, text = self.menu.get_text({}), font=("Helvetica", 18) )
		
		# Set control menu
		self.control_menu = self.menu.get_control_menu()
		
		# Variables for configuring the display of the buttons
		init_x = self.screen_width/1.52
		init_y = self.num_cells_view_y*self.cell_size + 19
		btn_width = self.cell_size*1.8
		btn_height = self.cell_size

		# Place buttons on menu
		buttons = self.control_menu.get_buttons()
		num_btns = self.control_menu.get_num_btns()
		for i in range(num_btns):
			btn = buttons[i]
			btn.place(x = init_x + btn_width*(i%4) , y = init_y+btn_height*(i/4), width = btn_width, height = btn_height, anchor=tk.NW)

	'''
		Updates the game graphics with the correct icons
	'''
	def update_graphics(self):
		# Update view of World
		count_x = -1
		for x in range(self.current_view_x,self.current_view_x+self.num_cells_view_x):
			count_x += 1
			count_y = -1
			for y in range(self.current_view_y,self.current_view_y+self.num_cells_view_y):
				count_y += 1
				self.canvas.itemconfig(self.canvas_image[count_x][count_y],image=self.grid.get_icon(x,y))

		# Update the menu
		self.update_menu()

	'''
		Updates the game menu with the correct information
	'''
	def update_menu(self):
		###### Update Menu Text ###### 
		selected_cells = self.grid.get_selected()
		self.canvas.itemconfig(self.menu_text, text=self.menu.get_text(selected_cells))

		###### Update Menu Buttons ######
		# Get available actions from the selected cells
		available_actions = self.menu.get_available_actions(selected_cells)
		self.control_menu.update_buttons(available_actions)



	'''
		Button Callback
	'''
	def btn_callback(self):
		print 'CALLBACK'

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

	'''
		Gets the cell in the grid from the screen at mouseclick x,y
	'''
	def get_clicked_cell(self, click_x, click_y):
		# Calculate the cell based on the mouse click
		cell_in_view_X = int(math.floor(click_x/32))
		cell_in_view_Y = int(math.floor(click_y/32))

		cell_in_grid_X = cell_in_view_X + self.current_view_x 
		cell_in_grid_Y = cell_in_view_Y + self.current_view_y

		# If the click is out of bounds
		if (cell_in_grid_X < 0):
			cell_in_grid_X = 0
		if (cell_in_grid_X > self.current_view_x + self.num_cells_view_x-1):
			cell_in_grid_X = self.current_view_x + self.num_cells_view_x-1
		if (cell_in_grid_Y < 0):
			cell_in_grid_Y = 0
		if (cell_in_grid_Y > self.current_view_y + self.num_cells_view_y-1):
			cell_in_grid_Y = self.current_view_y + self.num_cells_view_y-1

		return (cell_in_grid_X,cell_in_grid_Y)
		

	'''
		Sets a given cell as selected
	'''
	def set_clicked_cell(self, cell_x, cell_y, isMultiple):
		# Set this cell in the grid to be highlighted
		self.grid.set_selected(cell_x, cell_y, isMultiple)

	'''
		Set a given cell with an action
	'''
	def set_action_cell(self, cell_x, cell_y):
		# Set this cell in the grid to be highlighted
		self.grid.set_action(cell_x, cell_y)



	














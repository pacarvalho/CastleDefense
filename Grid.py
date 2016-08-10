'''
	Castle Defense Grid

	Keeps the board information. 

	by Katie and Paulo
'''
class Grid:
	def __init__(self, cells):
		# Array of cells (2D Array)
		self.cells = cells

		# Save the size of the grid
		self.num_cells_x, self.num_cells_y = len(cells), len(cells[0])

		# Save the location of the currently highlighted cell in the grid
		self.selected_cell_x = 0
		self.selected_cell_y = 0

	'''
		Gets the correct icons from the cells at a specific 
		x,y coordinate in the grid
	'''
	def get_icon(self,x,y):
		return self.cells[x][y].get_icon()

	'''
		Sets the cell at the given x,y location to be highlighted
	'''
	def set_selected(self,x,y):
		# Only deselect if the new clicked cell allowed itself to be selected
		selectConfirmed = self.cells[x][y].select()
		if (selectConfirmed and not ((x == self.selected_cell_x) and (y == self.selected_cell_y))):
			# Deselect previous cell if one exists
			self.cells[self.selected_cell_x][self.selected_cell_y].deselect()

			# Save the currenlty selected cell
			self.selected_cell_x = x
			self.selected_cell_y = y

		


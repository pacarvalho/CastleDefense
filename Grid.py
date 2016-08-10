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
		self.highlighted_cell_x = -1
		self.highlighted_cell_y = -1

	'''
		Gets the correct icons from the cells at a specific 
		x,y coordinate in the grid
	'''
	def get_icon(self,x,y):
		return self.cells[x][y].get_icon()

	'''
		Sets the cell at the given x,y location to be highlighted
	'''
	def set_highlighted(self,x,y):
		# Deselect previous cell if one exists
		if (self.highlighted_cell_x > 0 and self.highlighted_cell_y > 0):
			self.cells[self.highlighted_cell_x ][self.highlighted_cell_y].deselect()

		# Set new cell to be selected
		self.highlighted_cell_x = x
		self.highlighted_cell_y = y
		self.cells[self.highlighted_cell_x][self.highlighted_cell_y].select()


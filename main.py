'''
	Castle Defense Main

	Runs the castle defense program

	By Paulo and Katie
'''

from Screen import Screen
from Grid import Grid
from Menu import Menu
from KeyHandler import KeyHandler
from ManualMapCreator import ManualMapCreator

# Intantiate the screen
screen = Screen()

# Instantiate the key handler
keyHandler = KeyHandler(screen)

# Instantiate the grid with its default cells
manualMapCreator = ManualMapCreator()
grid = Grid(manualMapCreator.get_cell_array(),manualMapCreator.get_teams())
screen.set_grid(grid)

# Instatiate the menu with default values
menu = Menu()
screen.set_menu(Menu())

# Runs the game
def run():
	# Move entities
	grid.update()

	screen.update_graphics()

	# Updates the screen
	screen.update()

	# Calls this function periodically
	screen.after(200, lambda: run())	

# Calls the run method for the first time
run()

# Main game loop
screen.mainloop()
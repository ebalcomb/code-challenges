import random

def minesweeper(width, height, mines):
	width_counter = width
	height_counter = height
	non_mines = width*height - mines
	characters = []
	for i in range(non_mines):
		characters.append(0)
	for i in range(mines):
		characters.append("*")
	random.shuffle(characters)

	mines_map = []


	while height_counter > 0:
		this_row = []
		while width_counter > 0:
			this_row.append(characters.pop())
			width_counter -= 1
		width_counter = width
		mines_map.append(this_row)
		height_counter -= 1

	return mines_map


print minesweeper(3, 4, 3)
# import pygame library
from tracemalloc import start
import pygame
import time

# initialise the pygame font
pygame.font.init()

# Total window
screen = pygame.display.set_mode((700, 700))

# Title and Icon
pygame.display.set_caption("SUDOKU SOLVER USING BACKTRACKING")
img = pygame.image.load('icon.svg')
pygame.display.set_icon(img)

x = 0
y = 0
dif = 500 / 9
val = 0
# Default Sudoku Board.
grid =[
		[7, 8, 0, 4, 0, 0, 1, 2, 0],
		[6, 0, 0, 0, 7, 5, 0, 0, 9],
		[0, 0, 0, 6, 0, 1, 0, 7, 8],
		[0, 0, 7, 0, 4, 0, 2, 6, 0],
		[0, 0, 1, 0, 5, 0, 9, 3, 0],
		[9, 0, 4, 0, 6, 0, 0, 0, 5],
		[0, 7, 0, 3, 0, 0, 0, 1, 2],
		[1, 2, 0, 0, 0, 7, 4, 0, 0],
		[0, 4, 9, 2, 0, 6, 0, 0, 7]
	]

# Load test fonts for future use
font1 = pygame.font.SysFont("comicsans", 30)
font2 = pygame.font.SysFont("comicsans", 10)
def get_cord(pos):
	global x
	x = pos[0]//dif
	global y
	y = pos[1]//dif

# Highlight the cell selected
def draw_box():
	return True

# Function to draw required lines for making Sudoku grid		
def draw():
	# Draw the lines
		
	for i in range (9):
		for j in range (9):
			if grid[i][j]!= 0:

				# Fill blue color in already numbered grid
				pygame.draw.rect(screen, (0, 153, 153), (i * dif, j * dif, dif + 1, dif + 1))

				# Fill grid with default numbers specified
				text1 = font1.render(str(grid[i][j]), 1, (0, 0, 0))
				screen.blit(text1, (i * dif+17, j * dif+5))
	# Draw lines horizontally and verticallyto form grid		
	for i in range(10):
		if i % 3 == 0 :
			thick = 7
		else:
			thick = 1
		pygame.draw.line(screen, (0, 0, 0), (0, i * dif), (500, i * dif), thick)
		pygame.draw.line(screen, (0, 0, 0), (i * dif, 0), (i * dif, 500), thick)	

# Fill value entered in cell	
def draw_val(val):
	text1 = font1.render(str(val), 1, (0, 0, 0))
	screen.blit(text1, (x * dif + 15, y * dif + 15))

# Raise error when wrong value entered
def raise_error1():
	text1 = font1.render("WRONG !!!", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))
def raise_error2():
	text1 = font1.render("Wrong !!! Not a valid Key", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))

# Check if the value entered in board is valid
def valid(m, i, j, val):
	for it in range(9):
		if m[i][it]== val:#check row
			return False
		if m[it][j]== val:#check column
			return False
	#check square
	it = i//3
	jt = j//3
	for i in range(it * 3, it * 3 + 3):
		for j in range (jt * 3, jt * 3 + 3):
			if m[i][j]== val:
				return False
	return True

def count_node_function(grid,count_node) :
    for i in range(0,len(grid)) :
        for j in range(0,len(grid)) :
            if grid[i][j] == 0 :
                count_node += 1
count_node = 0
start_breath = 0
copy_grid = grid
count_round = 0

def solve_B(grid, i, j,st_b,count_node,count_round):
	# print("Run Program Solver")
	# print("\nStart Breath = ",st_b)
	# print("Count Round = ",count_round)
	# print("---------------------------")
	while st_b < count_node :
		while grid[i][j] != 0 :
			if i < 8 :
				i += 1
			elif i == 8 and j < 8 :
				i = 0
				j += 1
			elif i == 8 and j == 8 :
				return True
		pygame.event.pump()
		
		for it in range(1, 10) :
			if valid(grid,i,j,it) :
				# print("\nStart Breath = ",st_b)
				# print("Count Round = ",count_round)
				grid[i][j] = it
                # white color background\
				screen.fill((255, 255, 255))
				text1= font1.render("Breadth", 1, (0, 0, 0))
				BreathDisplay = font1.render(str(st_b), 1, (0, 0, 0))
				screen.blit(text1, (20, 520))
				screen.blit(BreathDisplay, (20, 550))
				draw()
				draw_box()
				pygame.display.update()
				pygame.time.delay(1)
				if count_round < st_b :
					solve_B(grid,i,j,st_b,count_node,count_round+1)
				if st_b >= count_node-1 and count_round >=count_node-1 :
					print(grid)
				screen.fill((255, 255, 255))
				draw()
				draw_box()
				pygame.display.update()
				pygame.time.delay(1)
			if it >= 9 and count_round <= st_b :
				grid[i][j] = 0
				if st_b >= 0 and count_round == 0 :
					st_b += 1
				else :	
					return True
		
	return False

# Solves the sudoku board using depth first search
def solve_D(grid, i, j):
	while grid[i][j]!= 0:
		if i<8:
			i+= 1
		elif i == 8 and j<8:
			i = 0
			j+= 1
		elif i == 8 and j == 8:
			return True
	pygame.event.pump()
	for it in range(1, 10):
		if valid(grid, i, j, it)== True:
			grid[i][j] = it
			global x, y
			x = i
			y = j
			# white color background\
			screen.fill((255, 255, 255))
			
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(1000)
			if solve_D(grid, i, j)== 1:
				return True
			else:
				grid[i][j]= 0
			# white color background\
			screen.fill((255, 255, 255))
		
			draw()
			draw_box()
			pygame.display.update()
			pygame.time.delay(1000)
	return False

# Display instruction for the game
def instruction():
	text1 = font2.render("PRESS ENTER TO RESET TO DEFAULT / R TO EMPTY", 1, (0, 0, 0))
	text2 = font2.render("ENTER D FOR DEPTH FIRST SEARCH", 1, (0, 0, 0))
	text3 = font2.render("ENTER B FOR BREATH FIRST SEARCH" , 1 , (0,0,0))
	screen.blit(text1, (20, 520))	
	screen.blit(text2, (20, 540))
	screen.blit(text3, (20, 560))

# Display options when solved
def result():
	text1 = font1.render("FINISHED PRESS ENTER or R", 1, (0, 0, 0))
	screen.blit(text1, (20, 570))
run = True
flag1 = 0
flag2 = 0
flag3 = 0
rs = 0
error = 0

# The loop thats keep the window running
while run:
	
	# White color background
	screen.fill((255, 255, 255))
    
	# Loop through the events stored in event.get()
	for event in pygame.event.get():
		# Quit the game window
		if event.type == pygame.QUIT:
			run = False
		# Get the mouse position to insert number
		if event.type == pygame.MOUSEBUTTONDOWN:
			flag1 = 1
			pos = pygame.mouse.get_pos()
			get_cord(pos)
		# Get the number to be inserted if key pressed
		if event.type == pygame.KEYDOWN:
			if event.key == pygame.K_LEFT:
				x-= 1
				flag1 = 1
			if event.key == pygame.K_RIGHT:
				x+= 1
				flag1 = 1
			if event.key == pygame.K_UP:
				y-= 1
				flag1 = 1
			if event.key == pygame.K_DOWN:
				y+= 1
				flag1 = 1
			if event.key == pygame.K_1:
				val = 1
			if event.key == pygame.K_2:
				val = 2
			if event.key == pygame.K_3:
				val = 3
			if event.key == pygame.K_4:
				val = 4
			if event.key == pygame.K_5:
				val = 5
			if event.key == pygame.K_6:
				val = 6
			if event.key == pygame.K_7:
				val = 7
			if event.key == pygame.K_8:
				val = 8
			if event.key == pygame.K_9:
				val = 9
			if event.key == pygame.K_d:
				flag2 = 1
			if event.key == pygame.K_b:
				flag3 = 1
                
			# If R pressed clear the sudoku board
			if event.key == pygame.K_r:
				rs = 0
				error = 0
				flag2 = 0
				flag3 = 0
				grid =[
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0],
				[0, 0, 0, 0, 0, 0, 0, 0, 0]
				]
			# If enter is pressed reset the board to default
			if event.key == pygame.K_RETURN:
				rs = 0
				error = 0
				flag2 = 0
				flag3 = 0
				grid =[
					[7, 8, 0, 4, 0, 0, 1, 2, 0],
					[6, 0, 0, 0, 7, 5, 0, 0, 9],
					[0, 0, 0, 6, 0, 1, 0, 7, 8],
					[0, 0, 7, 0, 4, 0, 2, 6, 0],
					[0, 0, 1, 0, 5, 0, 9, 3, 0],
					[9, 0, 4, 0, 6, 0, 0, 0, 5],
					[0, 7, 0, 3, 0, 0, 0, 1, 2],
					[1, 2, 0, 0, 0, 7, 4, 0, 0],
					[0, 4, 9, 2, 0, 6, 0, 0, 7]
				]
    
	if flag2 == 1:
		start_time = time.time()					
		if solve_D(grid, 0, 0)== False:
			error = 1
		else:
			rs = 1
		elasped_time = time.time()-start_time
		print(elasped_time)			
		flag2 = 0

	if flag3 == 1:
		count_node_function(grid,count_node)
		start_time = time.time()				
		if solve_B(grid, 0, 0,start_breath,count_node,count_round)== False:
			error = 1
		else:
			rs = 1
		elasped_time = time.time()-start_time
		print("time=",end='')
		print(elasped_time)			
		flag3 = 0
	
	if val != 0:		
		draw_val(val)
		# print(x)
		# print(y)
		if valid(grid, int(x), int(y), val)== True:
			grid[int(x)][int(y)]= val
			flag1 = 0
		else:
			grid[int(x)][int(y)]= 0
			raise_error2()
		val = 0
	
	if error == 1:
		raise_error1()
	if rs == 1:
		result()	
	draw()
	if flag1 == 1:
		draw_box()	

	instruction()

	# Update window
	pygame.display.update()

# Quit pygame window
pygame.quit()	
	

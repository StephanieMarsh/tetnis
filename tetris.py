# import pygame
# import random
# pygame.init()

# screen_width = 300  # Adjust as needed
# screen_height = 600
# screen = pygame.display.set_mode((screen_width, screen_height))
# pygame.display.set_caption('Tetris')

# grid_width = 10
# grid_height = 20
# block_size = 30  # Size of each block in pixels

# grid = [[(0, 0, 0) for _ in range(grid_width)] for _ in range(grid_height)]

# # Define the dimensions of the playing area
# play_width = grid_width * block_size  # Width of the playing area
# play_height = grid_height * block_size  # Height of the playing area
# top_left_x = (screen_width - play_width) // 2  # Center the grid horizontally
# top_left_y = screen_height - play_height  # Position it at the bottom of the screen


# #s tetromino
# S = [['.....',
#       '.....',
#       '..OO.',
#       '.OO..',
#       '.....'],
#      ['.....',
#       '..O..',
#       '..OO.',
#       '...O.',
#       '.....']]

# #z tetromino
# Z = [['.....',
#       '.....',
#       '.OO..',
#       '..OO.',
#       '.....'],
#      ['.....',
#       '..O..',
#       '.OO..',
#       '.O...',
#       '.....']]

# #i tetromino
# I = [['.....',
#       '.....',
#       'OOOO.',
#       '.....',
#       '.....'],
#      ['..O..',
#       '..O..',
#       '..O..',
#       '..O..',
#       '.....']]

# #o tetromino
# O = [['.....',
#       '.....',
#       '.OO..',
#       '.OO..',
#       '.....']]

# #j tetromino
# J = [['.....',
#       '.O...',
#       '.OOO.',
#       '.....',
#       '.....'],
#      ['.....',
#       '..OO.',
#       '..O..',
#       '..O..',
#       '.....'],
#      ['.....',
#       '.....',
#       '.OOO.',
#       '...O.',
#       '.....'],
#      ['.....',
#       '..O..',
#       '..O..',
#       '.OO..',
#       '.....']]

# #l tetromino
# L = [['.....',
#       '...O.',
#       '.OOO.',
#       '.....',
#       '.....'],
#      ['.....',
#       '..O..',
#       '..O..',
#       '..OO.',
#       '.....'],
#      ['.....',
#       '.....',
#       '.OOO.',
#       '.O...',
#       '.....'],
#      ['.....',
#       '.OO..',
#       '..O..',
#       '..O..',
#       '.....']]

# #t tetromino
# T = [['.....',
#       '..O..',
#       '.OOO.',
#       '.....',
#       '.....'],
#      ['.....',
#       '..O..',
#       '..OO.',
#       '..O..',
#       '.....'],
#      ['.....',
#       '.....',
#       '.OOO.',
#       '..O..',
#       '.....'],
#      ['.....',
#       '..O..',
#       '.OO..',
#       '..O..',
#       '.....']]

# shapes = [S, Z, I, O, J, L, T]
# colors = [(0, 255, 0),    # Green
#           (255, 0, 0),    # Red
#           (0, 255, 255),  # Cyan
#           (255, 255, 0),  # Yellow
#           (0, 0, 255),    # Blue
#           (255, 165, 0),  # Orange
#           (128, 0, 128)]  # Purple

# class Piece(object):
#     def __init__(self, x, y, shape):
#         self.x = x
#         self.y = y
#         self.shape = shape
#         self.color = random.choice(colors)  # Assign random color
#         self.rotation = 0

# def move_left(piece):
#     piece.x -= 1

# def move_right(piece):
#     piece.x += 1

# def move_down(piece):
#     piece.y += 1

# def rotate(piece):
#     piece.rotation = (piece.rotation + 1) % len(piece.shape)


# def valid_space(piece, grid):
#     accepted_positions = [...]
#     formatted = convert_shape_format(piece)
#     for pos in formatted:
#         if pos not in accepted_positions:
#             if pos[1] > -1:
#                 return False
#     return True


# def convert_shape_format(piece):
#     positions = []
#     format = piece.shape[piece.rotation % len(piece.shape)]
#     for i, line in enumerate(format):
#         row = list(line)
#         for j, column in enumerate(row):
#             if column == 'O':
#                 positions.append((piece.x + j, piece.y + i))
#     return positions

# def clear_rows(grid, locked_positions):
#     inc = 0
#     for i in range(len(grid)-1, -1, -1):
#         row = grid[i]
#         if (0, 0, 0) not in row:
#             inc += 1
#             ind = i
#             for j in range(len(row)):
#                 try:
#                     del locked_positions[(j, i)]
#                 except:
#                     continue
#     if inc > 0:
#         for key in sorted(list(locked_positions), key=lambda x: x[1])[::-1]:
#             x, y = key
#             if y < ind:
#                 newKey = (x, y + inc)
#                 locked_positions[newKey] = locked_positions.pop(key)

# def check_lost(positions):
#     for pos in positions:
#         x, y = pos
#         if y < 1:
#             return True
#     return False

# for event in pygame.event.get():
#     if event.type == pygame.QUIT:
#         run = False
#     if event.type == pygame.KEYDOWN:
#         if event.key == pygame.K_LEFT:
#             move_left(current_piece)
#         elif event.key == pygame.K_RIGHT:
#             move_right(current_piece)
#         elif event.key == pygame.K_DOWN:
#             move_down(current_piece)
#         elif event.key == pygame.K_UP:
#             rotate(current_piece)


# def main():
#     locked_positions = {}
#     grid = create_grid(locked_positions)
#     change_piece = False
#     run = True
#     current_piece = get_shape()
#     next_piece = get_shape()
#     clock = pygame.time.Clock()
#     fall_time = 0

#     while run:
#         fall_speed = 0.27
#         grid = create_grid(locked_positions)
#         fall_time += clock.get_rawtime()
#         clock.tick()

#         if fall_time/1000 > fall_speed:
#             fall_time = 0
#             move_down(current_piece)
#             if not valid_space(current_piece, grid) and current_piece.y > 0:
#                 current_piece.y -= 1
#                 change_piece = True

#         # User input handling code here

#         shape_pos = convert_shape_format(current_piece)

#         for i in range(len(shape_pos)):
#             x, y = shape_pos[i]
#             if y > -1:
#                 grid[y][x] = current_piece.color

#         if change_piece:
#             for pos in shape_pos:
#                 p = (pos[0], pos[1])
#                 locked_positions[p] = current_piece.color
#             current_piece = next_piece
#             next_piece = get_shape()
#             change_piece = False
#             clear_rows(grid, locked_positions)

#         draw_window(screen, grid)
#         pygame.display.update()

#         if check_lost(locked_positions):
#             run = False
#     pygame.display.quit()


# def draw_window(surface, grid):
#     surface.fill((0, 0, 0))
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             pygame.draw.rect(surface, grid[i][j],
#                              (top_left_x + j*block_size, top_left_y + i*block_size, block_size, block_size), 0)
#     pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)


# def create_grid(locked_positions={}):
#     grid = [[(0, 0, 0) for _ in range(grid_width)] for _ in range(grid_height)]
#     for i in range(len(grid)):
#         for j in range(len(grid[i])):
#             if (j, i) in locked_positions:
#                 grid[i][j] = locked_positions[(j, i)]
#     return grid

# def get_shape():
#     return Piece(5, 0, random.choice(shapes))

# font = pygame.font.SysFont('comicsans', 60)
# label = font.render('Tetris', 1, (255,255,255))

# if __name__ == '__main__':
#     main()


import pygame
import random

pygame.init()

# Set up the display
screen_width = 300
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption('Tetris')

# Define the grid size
grid_width = 10
grid_height = 20
block_size = 30  # Size of each block in pixels

# Define grid
grid = [[(0, 0, 0) for _ in range(grid_width)] for _ in range(grid_height)]

# Define dimensions of the playing area
play_width = grid_width * block_size
play_height = grid_height * block_size
top_left_x = (screen_width - play_width) // 2
top_left_y = screen_height - play_height

# Tetromino shapes
S = [['.....', '.....', '..OO.', '.OO..', '.....'], ['.....', '..O..', '..OO.', '...O.', '.....']]
Z = [['.....', '.....', '.OO..', '..OO.', '.....'], ['.....', '..O..', '.OO..', '.O...', '.....']]
I = [['.....', '.....', 'OOOO.', '.....', '.....'], ['..O..', '..O..', '..O..', '..O..', '.....']]
O = [['.....', '.....', '.OO..', '.OO..', '.....']]
J = [['.....', '.O...', '.OOO.', '.....', '.....'], ['.....', '..OO.', '..O..', '..O..', '.....'],
     ['.....', '.....', '.OOO.', '...O.', '.....'], ['.....', '..O..', '..O..', '.OO..', '.....']]
L = [['.....', '...O.', '.OOO.', '.....', '.....'], ['.....', '..O..', '..O..', '..OO.', '.....'],
     ['.....', '.....', '.OOO.', '.O...', '.....'], ['.....', '.OO..', '..O..', '..O..', '.....']]
T = [['.....', '..O..', '.OOO.', '.....', '.....'], ['.....', '..O..', '..OO.', '..O..', '.....'],
     ['.....', '.....', '.OOO.', '..O..', '.....'], ['.....', '..O..', '.OO..', '..O..', '.....']]

shapes = [S, Z, I, O, J, L, T]
colors = [(0, 255, 0), (255, 0, 0), (0, 255, 255), (255, 255, 0),
          (0, 0, 255), (255, 165, 0), (128, 0, 128)]  # Tetromino colors

class Piece(object):
    def __init__(self, x, y, shape):
        self.x = x
        self.y = y
        self.shape = shape
        self.color = random.choice(colors)  # Assign random color
        self.rotation = 0

def move_left(piece):
    piece.x -= 1

def move_right(piece):
    piece.x += 1

def move_down(piece):
    piece.y += 1

def rotate(piece):
    piece.rotation = (piece.rotation + 1) % len(piece.shape)

def valid_space(piece, grid):
    accepted_positions = [(x, y) for y in range(grid_height) for x in range(grid_width) if grid[y][x] == (0, 0, 0)]
    formatted = convert_shape_format(piece)
    for pos in formatted:
        if pos not in accepted_positions:
            if pos[1] > -1:  # Prevent piece from going above the grid
                return False
    return True

def convert_shape_format(piece):
    positions = []
    format = piece.shape[piece.rotation % len(piece.shape)]
    for i, line in enumerate(format):
        row = list(line)
        for j, column in enumerate(row):
            if column == 'O':
                positions.append((piece.x + j, piece.y + i))
    return positions

def clear_rows(grid, locked_positions):
    inc = 0
    for i in range(len(grid)-1, -1, -1):
        row = grid[i]
        if (0, 0, 0) not in row:  # Check if the row is full
            inc += 1
            ind = i
            for j in range(len(row)):
                try:
                    del locked_positions[(j, i)]
                except:
                    continue
    if inc > 0:  # Move the rows down
        for key in sorted(list(locked_positions), key=lambda x: x[1])[::-1]:
            x, y = key
            if y < ind:
                newKey = (x, y + inc)
                locked_positions[newKey] = locked_positions.pop(key)

def check_lost(positions):
    for pos in positions:
        x, y = pos
        if y < 1:  # If any piece is above the grid
            return True
    return False

def draw_window(surface, grid, score=0):
    surface.fill((0, 0, 0))
    # Draw grid
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            pygame.draw.rect(surface, grid[i][j],
                             (top_left_x + j * block_size, top_left_y + i * block_size, block_size, block_size), 0)

    # Draw border
    pygame.draw.rect(surface, (255, 0, 0), (top_left_x, top_left_y, play_width, play_height), 5)

    # Draw Score
    font = pygame.font.SysFont('comicsans', 30)
    score_label = font.render(f'Score: {score}', 1, (255, 255, 255))
    surface.blit(score_label, (top_left_x + 10, top_left_y + 10))

def create_grid(locked_positions={}):
    grid = [[(0, 0, 0) for _ in range(grid_width)] for _ in range(grid_height)]
    for i in range(len(grid)):
        for j in range(len(grid[i])):
            if (j, i) in locked_positions:
                grid[i][j] = locked_positions[(j, i)]
    return grid

def get_shape():
    return Piece(5, 0, random.choice(shapes))

def main():
    locked_positions = {}  # Store (x,y):(r,g,b)
    grid = create_grid(locked_positions)
    change_piece = False
    run = True
    current_piece = get_shape()
    next_piece = get_shape()
    clock = pygame.time.Clock()
    fall_time = 0
    score = 0

    while run:
        fall_speed = 0.27
        grid = create_grid(locked_positions)
        fall_time += clock.get_time()  # Updated to get_time()
        clock.tick(60)  # Set frame rate to 60 FPS

        if fall_time / 1000 > fall_speed:
            fall_time = 0
            move_down(current_piece)
            if not valid_space(current_piece, grid) and current_piece.y > 0:
                current_piece.y -= 1
                change_piece = True

        # User input handling
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                run = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    move_left(current_piece)
                    if not valid_space(current_piece, grid):
                        current_piece.x += 1  # Undo movement
                elif event.key == pygame.K_RIGHT:
                    move_right(current_piece)
                    if not valid_space(current_piece, grid):
                        current_piece.x -= 1  # Undo movement
                elif event.key == pygame.K_DOWN:
                    move_down(current_piece)
                    if not valid_space(current_piece, grid):
                        current_piece.y -= 1  # Undo movement
                elif event.key == pygame.K_UP:
                    rotate(current_piece)
                    if not valid_space(current_piece, grid):
                        current_piece.rotation -= 1  # Undo rotation

        shape_pos = convert_shape_format(current_piece)

        for i in range(len(shape_pos)):
            x, y = shape_pos[i]
            if y > -1:  # Only draw pieces that are on the screen
                grid[y][x] = current_piece.color

        if change_piece:
            for pos in shape_pos:
                p = (pos[0], pos[1])
                locked_positions[p] = current_piece.color
            current_piece = next_piece
            next_piece = get_shape()
            change_piece = False
            clear_rows(grid, locked_positions)

        draw_window(screen, grid, score)
        pygame.display.update()

        if check_lost(locked_positions):
            run = False

    pygame.quit()

if __name__ == "__main__":
    main()


#Things to look at:
#no borders on tiles
#no score
#no level speed increase
#no end condition
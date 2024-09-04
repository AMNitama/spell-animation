'''
practice/improvement using object orientation.
'''


import pygame

pygame.init()

WIDTH, HEIGHT = 800,800
ROWS, COLUMNS = 16, 16

TILE_SIZE = WIDTH//COLUMNS
clock = pygame.time.Clock()
FPS = 60

color = {
    "white" : (255,255,255),
    "black" : (0,0,0),
    "green" : (0,255,0),
    "red" : (255,0,0),
    "blue" : (0,0,255),
    "grey": (137,137,137)
}

screen = pygame.display.set_mode((WIDTH,HEIGHT)) # creates actual game environment
pygame.display.set_caption('Board Test') # application name/ hover caption

class Character():
    def __init__(self, x, y, color, movement_range=3):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE) # parameters of character's invisible box 
        self.color = color
        self.movement_range = movement_range
        self.selected = False
        self.dragging = False
        self.valid_move_cache = [] # cache valid moves
        self.selected_posX,self.selected_posY = x//TILE_SIZE, y//TILE_SIZE
        
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)
        if self.selected:
            pygame.draw.rect(screen, color["green"], self.rect,2)


    def update_position(self, pos):
        self.rect.x = pos[0] - TILE_SIZE//2
        self.rect.y = pos[1] - TILE_SIZE//2


    def snap_to_grid(self):
        # getting nearest grid position based on the location of the center of the square        
        grid_col = self.rect.centerx // TILE_SIZE
        grid_row = self.rect.centery // TILE_SIZE
        self.rect.x = grid_col * TILE_SIZE
        self.rect.y = grid_row * TILE_SIZE

    def calculate_valid_moves(self, board):
        # Get the character's current grid position
        current_col = self.rect.centerx // TILE_SIZE
        current_row = self.rect.centery // TILE_SIZE
        
        # Initialize a list to store valid moves
        valid = []

        # Reset all tiles to be invalid initially
        for row in board:
            for tile in row:
                tile.move_valid = False

        # Check each possible move within the movement range
        for dr in range(-self.movement_range, self.movement_range + 1):
            for dc in range(-self.movement_range, self.movement_range + 1):
                # Calculate the target row and column
                new_row = current_row + dr
                new_col = current_col + dc

                # Use Manhattan distance to limit movement
                if abs(dr) + abs(dc) <= self.movement_range:
                    # Ensure the move is within the board boundaries
                    if 0 <= new_row < ROWS and 0 <= new_col < COLUMNS: 
                        board[new_row][new_col].valid_move()  # set tile to be a valid move
                        valid.append((new_row, new_col))

        self.valid_move_cache = valid
        self.selected_posX, self.selected_posY = current_col, current_row


    def is_valid_move(self):
        # Validate the current position of the character
        grid_col = self.rect.centerx // TILE_SIZE
        grid_row = self.rect.centery // TILE_SIZE

        # Check if the current position is in the cache of valid moves
        if (grid_row, grid_col) not in self.valid_move_cache:
            # Snap back to the original position if the move is invalid
            self.rect.x = self.selected_posX * TILE_SIZE
            self.rect.y = self.selected_posY * TILE_SIZE
                    


class Tile():
    def __init__(self, row, col, size, color):
        self.row = row  # Row position on the grid
        self.col = col  # Column position on the grid
        self.size = size  # Size of the tile
        self.color = color  # Color of the tile
        self.rect = pygame.Rect(col * size, row * size, size, size)  # Pygame rectangle for the tile
        self.move_valid = False

    def valid_move(self):
        self.move_valid = True
 
    def draw(self, screen):
        # Draw the tile on the screen
        pygame.draw.rect(screen, self.color, self.rect)

    def highlight(self, screen, highlight_color, boarder_thickness=2):
        # Highlight the tile with a given color
            pygame.draw.rect(screen, highlight_color, self.rect, boarder_thickness)


    def contains_point(self, x, y):
        # Check if a point (x, y) is within the tile's rectangle
        return self.rect.collidepoint(x, y)
    


def createBoard():
    # Create a board as a list of Tile objects
    board = []
    for row in range(ROWS):
        board_row = []
        for col in range(COLUMNS):
            # Initialize each tile with its row, column, size, and base color
            tile = Tile(row, col, TILE_SIZE, color["white"])

            board_row.append(tile)
        board.append(board_row)
    return board



def draw_board(board, character):
    # Draw the game board
    for row in range(ROWS):
        for col in range(COLUMNS):
            tile = board[row][col]

            # Draw each tile
            tile.draw(screen)
            tile.highlight(screen, color["grey"], 1)

            # Highlight the valid move tiles if the character is selected
            if character.selected and (row,col) in character.valid_move_cache:
                tile.highlight(screen, color["green"])
            # else:
            #     tile.highlight(screen, color["red"])


character = Character(0,0, color["blue"], movement_range=3)
board = createBoard()


while True:
    screen.fill(color["black"])  # Clear the screen with a black background

    draw_board(board, character)  # Draw the game board with character's move range highlighted
    character.draw()  # Draw the character

    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if character.rect.collidepoint(event.pos):
                character.selected = True
                character.dragging = True
                character.calculate_valid_moves(board)
            else:
                character.selected = False  # Deselect the character if clicked elsewhere

        elif event.type == pygame.MOUSEBUTTONUP:
            if character.dragging:
                character.dragging = False
                character.is_valid_move()
                character.snap_to_grid()  # Snap character to the nearest tile

        elif event.type == pygame.MOUSEMOTION:
            if character.dragging:
                character.update_position(event.pos)

    pygame.display.flip()
    clock.tick(FPS)
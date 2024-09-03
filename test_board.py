'''
Making a board for the game similar to Fire Emblem's system
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

    def valid_moves(self):
        # Get the character's current grid position
        current_col = self.rect.centerx // TILE_SIZE
        current_row = self.rect.centery // TILE_SIZE
        
        # Initialize a list to store valid moves
        valid = []

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
                        valid.append((new_row, new_col))

        return valid
    
    #def click_on_grid(self):




def createBoard():
    # for each horizontal row, look at the column's index, and create a tile
    # this tile object within a dictionary is then added to the board row, after the row is finished it is then added to the full board
    # board = [board_row_1, board_row_2, etc] , board_row = [[tile_1, color], [tile_2, color ], etc]
    # pygame.Rect is a class to create an actual rectangle object class
    board = []
    for row in range(ROWS):
        board_row = []
        for col in range(COLUMNS):
            board_row.append({
                "tile": pygame.Rect(col * TILE_SIZE, row * TILE_SIZE, TILE_SIZE, TILE_SIZE), # create a rectangle in posX, posY, width, height
                "color" : color["white"]
            })
        board.append(board_row)
        print(board_row)

    print(board)
    return board



def draw_board(board, character):
    for row in range(ROWS):
        for col in range(COLUMNS):
            tile_rect = board[row][col]["tile"]
            base_color = board[row][col]["color"]

            pygame.draw.rect(screen, base_color,tile_rect)
            # pygame.draw.rect(screen, color["grey"], tile_rect, 2)
            pygame.draw.rect(screen, color["black"], tile_rect, 1)

            if character.selected:
                valid_tiles = character.valid_moves()
                for (r,c) in valid_tiles:
                    if (r,c) == (row, col):
                        pygame.draw.rect(screen, color["green"], tile_rect, 2)
            
            

character = Character(0,0, color["blue"], movement_range=3)
board = createBoard()



while True:
    screen.fill(color["black"])
    # valid_tiles = valid_moves(character)

    # draw_board(board, valid_tiles)
    draw_board(board, character)
    character.draw()
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if character.rect.collidepoint(event.pos):
                character.selected = True
                character.dragging = True
            
            elif character.selected == True and character.valid_moves:
                character.update_position(event.pos)
                character.snap_to_grid
            
            else:
                character.selected = False # deselect if clicked elsewhere

            

        elif event.type == pygame.MOUSEBUTTONUP:
            character.dragging = False
            character.snap_to_grid()

        elif event.type == pygame.MOUSEMOTION:
            if character.dragging:
                character.update_position(event.pos)
                print(event.pos)

    pygame.display.flip()
    clock.tick(FPS)
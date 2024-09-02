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
    def __init__(self, x, y):
        self.rect = pygame.Rect(x, y, TILE_SIZE, TILE_SIZE) # parameters of character's invisible box 
        self.color = color["blue"]
        self.dragging = False
    
    def draw(self):
        pygame.draw.rect(screen, self.color, self.rect)

    def update_position(self, pos):
        self.rect.x = pos[0] - TILE_SIZE//2
        self.rect.y = pos[1] - TILE_SIZE//2

    def snap_to_grid(self):
        # getting nearest grid position based on the location of the center of the square
        grid_col = self.rect.centerx // TILE_SIZE
        grid_row = self.rect.centery // TILE_SIZE
        self.rect.x = grid_col * TILE_SIZE
        self.rect.y = grid_row * TILE_SIZE


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


# # Check Valid Moves (dummy implementation)
# def valid_moves(character):
#     # Here you can implement your logic to determine valid tiles
#     # For now, just make the surrounding tiles valid (as an example)
#     valid = []
#     for row in range(ROWS):
#         for col in range(COLUMNS):
#             if abs(character.rect.x // TILE_SIZE - col) <= 1 and abs(character.rect.y // TILE_SIZE - row) <= 1:
#                 valid.append((row, col))
#     return valid


# def draw_board(board, valid_moves):
#     for row in range(ROWS):
#         for col in range(COLUMNS):
#             tile_rect = board[row][col]["tile"]
#             base_color = board[row][col]["color"]

#             pygame.draw.rect(screen, base_color,tile_rect)
            
#             pygame.draw.rect(screen, color["grey"], tile_rect, 2)
#             if (row,col) in valid_moves:
#                 pygame.draw.rect (screen, color["green"], tile_rect, 2)

def draw_board(board):
    for row in range(ROWS):
        for col in range(COLUMNS):
            tile_rect = board[row][col]["tile"]
            base_color = board[row][col]["color"]

            pygame.draw.rect(screen, base_color,tile_rect)
            
            pygame.draw.rect(screen, color["grey"], tile_rect, 2)
            

character = Character(0,0)
board = createBoard()

while True:
    screen.fill(color["black"])
    # valid_tiles = valid_moves(character)

    # draw_board(board, valid_tiles)
    draw_board(board)
    character.draw()
    
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if character.rect.collidepoint(event.pos):
                character.dragging = True

        elif event.type == pygame.MOUSEBUTTONUP:
            character.dragging = False
            character.snap_to_grid()

        elif event.type == pygame.MOUSEMOTION:
            if character.dragging:
                character.update_position(event.pos)
                print(event.pos)

    pygame.display.flip()
    clock.tick(FPS)
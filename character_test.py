import pygame
import random
import load_assets as pic

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


class Hero(pygame.sprite.Sprite):
    def __init__(self, hero_profession, pos_x, pos_y, level=1):
        super().__init__()
        self.hero_profession = hero_profession
        self.name = self.generate_name(hero_profession)
        self.level = level
        self.base_stats = self.initialize_stats()
        self.apply_profession_stat_bonus()

        self.image = pygame.Surface((TILE_SIZE, TILE_SIZE))  # Placeholder: Create a plain surface
        self.image.fill(color['green'])  # Just color it green for now
        self.rect = self.image.get_rect()
        self.rect.x = pos_x
        self.rect.y = pos_y

    

    def generate_name(self, hero_profession):
        gender = random.choice(["male", "female"])
        first_name = random.choice(hero_profession.first_names[gender])
        last_name = random.choice(hero_profession.last_names)
        return f"{first_name} {last_name}"
    

    def initialize_stats(self):
        base_stats = {
            "strength" : 5,
            "agility" : 5,
            "constitution": 5,
            "intelligence" : 5,
            "mind": 5,
            "social": 0.5,
            "luck" : 0.05
        }
        base_stats["health"] = 2 * base_stats["constitution"]
        base_stats["mana"] = 4 * base_stats["mind"]
        return base_stats
    
    def apply_profession_stat_bonus(self):
        for stat, bonus in self.hero_profession.stat_bonus.items():
            if stat in self.base_stats:
                self.base_stats[stat] += bonus



class Farmer:
    def __init__(self):
        self.first_names = {
            "male": ["Erin", "Alden", "Cedric", "Heward", "Farlan", "Garrin", 'Barlow', 'Sam'],
            "female": ["Arla", "Cerys", "Mira", "Mable", "Audrey", "Rose", "Bianca", "Riley"]
        }
        self.last_names = ["Bellow", "Fairford", "Woodman", "Smith", "Black", "Atwood", "Merryfield"]
        self.stat_bonus = {
            "social" : 0.15,
            "luck" : 0.03
        }



farmer_profession = Farmer()
hero1 = Hero(farmer_profession, WIDTH//2, HEIGHT//2)

print(f"Hero Name: {hero1.name}")
print(f"Hero Stats: {hero1.base_stats}")

all_sprites = pygame.sprite.Group()
all_sprites.add(hero1)

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
    
    screen.fill(color["white"])
    all_sprites.update()
    all_sprites.draw(screen)
    



    pygame.display.flip()
    clock.tick(FPS)
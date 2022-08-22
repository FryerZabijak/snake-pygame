from random import randint, random
import pygame
from food import Food
from player import Snake
from window import width, height, FPS, size, BACKGROUND_COLOR, TEXT_COLOR, snake_color

# Inicializace Pygamu
pygame.init()
screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

# Nastavení začátku hada do středudd
snake_starting_positions = [{"x": round(width//2/size)*size, "y": round(width//2/size)*size},
                            {"x": round(width//2/size)*size,
                             "y": round(width//2/size)*size+size},
                            {"x": round(width//2/size)*size, "y": round(width//2/size)*size+size+size}]

# Vytvoření třídy had pro hráče
player = Snake(0, -size, snake_color, snake_starting_positions, screen)

# Vytvoření třídy pro jídlo s náhodným generováním pozice
food = Food(screen, None, None, player)
foods = [food]

# Deklarované a inicializované skóre na nulu
score = 0

# Nastavení fontu, poté vytvoření zprávy a vyrenderované na objekt
system_font = pygame.font.SysFont("Montserrat", 64)
score_text = system_font.render(f"Skóre: {score}", True, TEXT_COLOR)
score_text_rect = score_text.get_rect()
score_text_rect.topleft = (0, 0)

# Proměnná, která uvádí, jestli hra jede je na True
game_running = True

# Cyklus celé hry
while game_running:
    # Pokud se klikne na křížek, tak se okno zavře (Jinak by se hra dala vypnout např. přes správce úloh)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_running = False

    # Pokud je stisknutá nějaké klávesa
    if pygame.KEYDOWN:
        # Stisknuté klávesy se uloží do proměnné "keys"
        keys = pygame.key.get_pressed()
        # Jestli se zmáčkne "W" a zároveň hráč nejede směrem "nahoru", tak se nastaví aby tudma jel
        if (keys[pygame.K_w] and player.speedY != size):
            player.speedX = 0
            player.speedY = -size
        # Jestli se zmáčkne "A" a zároveň hráč nejede směrem "doleva", tak se nastaví aby tudma jel
        elif (keys[pygame.K_a] and player.speedX != size):
            player.speedX = -size
            player.speedY = -0
        # Jestli se zmáčkne "S" a zároveň hráč nejede směrem "doprava", tak se nastaví aby tudma jel
        elif (keys[pygame.K_s] and player.speedY != -size):
            player.speedX = 0
            player.speedY = size
        # Jestli se zmáčkne "D" a zároveň hráč nejede směrem "dolů", tak se nastaví aby tudma jel
        elif (keys[pygame.K_d] and player.speedX != -size):
            player.speedX = size
            player.speedY = 0

        # Jestliže následujícím tahem, hráč dopadne na jídlo (na 100%), tak se zvětší o jeden bod a přibude mu skóre
        # plus se aktualizuje text
        new_foods = []
        for f in foods:
            if f.CheckEat():
                f = Food(screen, None, None, player)
                player.trace.append({"x": food.x, "y": food.y})
                score += 10
                score_text = system_font.render(
                    f"Skóre: {score}", True, TEXT_COLOR)
                new_food = Food(screen, None, None, player)
                if randint(0, 4) == 0 and len(foods):
                    new_foods.append(new_food)
                    FPS += 2
            new_foods.append(f)
        foods = new_foods

        # Pohyb hráče ve směru
        player.Move()

    # Zjistí-li, že je hráč mrtvý "game_running" se přepne na false (tzn. konec hry)
    if player.CheckDeath():
        game_running = False

    # Kreslení - začíná se pozadí, poté hadem, jídlem a textem
    screen.fill(BACKGROUND_COLOR)
    player.DrawSnake()
    for f in foods:
        f.DrawFood()

    screen.blit(score_text, score_text_rect)
    pygame.display.update()
    # Hard-Locknuté FPS (Jinak by cyklus probíhal v závislosti na rychlosti počítače)
    clock.tick(FPS)

# Konec
pygame.quit()

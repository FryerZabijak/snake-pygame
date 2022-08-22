# Konfigurační proměnné
# Lze je možné cokoliv změnit a přizpůsobit si hru
width = 1000
height = 800
FPS = 15
size = 27

while width%size!=0:
    size = round(size)
    size-=1

BACKGROUND_COLOR = "#111111"
TEXT_COLOR = "#ffffff"
snake_color = (144, 144, 0)
food_color = (255, 48, 64)

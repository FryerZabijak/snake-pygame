# Konfigurační proměnné
## Lze je možné cokoliv změnit a přizpůsobit si hru

### Šířka okna v pixelech
width = 1000

### Výška okna v pixelech
height = 800

### FPS - rychlost hry
FPS = 15

### Základní rozměr hry (čím větší tím větší objekty)
size = 25

## Barvy
### Barva pozadí
BACKGROUND_COLOR = "#222222"

### Barva textu
TEXT_COLOR = "#ffffff"

### Barva hada
snake_color = "#aaaa00"

### Barva jídla
food_color = "#aa0000"

## Úpravy potřebné k zabránění chybám
while width % size != 0:
    size = round(size)
    size -= 1

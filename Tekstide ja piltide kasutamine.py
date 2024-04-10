import pygame
import sys

# Initsialiseerime Pygame'i
pygame.init()

# Määrame ekraani suuruse
screen_width = 640
screen_height = 480
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Ülesanne 1")

# Laeme pildid ja muudame nende suurust
background = pygame.transform.scale(pygame.image.load('bgshop.jpg'), (screen_width, screen_height))  # Taustapildi laadimine ja suuruse muutmine
seller = pygame.transform.scale(pygame.image.load('seller.png'), (280, 350))  # Poemüüja pildi laadimine ja suuruse muutmine
chat_bubble = pygame.transform.scale(pygame.image.load('chat.png'), (250, 150))  # Jutumulli pildi laadimine ja suuruse muutmine

# Teksti loomine
font = pygame.font.Font(None, 24)  # Fondi määramine teksti jaoks
text_surface = font.render("Tere, minu nimi on Oskar", True, (255, 255, 255))  # Teksti loomine valge värviga

# Mängu tsükkel
running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    # Tausta ja müüja joonistamine
    screen.blit(background, (0, 0))  # Taustapildi joonistamine ekraanile alguspunkti (0, 0)
    screen.blit(seller, (75, 100))  # Poemüüja pildi joonistamine ekraanile koordinaatidele (75, 100)

    # Jutumulli joonistamine
    screen.blit(chat_bubble, (250, 75))  # Jutumulli pildi joonistamine ekraanile koordinaatidele (250, 75)
    screen.blit(text_surface, (270, 125))  # Teksti joonistamine jutumulli sisse alguspunkti (270, 125)

    # Ekraani värskendamine
    pygame.display.flip()

# Pygame'i lõpetamine
pygame.quit()
sys.exit()

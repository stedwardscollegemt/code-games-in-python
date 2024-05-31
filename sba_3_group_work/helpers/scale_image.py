import pygame

# ---- initialize Pygame and scale images -------------------
pygame.init()

# Load the image using Pygame and scale it
original_grapes_image = pygame.image.load("sba_3_group_work/images/banana.png")
scaled_grapes_image = pygame.transform.scale(original_grapes_image, (50, 50))  # Scale to 50x50 pixels

# Save the scaled image so Pygame Zero can use it
pygame.image.save(scaled_grapes_image, "sba_3_group_work/images/scaled_banana.png")
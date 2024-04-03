import pygame
import sys

pygame.init()

WIDTH, HEIGHT = 800, 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Tower of Hanoi")

# Colors
Dark_Brown = (100, 50, 10)
LIGHT_Brown= (222, 184, 135)
# Tower of Hanoi function
def hanoi(n, i, j, k):
    if n > 0:
        hanoi(n - 1, i, k, j)
        move_disk(i, j)
        draw_towers()
        draw_disks()
        pygame.display.flip()
        pygame.time.wait(500)  
        hanoi(n - 1, k, j, i)

# Move disk from tower i to tower j
def move_disk(i, j):
    disk = towers[i].pop()
    towers[j].append(disk)

def draw_towers():
    background_image = pygame.image.load(r'C:\Users\User\Desktop\hanoi\back.png')
    background_image = pygame.transform.scale(background_image, (800, 600))  # Resize the image to match the screen size

    screen.blit(background_image, (0, 0))
    for i in range(3):
        pygame.draw.rect(screen, Dark_Brown, (150 + i * 250, 200, 10, 200))


DISK_COLORS = [ (139, 69, 19), (160, 82, 45), (205, 133, 63)] 

def draw_disks():
    for i in range(len(towers)):
        for j in range(len(towers[i])):
            disk_width = towers[i][j] * 30
            disk_height = 20
            x = 150 + i * 250 - disk_width // 2 + 5
            y = 370 - j * 30
            color_index = (i + j) % len(DISK_COLORS)  # Alternate colors based on tower and disk level
            pygame.draw.rect(screen, DISK_COLORS[color_index], (x, y, disk_width, disk_height))


def get_input():
    pygame.init()
    screen = pygame.display.set_mode((800, 600))
    font = pygame.font.Font(None, 32)
    input_value = ""
    input_rect = pygame.Rect(300, 190, 200, 50)
    color_inactive = pygame.Color(188, 143, 143)  
    color_active = pygame.Color(139, 69, 19)      
    color = color_inactive
    active = False

    background_image = pygame.image.load(r'C:\Users\User\Desktop\hanoi\images.png')
    background_image = pygame.transform.scale(background_image, (800, 600))  

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if input_rect.collidepoint(event.pos):
                    active = not active
                else:
                    active = False
                color = color_active if active else color_inactive
            if event.type == pygame.KEYDOWN:
                if active:
                    if event.key == pygame.K_RETURN:
                        return int(input_value)
                    elif event.key == pygame.K_BACKSPACE:
                        input_value = input_value[:-1]
                    else:
                        input_value += event.unicode

        # Blit the background image onto the screen
        screen.blit(background_image, (0, 0))

        pygame.draw.rect(screen, color, input_rect, 2)  # Draw the input box

      
        text_surface = font.render("Please Enter Number Of Disks:", True, pygame.Color('white'))
        screen.blit(text_surface, (250, 137))

        txt_surface = font.render(input_value, True, pygame.Color('white'))  # Render the input text
        screen.blit(txt_surface, (input_rect.x + 60, input_rect.y + 5))

        text_surface_below = font.render("Press Enter To Continue", True, pygame.Color(139, 69, 19))  # Saddle brown
        screen.blit(text_surface_below, (265, 270))

        pygame.display.flip()


def main():
    global towers
    n = get_input()
    towers = [list(range(n, 0, -1)), [], []]  # Initial configuration
    i = 0  # Source tower
    j = 2  # Target tower
    k = 1  # Auxiliary tower

    draw_towers()
    draw_disks()
    pygame.display.flip()
    hanoi(n, i, j, k)

    # Pygame event loop
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

if __name__ == '__main__':
    main()

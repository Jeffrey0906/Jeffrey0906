import pygame
import sys
import math
import random

pygame.init()  # Initialize the Pygame class
screen = pygame.display.set_mode((600, 600))  # Set window size
pygame.display.set_caption('Wheel of Fortune')  # Set window title
tick = pygame.time.Clock()
fps = 10  # Set refresh rate, the larger the number, the higher the refresh rate
picture = pygame.transform.scale(pygame.image.load("./Wheel of fortune.png"), (600, 600))
bg = picture.convert()
picture = pygame.transform.scale(pygame.image.load("./1.png"), (30, 230))
hand = picture.convert_alpha()


rewardDict = {
    'Star prize': (0, 0.03),
    'Second level (Second prize or First prize': (0.03, 0.2),
    'Third level (Consolation prize or Third prize)': (0.2, 1)
}


def reward_fun():
    """
    Determines the prize level won by the user in the lucky wheel game.

    This function generates a random number between 0 and 1 and compares it
    with predefined prize level ranges in the `rewardDict` dictionary.
    It returns the prize level key as a string based on where the generated
    number falls within these ranges.

    Returns:
        str: A key from `rewardDict` indicating the prize level won.
    """

    # Generate a random number between 0 and 1
    number = random.random()
    # Determine the prize tier of the random wheel
    for k, v in rewardDict.items():
        if v[0] <= number < v[1]:
            return k


def start():
    """
    Initiates the lucky wheel game display.

    This function sets up the initial game screen. It loads and displays
    the background and the wheel hand. It also waits for the user to press
    space key to start spinning the wheel or click to quit.

    The function runs in a loop that checks for quit events or key presses
    and updates the screen accordingly.
    """

    while True:
        for event in pygame.event.get():

            # Handle quit event
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    sys.exit()
                else:
                    return

        screen.blit(bg, (0, 0))
        new_rect = hand.get_rect(center=(300, 150))
        screen.blit(hand, new_rect)

        pygame.draw.circle(screen, (255, 255, 0), (300, 300), 50)

        text_font = pygame.font.Font("./font.ttf", 80)
        text_surface = text_font.render("go", True, (110, 55, 155))
        screen.blit(text_surface, (250, 255))
        pygame.display.update()


def middle():
    """
    Handles the spinning of the lucky wheel.

    The function calculates and updates the rotation of the wheel hand.
    It increments the angle of rotation in each loop, simulating the spinning
    of the wheel. Once the angle exceeds a certain limit (indicating the
    wheel has spun enough), it calls the `end` function with the prize level
    determined by `rewardFun`.

    The loop checks for quit events and updates the screen display with
    the rotating hand.
    """

    angle = 0
    while True:
        posx = 300 + int(150 * math.sin(angle * math.pi / 180))
        posy = 300 - int(150 * math.cos(angle * math.pi / 180))
        print(posx, posy, math.sin(angle * math.pi / 180))

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
        screen.blit(bg, (0, 0))

        new_hand = pygame.transform.rotate(hand, -angle)

        new_rect = new_hand.get_rect(center=(posx, posy))
        screen.blit(new_hand, new_rect)
        pygame.draw.circle(screen, (255, 255, 0), (300, 300), 50)

        angle += 10

        if angle > 500:
            k = reward_fun()
            end(k)
            break

        tick.tick(fps)
        pygame.display.flip()  # Refresh the window


def end(k):
    """
    Displays the prize won by the user at the end of the lucky wheel game.

    Args:
        k (str): A string indicating the prize level won by the user,
                 as returned by the `rewardFun` function.

    The function updates the game screen to show a message with the prize
    level won. It changes the background and renders the prize text.
    """

    text_font = pygame.font.Font("./font.ttf", 50)
    print("Congratulations, you have drawn " + k)
    text_surface = text_font.render("Your award is: %s" % k, True, (110, 55, 155))
    screen.fill((155, 155, 0))
    screen.blit(text_surface, (30, 230))


if __name__ == '__main__':
    start()
    middle()

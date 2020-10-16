import pygame
import time
import random


class SortVisualizer:
    # Colors
    WHITE = (255, 255, 255)
    BLACK = (0, 0, 0)

    def __init__(self, width, height, delay=0.05):
        self.width = width
        self.height = height
        self.arr = []
        self.visualize = False
        self.speed = delay

    """
    Start the program
        Call this function after creating an instance of the class
        to create the window and start the program
    """
    def start(self):
        pygame.init()
        pygame.font.init()
        pygame.display.set_caption('Sorting Visualizer')
        self.screen = pygame.display.set_mode((self.width, self.height))
        self.screen.fill(self.WHITE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.font_num = pygame.font.SysFont('Arial', 15)

        self.generate_array(20)
        self.draw_array()

        # Main loop
        while self.running:
            # Pygame events
            self.check_events()

            # Visualize mode
            if self.visualize == True:
                # Bubble Sort
                for i in range(len(self.arr)):
                    already_sorted = True
                    for j in range(len(self.arr) - i -1):
                        if self.arr[j] > self.arr[j + 1]:
                            self.arr[j], self.arr[j + 1] = self.arr[j + 1], self.arr[j] # Swap adjacent elements
                            already_sorted = False

                            time.sleep(self.speed)
                            self.draw_array()
                    if already_sorted:
                        break

                # Done visualizing
                self.visualize = False
                self.draw_array()

            # Update
            pygame.display.update()
            self.clock.tick(60)

        self.quit()

    """
    Quit the program
        This is a separate function in case there is a need to perform
        certain operations when quitting
    """
    def quit(self):
        pygame.quit()

    """
    Check for pygame events
    """
    def check_events(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    self.running = False
                if event.key == pygame.K_RETURN:
                    self.visualize = True
                    self.clear_screen()

    """
    Clear the screen
        This is a separate function in case there is a need to perform
        certain operations when clearing the screen
    """
    def clear_screen(self):
        self.screen.fill(self.WHITE)

    """
    Generate random numbers for the array to sort
        Optional parameters:
            min: Minimum number (default: 1)
            max: Maximum number (default: 100)
    """
    def generate_array(self, length, min=1, max=100):
        for i in range(length):
            self.arr.append(random.randint(min, max))

    """
    Draw the current array to the screen, represented by bars
    """     
    def draw_array(self):
        self.clear_screen()
        heightModifier = self.height / 150  # How much to multiply the number of the bar for the height by
        width = self.width * 0.03125  # The width of each bar
        currOffsetX = 0  # The current x offset, to keep track when drawing the next bar
        spacingX = self.width * 0.00375  # The spacing of each bar from its neighbor
        for num in self.arr:
            pygame.draw.rect(self.screen, self.BLACK, (currOffsetX, 0, width, num * heightModifier))
            currOffsetX += width + spacingX
            # Add text if the screen is big enough
            if self.width > 400 and self.height > 400:
                textsurf = self.font_num.render(str(num), True, (255, 255, 255), (0, 0, 0))
                self.screen.blit(textsurf, (currOffsetX - (self.width * 0.02875), 0))
        pygame.display.update()

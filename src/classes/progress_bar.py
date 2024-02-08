import pygame

class ProgressBar(pygame.sprite.Sprite):
    def __init__(self, x, y, width, height, background_image, testtube_image):
        super().__init__()

        # constants (work as and on a the initial screen size)
        self.x = x
        self.y = y

        self.width = width
        self.height = height
        
        # other vars
        self.background = pygame.Surface((width, height))
        self.background.fill(background_image)

        self.testtube = pygame.Surface((self.width*0.35, self.height*0.95))
        self.testtube.fill(testtube_image)

        self.update_progress_bar(0.0)


    def update_progress_bar(self, progress):
        # draw testtube
        self.background.blit(self.testtube, self.testtube.get_rect(topleft=(int(self.x+self.width*0.5), self.height*0.025)))

        # calculate the bar height and draw it
        bar_height = self.height*0.1 + progress*self.height*0.8
        pygame.draw.rect(self.background, (50, 175, 10), (int(self.x + self.width*0.525), self.height*0.9 - bar_height, self.width*0.3, bar_height))

        self.image = self.background
        self.rect = self.image.get_rect(topleft=(self.x, self.y))


    def update(self, Iwidth:int, Iheight:int, Cwidth:int, Cheight:int, *args, **kwargs):
        #progress bar updaten
        for key, value in kwargs.items():
            if key == 'progress':
                self.update_progress_bar(value)

        #Objekt skalieren
        x_factor = Cwidth/Iwidth
        y_factor = Cheight/Iheight

        self.image = pygame.transform.scale(self.image, (self.width * x_factor, self.height * y_factor))
        self.rect = self.image.get_rect(topleft=(self.x * x_factor, self.y * y_factor))

    def add_progress(self, amount: int) -> None:
        if (self.height + amount) < 5:
            amount = -self.height + 5
        self.y -= amount
        self.height += amount

    def set_progress(self, progress: int) -> None:
        if progress < 5:
            progress = 5
        self.y += (self.height - progress)
        self.height = progress
        
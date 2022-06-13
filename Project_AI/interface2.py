import webbrowser

import pygame
import Hard
import Easy
import Medium
import Human

def help():
    webbrowser.open('https://en.wikipedia.org/wiki/Chinese_checkers')

def window2():
    color_hover = (202, 203, 213)
    # dark shade of the button
    color_Normal = (160, 0, 0) # color of button
    pygame.init()  # initialize all imported pygame modules
    (width, height) = (1000, 780)
    window = pygame.display.set_mode((width, height))  # window size
    image = pygame.image.load("background.png")  # background image
    # image = image.convert()
    smallfont = pygame.font.Font('palamecia titling.ttf', 70)
    text = smallfont.render('CHOOSE lEVEL TO START', True, (200,0,0))
    textRect = text.get_rect()
    textRect.center = (500, 70)
    """def quit():
        window.distroy()"""

    #button
    def text_objects(text,font):
        textsurface =font.render(text,True , (0,0,0))
        return textsurface , textsurface.get_rect()

    def button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(window, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(window, ic, (x, y, w, h))

        smallText = pygame.font.Font('palamecia titling.ttf', 30)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        window.blit(textSurf, textRect)
    running= True
    while running:
      events = pygame.event.get()
      window.blit(pygame.transform.scale(image, (700, 700)), (130, 100))
      window.blit(text,textRect)
      for event in pygame.event.get():
        if event.type == pygame.QUIT:
          running= False
      button("Easy", 410, 430, 120, 30, color_Normal, color_hover, Easy.Easy)
      button("Medium", 410, 380, 120, 30, color_Normal, color_hover, Medium.Medium)
      button("Hard", 410, 330, 120, 30, color_Normal, color_hover, Hard.Hard)

      button("2 players", 400, 500, 150, 50, color_Normal, color_hover, Human.Human)

      button("Quit", 850, 670, 100, 50, color_Normal, color_hover, quit)
      button("Help", 50, 670, 100, 50, color_Normal, color_hover, help)

      rect2 = pygame.draw.rect(window, color_Normal, pygame.Rect(844, 664, 112, 62), 6, 20)
      rect3 = pygame.draw.rect(window, color_Normal, pygame.Rect(44, 664, 112, 62), 6, 20)

      rect4 = pygame.draw.rect(window, color_Normal, pygame.Rect(404, 424, 132, 42), 6, 20)
      rect5 = pygame.draw.rect(window, color_Normal, pygame.Rect(404, 374, 132, 42), 6, 20)
      rect6 = pygame.draw.rect(window, color_Normal, pygame.Rect(404, 324, 132, 42), 6, 20)
      rect7 = pygame.draw.rect(window, color_Normal, pygame.Rect(394, 494, 162, 62), 6, 20)
      pygame.display.update()
      pygame.display.flip()

    pygame.quit()


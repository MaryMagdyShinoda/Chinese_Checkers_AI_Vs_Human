import pygame
import interface2
import webbrowser

def help():
    webbrowser.open('https://en.wikipedia.org/wiki/Chinese_checkers')

def window1():
    color_hover = (202, 203, 213)

    color_Normal = (160, 0, 0) # color of button
    pygame.init() #initialize all imported pygame modules
    (width, height) = (1000, 780)
    window =pygame.display.set_mode((width, height)) #window size

    image = pygame.image.load("background.png") #background image
   # image = image.convert()
    smallfont1 = pygame.font.Font('palamecia titling.ttf', 100)
    text1 = smallfont1.render('CHINESE CHECKERS', True, (200,0,0))
    textRect1 = text1.get_rect() #manipulate as rectangle
    textRect1.center = (500, 70)

    #button
    def quit():
        window.distroy()

    #specify the color and manipulate it as rectangle
    def text_objects(text,font):
        textsurface = font.render(text,True , (0,0,0))
        return textsurface , textsurface.get_rect()


        
    def button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos() #get mouse position
        click = pygame.mouse.get_pressed() #get click press from user
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

    running = True
    while running:
        window.blit(pygame.transform.scale(image, (700, 700)), (130, 100))
        window.blit(text1, textRect1)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        button("Play Game", 360, 405, 230, 62, color_Normal, color_hover, interface2.window2)
        button("Quit", 850, 670, 100, 50, color_Normal, color_hover, quit)
        button("Help", 50, 670, 100, 50, color_Normal, color_hover, help)

        Playrect = pygame.draw.rect(window, color_Normal, pygame.Rect(354, 399, 240, 74), 6, 20)
        Quitrect2 = pygame.draw.rect(window, color_Normal, pygame.Rect(844, 664, 112, 62), 6, 20)
        Helprect3 = pygame.draw.rect(window, color_Normal, pygame.Rect(44, 664, 112, 62), 6, 20)
        pygame.display.update()
        pygame.display.flip()


    pygame.quit() #uninitialize all pygame modules

window1()
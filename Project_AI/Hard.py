import pygame
import sys
import numpy
import interface2
#from AI import minimax
import math

color_hover = (202, 203, 213)
color_Normal = (160, 0, 0) # color of button
pygame.init()
pygame.font.init()
def Hard():
    pygame.init()

    matrix = numpy.ones((17, 25))

    matrix *= -1



    firstplayerP = [[0, 12], [1, 11], [1, 13], [2, 10], [2, 12], [2, 14], [3, 9], [3, 11], [3, 13], [3, 15]]   #green
    secondplayerP = [[4, 18], [4, 20], [4, 22], [4, 24], [5, 19], [5, 21], [5, 23], [6, 20], [6, 22], [7, 21]] #yellow
    thirdplayerP = [[12, 18], [12, 20], [12, 22], [12, 24], [11, 19], [11, 21], [11, 23], [10, 20], [10, 22], [9, 21]] #orange
    forthplayerP = [[16, 12], [15, 11], [15, 13], [14, 10], [14, 12], [14, 14], [13, 9], [13, 11], [13, 13], [13, 15]] #red
    fifthplayerP = [[12, 0], [12, 2], [12, 4], [12, 6], [11, 1], [11, 3], [11, 5], [10, 2], [10, 4], [9, 3]]   #purple
    sixthplayerP = [[4, 0], [4, 2], [4, 4], [4, 6], [5, 1], [5, 3], [5, 5], [6, 2], [6, 4], [7, 3]]   #blue


    move_index = [[-1, -1], [-1, 1], [0, 2], [1, 1], [1, -1], [0, -2]]


    matrix_index = [1, 2, 3, 4, 13, 12, 11, 10, 9]
    for i in range(9):
        j = 12
        first_time = True
        while matrix_index[i] > 0:
            if (i % 2 == 0) and first_time:
                first_time = False
                # print(i,j)
                matrix[i][j] = matrix[16 - i][j] = 0
                matrix_index[i] -= 1

            else:
                j -= 1
                matrix[i][j] = matrix[i][24 - j] = matrix[16 - i][j] = matrix[16 - i][24 - j] = 0
                matrix_index[i] -= 2
            j -= 1


    def playerInserting(index):
        if index == 1:
            for i in range(len(firstplayerP)):
                matrix[firstplayerP[i][0]][firstplayerP[i][1]] = index
        if index == 2:
            for i in range(len(secondplayerP)):
                matrix[secondplayerP[i][0]][secondplayerP[i][1]] = index
        if index == 3:
            for i in range(len(thirdplayerP)):
                matrix[thirdplayerP[i][0]][thirdplayerP[i][1]] = index
        if index == 4:
            for i in range(len(forthplayerP)):
                matrix[forthplayerP[i][0]][forthplayerP[i][1]] = index
        if index == 5:
            for i in range(len(fifthplayerP)):
                matrix[fifthplayerP[i][0]][fifthplayerP[i][1]] = index
        if index == 6:
            for i in range(len(sixthplayerP)):
                matrix[sixthplayerP[i][0]][sixthplayerP[i][1]] = index


    class positionClass:
        def _init_(self):
            self_x = 0
            self_y = 0

        def point(self):
            colors = [(240,240,240), (0,255,0), (255,255,0), (255,102,0), (255,0,0), (128,0,128), (0,0,255)]
            for i in range(0, 17):
                for j in range(0, 25):
                    if matrix[i][j] >= 0:
                        rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pions_rect.append(pygame.draw.rect(screen, colors[int(matrix[i][j])], rect, border_radius=20))


    def legalMoves(coor):
        valid_index = []
        for i in range(len(move_index)):

            x = coor[0] + move_index[i][0]
            y = coor[1] + move_index[i][1]
            if -1 < x < 17 and -1 < y < 25:
                if matrix[x][y] == 0:
                    valid_index.append([x, y])
                elif matrix[x][y] != -1:
                    checkRoute(move_index[i], x, y, valid_index)

        return valid_index


    def checkRoute(path_coor, x, y, moves_array):
        # print('before:', x, y)
        x2 = x + path_coor[0]
        y2 = y + path_coor[1]
        if [x2, y2] not in moves_array:
            if -1 < x2 < 17 and -1 < y2 < 25:
                if matrix[x2][y2] == 0:
                    moves_array.append([x2, y2])
                    for j in range(len(move_index)):
                        x3 = x2 + move_index[j][0]
                        y3 = y2 + move_index[j][1]
                        if [x3, y3] not in moves_array:
                            if -1 < x3 < 17 and -1 < y3 < 25:
                                if matrix[x3][y3] > 0:
                                    checkRoute(move_index[j], x3, y3, moves_array)


    def move(pos, target):
        matrix[target[0]][target[1]] = matrix[pos[0]][pos[1]]
        matrix[pos[0]][pos[1]] = 0


    def getCoor(x, y):
            grid_width = 0
            grid_heigth = 0
            coor = [int((y - grid_heigth) / 20), int((x - grid_width) / 20)]
            return coor


    def Movement(moves=[], clicked_token=None):

            colors = [(240,240,240), (0,255,0), (255,255,0), (255,102,0), (255,0,0), (128,0,128), (0,0,255)]
            moves.append(clicked_token)
            for i in range(0, 17):
                for j in range(0, 25):
                    if matrix[i][j] >= 0:
                        rect = pygame.Rect(j * CELL_SIZE, i * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                        pions_rect.append(pygame.draw.rect(screen, colors[int(matrix[i][j])], rect, border_radius=20))
                    if [i, j] in moves:
                        test_cercle = pygame.image.load('circle.png')
                        test_cercle = pygame.transform.scale(test_cercle, (CELL_SIZE, CELL_SIZE))
                        screen.blit(test_cercle, (j * CELL_SIZE, i * CELL_SIZE))


    def showPostions():
            for i in range(0, nb_col):
                for j in range(0, nb_ligne):
                    rect = pygame.Rect(i * CELL_SIZE, j * CELL_SIZE, CELL_SIZE, CELL_SIZE)
                    pygame.draw.rect(screen, pygame.Color("white"), rect, width=1)

    def get_all_positios(matrix):
        positions = []
        for i in range(0, 17):
            for j in range(0, 25):
                if matrix[i][j] == 2 or matrix[i][j] == 3 or matrix[i][j] == 4:
                    positions.append([i, j])

        return positions

    def evaluate(matrix, id):  # id = [x,y]
        total_distance = 0
        avg_distance = 0
        id1 = id[0]
        id2 = id[1]
        if matrix[id1][id2] == 4:
            goal = firstplayerP
            # xg_yg = goal[g] = [xg,yg]---------------xg_yg[0] = xg-------------xg_yg[1] = yg
            for g in range(len(goal)):
                xg_yg = goal[g]

                square_yg = (xg_yg[1] * 14.43) / 25
                square_y = (id2 * 14.43) / 25

                x = id1
                xg = xg_yg[0]

                distance_diag = math.sqrt(((xg - x) ** 2) + ((square_yg - square_y) ** 2))

                total_distance = total_distance + distance_diag


            avg_distance4 = total_distance / 10
            avg_distance = max(avg_distance4, avg_distance)

        elif matrix[id1][id2] == 2:
            goal = fifthplayerP
            # xg_yg = goal[g] = [xg,yg]---------------xg_yg[0] = xg-------------xg_yg[1] = yg
            for g in range(len(goal)):
                xg_yg = goal[g]

                square_yg = (xg_yg[1] * 14.43) / 25
                square_y = (id2 * 14.43) / 25

                x = id1
                xg = xg_yg[0]

                distance_diag = math.sqrt(((xg - x) ** 2) + ((square_yg - square_y) ** 2))

                total_distance = total_distance + distance_diag


            avg_distance2 = total_distance / 10
            avg_distance = max(avg_distance2, avg_distance)

        elif matrix[id1][id2] == 3:
            goal = sixthplayerP
            # xg_yg = goal[g] = [xg,yg]---------------xg_yg[0] = xg-------------xg_yg[1] = yg
            for g in range(len(goal)):
                xg_yg = goal[g]

                square_yg = (xg_yg[1] * 14.43) / 25
                square_y = (id2 * 14.43) / 25

                x = id1
                xg = xg_yg[0]

                distance_diag = math.sqrt(((xg - x) ** 2) + ((square_yg - square_y) ** 2))

                total_distance = total_distance + distance_diag


            avg_distance3 = total_distance / 10
            avg_distance = max(avg_distance3, avg_distance)

        return avg_distance


    def minimax(pos,matrix, depth, max_player, id, best_move):
        if depth == 0:
            return evaluate(matrix, id), best_move

        if max_player:
            maxEval = float('-inf')

            for p in pos:
                moves = legalMoves(p)
                moves.append(p)
                length = len(moves) - 1

                for i in range(length):
                    id = moves[length]
                    move(moves[length], moves[i])

                    evaluation = minimax(pos, matrix, depth - 1, False, id, best_move)[0]
                    maxEval = max(maxEval, evaluation)
                    if maxEval == evaluation:
                        best_move.append(moves[length])
                        best_move.append(moves[i])

                    # undo the step
                    move(moves[i], moves[length])

            return maxEval, best_move

        else:
            minEval = float('inf')
            for p in pos:
                moves = legalMoves(p)
                moves.append(p)
                length = len(moves) - 1

                for i in range(length):
                    id = moves[length]
                    move(moves[length], moves[i])

                    evaluation = minimax(pos, matrix, depth - 1, True, id, best_move)[0]
                    minEval = min(minEval, evaluation)

                    if minEval == evaluation:
                        best_move.append(moves[length])
                        best_move.append(moves[i])

                    # undo the step
                    move(moves[i], moves[length])

            return minEval, best_move


    def text_objects(text, font):
        textsurface = font.render(text, True, (0,0,0))
        return textsurface, textsurface.get_rect()

    def WritingText(text, text_pos_x, text_pos_y, text_size, col):
            text_font = pygame.font.SysFont("palamecia titling.ttf", text_size)
            text_render = text_font.render(text, True, col)
            screen.blit(text_render, (text_pos_x, text_pos_y))



    def winner():
        first = True
        second = True
        third = True
        fourth = True
        fifth = True
        sixth = True
        for i in range(len(firstplayerP)):
            if matrix[firstplayerP[i][0]][firstplayerP[i][1]] != 4:
                fourth = False
                break
        for i in range(len(forthplayerP)):
            if matrix[forthplayerP[i][0]][forthplayerP[i][1]] != 1:
                first = False
                break
        for i in range(len(secondplayerP)):
            if matrix[secondplayerP[i][0]][secondplayerP[i][1]] != 5:
                fifth = False
                break
        for i in range(len(fifthplayerP)):
            if matrix[fifthplayerP[i][0]][fifthplayerP[i][1]] != 2:
                second = False
                break
        for i in range(len(thirdplayerP)):
            if matrix[thirdplayerP[i][0]][thirdplayerP[i][1]] != 6:
                sixth = False
                break
        for i in range(len(sixthplayerP)):
            if matrix[sixthplayerP[i][0]][sixthplayerP[i][1]] != 3:
                third = False
                break
        if second == True & third == True & fourth == True:
            WritingText('Player 2 had won!', nb_col * CELL_SIZE - 370, nb_ligne * CELL_SIZE - 100, 50, (255, 255, 255))
            game_on = False
        elif first == True & sixth == True & fifth == True:
            WritingText('Player 1 had won!', nb_col * CELL_SIZE - 370, nb_ligne * CELL_SIZE - 100, 50, (255, 255, 255))
            game_on = False
        else:
            return False


    playerInserting(1)
    playerInserting(2)
    playerInserting(3)
    playerInserting(4)
    playerInserting(5)
    playerInserting(6)


    nb_col = 25
    nb_ligne = 25
    CELL_SIZE = 20
    (width, height) = (1000, 780)

    screen = pygame.display.set_mode((width, height))

    timer = pygame.time.Clock()
    game_on = True
    pions_rect = []

    players = positionClass()
    BackColor = (0, 0, 0)
    screen.fill(BackColor)
    pygame.display.flip()
    screen.fill(pygame.Color(BackColor))
    players.point()

    player_index1 = 1
    player_index2 = 5
    player_index3 = 6

    is_selecting = False
    player_valid_moves = []
    last_selected_token = []


    def text_objects(text, font):
        textsurface = font.render(text, True, (BackColor))
        return textsurface, textsurface.get_rect()

    def button(msg, x, y, w, h, ic, ac, action=None):
        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()
        if x + w > mouse[0] > x and y + h > mouse[1] > y:
            pygame.draw.rect(screen, ac, (x, y, w, h))

            if click[0] == 1 and action != None:
                action()
        else:
            pygame.draw.rect(screen, ic, (x, y, w, h))

        pygame.font.init()
        smallText = pygame.font.Font('palamecia titling.ttf', 20)
        textSurf, textRect = text_objects(msg, smallText)
        textRect.center = ((x + (w / 2)), (y + (h / 2)))
        screen.blit(textSurf, textRect)

    while game_on:

        if player_index1 == 2 or player_index2 == 3 or player_index3 == 4:

            pos = get_all_positios(matrix)

            value, best = minimax(pos, matrix, 5, True, [], [])
            pos = best[0]
            tar = best[1]
            move(pos, tar)

            Movement()

            player_index1 = 1
            player_index2 = 5
            player_index3 = 6


        if player_index1 == 1 or player_index2 == 5 or player_index3 == 6:

            if (winner() == False):
                WritingText('Play! Your Turn', nb_col * CELL_SIZE - 370, nb_ligne * CELL_SIZE - 100, 50, (255, 255, 255))

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    sys.exit()
                if event.type == pygame.MOUSEBUTTONDOWN:
                    pos = pygame.mouse.get_pos()


                    clicked_sprites = [s for s in pions_rect if s.collidepoint(pos)]

                    if clicked_sprites:
                        clicked_token = getCoor(clicked_sprites[0].x, clicked_sprites[0].y)
                        if matrix[clicked_token[0], clicked_token[1]] == player_index1 or matrix[clicked_token[0], clicked_token[1]] == player_index2 or matrix[clicked_token[0], clicked_token[1]] == player_index3:
                            if clicked_token == last_selected_token:
                                is_selecting = False
                                last_selected_token = []
                                player_valid_moves = []
                                screen.fill(pygame.Color(0,0,0))
                                Movement()

                            else:
                                player_valid_moves = legalMoves(clicked_token)
                                last_selected_token = clicked_token
                                is_selecting = True
                                screen.fill(pygame.Color(0,0,0))
                                Movement(player_valid_moves, last_selected_token)

                        elif clicked_token in player_valid_moves:
                            move(last_selected_token, clicked_token)
                            winner()
                            is_selecting = False
                            last_selected_token = []
                            player_valid_moves = []
                            screen.fill(pygame.Color(0,0,0))
                            Movement()
                            if player_index1 == 1 or player_index2 == 5 or player_index3 == 6:
                                player_index1 = 2
                                player_index2 = 3
                                player_index3 = 4

                button("back", 500, 430, 70, 30, color_Normal, color_hover, interface2.window2)
                rect2 = pygame.draw.rect(screen, color_Normal, pygame.Rect(494, 424, 82, 42), 6, 20)
                #break

        pygame.display.update()
        timer.tick(60)

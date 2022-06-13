#from file name import function name
import Hard
import math

def get_all_positios(matrix):
    positions = []
    for i in range(0, 17):
        for j in range(0, 25):
            if matrix[i][j] == 2 or matrix[i][j] == 3 or matrix[i][j] == 4:
                positions.append([i, j])

    return positions


def get_all_valid_moves(positions):
    x = len(positions)
    a_3d_list = []

    for i in range(len(positions)):
        coor = positions[i]
        move = Hard.valid_moves(coor)
        pos_move = [coor] + move
        y = len(pos_move)
        for i in range(x):
            a_3d_list.append([])

            for j in range(y):
                a_3d_list[i].append([])

                for k in range(2):
                    a_3d_list[i][j].append(pos_move)

    return a_3d_list


def evaluate(newmatrix, idx): #index = [x,y]
    total_distance = 0
    avg_distance = 0

    if newmatrix[idx] == 4:
        goal = Hard.first_player
        # xg_yg = goal[g] = [xg,yg]---------------xg_yg[0] = xg-------------xg_yg[1] = yg
        for g in range(len(goal)):
            xg_yg = goal[g]

            square_yg = (xg_yg[1] * 14.43) / 25
            square_y = (idx[1] * 14.43) / 25

            x = idx[0]
            xg = xg_yg[0]

            distance_diag = math.sqrt(((xg - x) ** 2) + ((square_yg - square_y) ** 2))

            total_distance = total_distance + distance_diag

        avg_distance1 = total_distance / 10
        avg_distance = max(avg_distance1,0)
    if newmatrix[idx] == 2:
        goal = Hard.fifth_player
        # xg_yg = goal[g] = [xg,yg]---------------xg_yg[0] = xg-------------xg_yg[1] = yg
        for g in range(len(goal)):
            xg_yg = goal[g]

            square_yg = (xg_yg[1] * 14.43) / 25
            square_y = (idx[1] * 14.43) / 25

            x = idx[0]
            xg = xg_yg[0]

            distance_diag = math.sqrt(((xg - x) ** 2) + ((square_yg - square_y) ** 2))

            total_distance = total_distance + distance_diag

        avg_distance2 = total_distance / 10
        avg_distance = max(avg_distance, avg_distance2)
    if newmatrix[idx] == 3:
        goal = Hard.sixth_player
        # xg_yg = goal[g] = [xg,yg]---------------xg_yg[0] = xg-------------xg_yg[1] = yg
        for g in range(len(goal)):
            xg_yg = goal[g]

            square_yg = (xg_yg[1] * 14.43) / 25
            square_y = (idx[1] * 14.43) / 25

            x = idx[0]
            xg = xg_yg[0]

            distance_diag = math.sqrt(((xg - x) ** 2) + ((square_yg - square_y) ** 2))

            total_distance = total_distance + distance_diag

        avg_distance3 = total_distance / 10
        avg_distance = max(avg_distance, avg_distance3)
    return avg_distance

def minimax(newmatrix, depth, max_player, id):
    pos = get_all_positios(newmatrix)
    _3D_moves = get_all_valid_moves(pos)

    if depth == 0:
        return evaluate(newmatrix, id), newmatrix

    if max_player:
        maxEval = float('-inf')
        best_move = None

        for moves in _3D_moves:
            for i in range(1, len(moves)):
                id = moves[i]
                Hard.move(moves[0], moves[i])

                evaluation = minimax(Hard.matrix, depth - 1, False, id)[0]
                maxEval = max(maxEval, evaluation)
                if maxEval == evaluation:
                    best_move = Hard.matrix

                #idx = moves[i]
                #undo the step
                Hard.move(moves[i], moves[0])

        return maxEval, best_move

    else:
        minEval = float('inf')
        best_move = None

        for moves in _3D_moves:
            for i in range(1, len(moves)):
                Hard.move(moves[0], moves[i])
                evaluation = minimax(Hard.matrix, depth - 1, True)[0]
                minEval = min(minEval, evaluation)
                if minEval == evaluation:
                    best_move = Hard.matrix

                moves[i]
                # undo the step
                Hard.move(moves[i], moves[0])

        return minEval, best_move






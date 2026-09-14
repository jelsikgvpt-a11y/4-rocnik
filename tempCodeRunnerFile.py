#import NumPy kniznicu na zoznamy

chessboard = []


def createchessboard():
    global chessboard
    row = [0] * 8
    for i in range(8):
        row = [0] * 8
        chessboard.append(row)
        
def checkit(x,y):
    for i in range(0,8):
        if chessboard[y][i] == 1:
            return False
        if chessboard[i][x] == 1:
            return False
    for i in range(0,8):
        for j in range(0,8):
            if i + j == x+y:
                if chessboard[i][j] == 1:
                    return False
            if i - j == y - x:
                if chessboard[i][j] == 1:
                    return False
    return True
        
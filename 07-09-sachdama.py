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
    return True
        

        
        
        
createchessboard()


chessboard[2][3] = 1
print(chessboard)


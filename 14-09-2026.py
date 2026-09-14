sudoku = []

def create_sudoku(sudoku):
    f = open("sudoku.txt", "r")
    for row in f:
        row = row.strip()
        temp = []
        for char in row:
            temp.append(int(char))
        sudoku.append(temp)
create_sudoku(sudoku)
print(sudoku)

def over(x,y, number):
    for i in range(0,9):
        if sudoku[y][i] == number or sudoku[i][x] == number:
            return False
    sx = (x // 3) * 3
    sy = (y // 3) * 3
    for i in range(sx, sx + 3):
        for j in range(sx, sx+3):
            if sudoku [i][j] == number:
                return False
    return True

over(1,2,7)
print(over(1,2,7))

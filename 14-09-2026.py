from PIL import Image, ImageDraw, ImageFont
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
    for i in range(sy, sy + 3):
        for j in range(sx, sx+3):
            if sudoku [i][j] == number:
                return False
    return True

over(1,2,7)
print(over(1,2,7))


def sudoku_solver():
    global sudoku
    for y in range (9):
        for x in range (9):
            if sudoku[y][x] == 0:
                for i in range(1,10):
                    if over(x,y,i):
                        sudoku[y][x] = i
                        if sudoku_solver():
                            return True
                        sudoku[y][x] = 0
                return False
    print(sudoku)
    return True

sudoku_solver()

#teraz to sudoku dame na obrazek
img = Image.new("RGB", (630, 630), "white")
draw = ImageDraw.Draw(img)
image_font = ImageFont.truetype("arial.ttf", 40)

#teraz cisla a linie
for i in range(10):
    if i % 3 == 0:
        draw.line((i*70, 0, i*70, 630), fill="black", width=5)
        draw.line((0, i*70, 630, i*70), fill="black", width=5)
    else:
        draw.line((i*70, 0, i*70, 630), fill="black", width=2)
        draw.line((0, i*70, 630, i*70), fill="black", width=2)
        
for y in range(9):
    for x in range(9):
        if sudoku[y][x] != 0:
            draw.text((x*70 + 20, y*70 + 10), str(sudoku[y][x]), fill="black", font=image_font)
            




img.show()
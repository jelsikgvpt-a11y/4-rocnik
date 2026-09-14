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

#teraz cisla a linie cez stvorceky
draw.line((0, 210, 630, 210), fill="black", width=4)
for i in range(9):
    for j in range(9):
        draw.rectangle((i*70, j*70, (i+1)*70, (j+1)*70), outline="black", width=2)
        
        if sudoku[j][i] != 0:
            draw.text((i*70 + 20, j*70 + 10), str(sudoku[j][i]), fill="black", font=image_font)
            
draw.line((0, 210, 630, 210), fill="black", width=8)
draw.line((210,0,210,630), fill="black", width=8)
draw.line((420, 0, 420, 630), fill="black", width=8)
draw.line((0, 420, 630, 420), fill="black", width=8)

img.show()
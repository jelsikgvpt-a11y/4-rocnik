names = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def spracuj_cisla():
    for cislo in names:
        fr = open("cisla/" + cislo + ".txt", "r")
        for line in fr:
            print(line)


spracuj_cisla()       
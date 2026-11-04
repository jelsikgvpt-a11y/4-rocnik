import random
import os

# Hra: "Poklad v zámku"
# Jednohráčová textová hra pre zabavenie v konzole.

SIZE = 7
START = (0, 0)
MAX_TURNS = 30
TOTAL_TREASURES = 3


def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')


def print_intro():
    print("""
    ╔══════════════════════════════════════╗
    ║        POKLAD V ZÁMKU             ║
    ║      1 hráč, 1 veľký poklad       ║
    ╚══════════════════════════════════════╝
    """)
    print("Vstup do zámku je otvorený. Zbieraj 3 poklady, vyhýbaj sa pastiam a zvyšuj životy.")
    print("Príkazy: w = hore, a = vľavo, s = dole, d = vpravo, q = ukončiť hru")
    print("Znášky: P = ty, T = poklad, + = lektvar, X = past, M = monštrum, . = prázdne pole")


def generate_map():
    board = [["." for _ in range(SIZE)] for _ in range(SIZE)]
    positions = []

    def place(item, count):
        for _ in range(count):
            while True:
                x = random.randint(0, SIZE - 1)
                y = random.randint(0, SIZE - 1)
                if (x, y) != START and (x, y) not in positions:
                    positions.append((x, y))
                    board[y][x] = item
                    break

    place("T", TOTAL_TREASURES)
    place("X", 5)
    place("+", 3)
    place("M", 3)
    return board


def print_board(board, player_pos, hp, treasure_collected, turns_left):
    clear_screen()
    print(f"Životy: {hp} | Zbierané poklady: {treasure_collected}/{TOTAL_TREASURES} | Krokov: {turns_left}")
    print("  " + " ".join(str(i) for i in range(SIZE)))
    for y in range(SIZE):
        row = [str(y), "|"]
        for x in range(SIZE):
            cell = board[y][x]
            if (x, y) == player_pos:
                row.append("P")
            else:
                row.append(cell)
        print(" ".join(row))
    print("Legenda: P = hráč, T = poklad, + = lektvar, X = past, M = monštrum")


def move_player(player_pos, direction):
    x, y = player_pos
    if direction == "w":
        y -= 1
    elif direction == "a":
        x -= 1
    elif direction == "s":
        y += 1
    elif direction == "d":
        x += 1
    else:
        return player_pos

    x = max(0, min(SIZE - 1, x))
    y = max(0, min(SIZE - 1, y))
    return (x, y)


def handle_cell(board, pos, hp, treasure_collected):
    x, y = pos
    cell = board[y][x]

    if cell == "T":
        board[y][x] = "."
        treasure_collected += 1
        print("Našiel si poklad! Krásny úlovok.")
        input("Stlač Enter pre pokračovanie... ")
    elif cell == "+":
        board[y][x] = "."
        hp += 2
        print("Našiel si lektvar! +2 životy.")
        input("Stlač Enter pre pokračovanie... ")
    elif cell == "X":
        hp -= 2
        print("Spadol si do pasce! Stratil si 2 životy.")
        input("Stlač Enter pre pokračovanie... ")
    elif cell == "M":
        board[y][x] = "."
        battle_roll = random.randint(1, 6)
        if battle_roll >= 4:
            print("Bojuješ s monštrom a vyhral si! Super.")
        else:
            hp -= 3
            print("Monštrum ťa zranilo! Stratil si 3 životy.")
        input("Stlač Enter pre pokračovanie... ")

    return hp, treasure_collected


def play_game():
    board = generate_map()
    player_pos = START
    hp = 8
    treasure_collected = 0
    turns_left = MAX_TURNS

    while hp > 0 and treasure_collected < TOTAL_TREASURES and turns_left > 0:
        print_board(board, player_pos, hp, treasure_collected, turns_left)
        command = input("Tvoj ťah: ").strip().lower()

        if command == "q":
            print("Hru si ukončil. Vráť sa neskôr na ďalšiu výpravu!")
            return

        if command not in ["w", "a", "s", "d"]:
            print("Neplatný príkaz! Použi w, a, s, d alebo q.")
            input("Stlač Enter pre pokračovanie... ")
            continue

        new_pos = move_player(player_pos, command)
        player_pos = new_pos
        turns_left -= 1
        hp, treasure_collected = handle_cell(board, player_pos, hp, treasure_collected)

        if hp <= 0:
            clear_screen()
            print("Zomrel si v zámku... ale aspoň si bojoval statočne!")
            print(f("Zbieral si {treasure_collected} pokladov z {TOTAL_TREASURES}."))
            return

    clear_screen()
    if treasure_collected >= TOTAL_TREASURES:
        print("Gratulujem! Získal si všetky 3 poklady a vyhral si hru!")
        print("Zámok sa rozsvietil a ty si odchádzaš ako skutočný hrdina.")
    elif turns_left <= 0:
        print("Čas vypršal! Zámok sa zatvoril a ty si nevyšiel so všetkými pokladmi.")
        print(f("Stihol si nazbierať {treasure_collected} pokladov.") )
    else:
        print("Hra skončila.")


if __name__ == "__main__":
    print_intro()
    input("Stlač Enter pre začatie hry... ")
    play_game()

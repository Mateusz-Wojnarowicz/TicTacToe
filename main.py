rows = []
columns = []
diagonals = []
counter = 0
string = ""
win = False

def play():
    global rows
    global counter

    while not win:
        global string
        if counter == 0:
            string = get_input(counter)
            update(original=string)
            counter += 1
        else:
            coordinates_in_strings = get_input(counter)
            update(a=coordinates_in_strings[0], b=coordinates_in_strings[1])
            check_win()
            if counter == 9 and win is False:
                print("Draw")
                break
            counter += 1


def get_input(c):
    if c == 0:
        return 9 * " "
    else:
        while True:
            global rows
            s = input("Enter the coordinates: ").split()
            try:
                coordinates = list(map(int, s))
            except ValueError:
                print("You should enter numbers!")
                continue
            if len(coordinates) != 2:
                print("You should enter just two numbers!")
                continue
            elif not(1 <= coordinates[0] <= 3) or not(1 <= coordinates[0] <= 3):
                print("Coordinates should be from 1 to 3!")
                continue
            elif rows[coordinates[0]-1][coordinates[1] - 1] is not " ":
                print("This cell is occupied! Choose another one!")
                continue
            else:
                return [coordinates[0]-1, coordinates[1] - 1]




def update(original=None, a=None, b=None):
    global string
    global rows
    global columns
    global diagonals
    global counter
    if a is not None:
        if counter % 2 == 1:
            rows[a][b] = "X"
        else:
            rows[a][b] = "O"
    else:
        string = original
        rows = [[string[0], string[1], string[2]], [string[3], string[4], string[5]], [string[6], string[7], string[8]]]
    print("---------\n| {} {} {} |\n| {} {} {} |\n| {} {} {} |\n---------".format(rows[0][0], rows[0][1], rows[0][2],
                                                                                    rows[1][0], rows[1][1], rows[1][2],
                                                                                    rows[2][0], rows[2][1], rows[2][2]))
    columns = [[rows[0][0], rows[1][0], rows[2][0]], [rows[0][1], rows[1][1], rows[2][1]], [rows[0][2], rows[1][2], rows[2][2]]]
    diagonals = [[rows[0][0], rows[1][1], rows[2][2]], [rows[0][2], rows[1][1], rows[2][0]]]





def win_x():
    return bool((len(set(rows[0])) == 1 and rows[0][0] == "X")
                or (len(set(rows[1])) == 1 and rows[1][0] == "X")
                or (len(set(rows[2])) == 1 and rows[2][0] == "X")
                or (len(set(columns[0])) == 1 and columns[0][0] == "X")
                or (len(set(columns[1])) == 1 and columns[1][0] == "X")
                or (len(set(columns[2])) == 1 and columns[2][0] == "X")
                or (len(set(diagonals[0])) == 1 and diagonals[0][0] == "X")
                or (len(set(diagonals[1])) == 1 and diagonals[1][0] == "X"))


def win_o():
    return bool((len(set(rows[0])) == 1 and rows[0][0] == "O")
                or (len(set(rows[1])) == 1 and rows[1][0] == "O")
                or (len(set(rows[2])) == 1 and rows[2][0] == "O")
                or (len(set(columns[0])) == 1 and columns[0][0] == "O")
                or (len(set(columns[1])) == 1 and columns[1][0] == "O")
                or (len(set(columns[2])) == 1 and columns[2][0] == "O")
                or (len(set(diagonals[0])) == 1 and diagonals[0][0] == "O")
                or (len(set(diagonals[1])) == 1 and diagonals[1][0] == "O"))


def check_win():
    global win
    x = win_x()
    o = win_o()
    if x:
        print("X wins")
        win = True
    elif o:
        print("O wins")
        win = True


play()

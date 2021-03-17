def print_field(field):
    print("---------")
    for element in range(len(field)):
        print(f'| {" ".join(field[element])} |')
    print("---------")

inp = "_________"

cells = None
field = []
out = []
t = []

x_wins = False
o_wins = False
draw = False
impossible = False
not_finished = True
avg = len(inp) // 3
last = 0
turn = 0
player = ""
nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0", " "]
while last < len(inp):
    out.append(inp[int(last):int(last + avg)])
    last += avg
for i in range(len(out)):
    field.append(list(out[i]))

while not_finished:
    turn += 1
    if turn % 2 == 1:
        player = "X"
    if turn % 2 == 0:
        player = "O"

    x_count = 0
    o_count = 0
    _count = 0

    while True:
        try:
            cells = input("Enter the coordinates: ")
            if len(cells) == 3:
                if cells[0] in nums:
                    if 1 <= int(cells[0]) <= 3 and 1 <= int(cells[2]) <= 3:
                        if field[int(cells[0]) - 1][int(cells[2]) - 1] == "_":
                            input_x = int(cells[0]) - 1
                            input_y = int(cells[2]) - 1
                            # player_turn = [input_x, input_y]

                            break
                        else:
                            print("This cell is occupied! Choose another one!")
                    else:
                        print("Coordinates should be from 1 to 3!")
                else:
                    print("You should enter numbers!")
            else:
                print("Enter the coordinates as follows: (x y)")

        except ValueError:
            pass

    field[input_x][input_y] = player

    # calculating difference between numbers of X and O
    for i in field:
        for ii in i:
            if ii == "X":
                x_count += 1
            if ii == "O":
                o_count += 1
            if ii == "_":
                _count += 1

    x_o_diff = abs(x_count - o_count)

    print_field(field)
    if x_o_diff < 2:# and (not o_wins and not x_wins):

        if field[0][0] == field[0][1] == field[0][2] == "X" or field[1][0] == field[1][1] == field[1][2] == "X" or field[2][0] == field[2][1] == field[2][2] == "X":
            x_wins = True

        elif field[0][0] == field[1][0] == field[2][0] == "X" or field[0][1] == field[1][1] == field[2][1] == "X" or field[0][2] == field[1][2] == field[2][2] == "X":
            x_wins = True

        elif field[0][0] == field[1][1] == field[2][2] == "X" or field[0][2] == field[1][1] == field[2][0] == "X":
            x_wins = True

        if field[0][0] == field[0][1] == field[0][2] == "O" or field[1][0] == field[1][1] == field[1][2] == "O" or field[2][0] == field[2][1] == field[2][2] == "O":
            o_wins = True

        elif field[0][0] == field[1][0] == field[2][0] == "O" or field[0][1] == field[1][1] == field[2][1] == "O" or field[0][2] == field[1][2] == field[2][2] == "O":
            o_wins = True

        elif field[0][0] == field[1][1] == field[2][2] == "O" or field[0][2] == field[1][1] == field[2][0] == "O":
            o_wins = True

        if o_wins and x_wins:
            print("Impossible")
        else:
            if not o_wins and not x_wins and _count > 0:
                not_finished = True
                # print("Game not finished")
            elif o_wins and not x_wins:
                not_finished = False
                print("O wins")
            elif x_wins and not o_wins:
                not_finished = False
                print("X wins")
            else:
                print("Draw")
                not_finished = False

    else:
        print("Impossible")
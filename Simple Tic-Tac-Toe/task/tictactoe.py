# write your code here
matrix = [[" ", " ", " "],
          [" ", " ", " "],
          [" ", " ", " "]]

print("---------")
print("| {} {} {} |".format(matrix[0][0], matrix[0][1], matrix[0][2]))
print("| {} {} {} |".format(matrix[1][0], matrix[1][1], matrix[1][2]))
print("| {} {} {} |".format(matrix[2][0], matrix[2][1], matrix[2][2]))
print("---------")

matrix_rows = [[matrix[0][0], matrix[0][1], matrix[0][2]],
               [matrix[1][0], matrix[1][1], matrix[1][2]],
               [matrix[2][0], matrix[2][1], matrix[2][2]],
               [matrix[0][0], matrix[1][0], matrix[2][0]],
               [matrix[0][1], matrix[1][1], matrix[2][1]],
               [matrix[0][2], matrix[1][2], matrix[2][2]],
               [matrix[0][0], matrix[1][1], matrix[2][2]],
               [matrix[0][2], matrix[1][1], matrix[2][0]]]


def update_matrix_rows():
    global matrix_rows
    matrix_rows = [[matrix[0][0], matrix[0][1], matrix[0][2]],
                   [matrix[1][0], matrix[1][1], matrix[1][2]],
                   [matrix[2][0], matrix[2][1], matrix[2][2]],
                   [matrix[0][0], matrix[1][0], matrix[2][0]],
                   [matrix[0][1], matrix[1][1], matrix[2][1]],
                   [matrix[0][2], matrix[1][2], matrix[2][2]],
                   [matrix[0][0], matrix[1][1], matrix[2][2]],
                   [matrix[0][2], matrix[1][1], matrix[2][0]]]


def turn_play_x():
    user_play = input("Enter the coordinates: ").split()
    if not user_play[0].isdigit() or not user_play[1].isdigit():
        print("You should enter numbers!")
        turn_play_x()
    elif int(user_play[0]) < 1 or int(user_play[1]) < 1 or int(user_play[0]) > 3 or int(user_play[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        turn_play_x()
    elif matrix[int(user_play[0]) - 1][int(user_play[1]) - 1] != " ":
        print("This cell is occupied! Choose another one!")
        turn_play_x()
    else:
        matrix[int(user_play[0]) - 1][int(user_play[1]) - 1] = "X"
        print("---------")
        print("| {} {} {} |".format(matrix[0][0], matrix[0][1], matrix[0][2]))
        print("| {} {} {} |".format(matrix[1][0], matrix[1][1], matrix[1][2]))
        print("| {} {} {} |".format(matrix[2][0], matrix[2][1], matrix[2][2]))
        print("---------")
        update_matrix_rows()
        check_matrix_x()


def turn_play_o():
    user_play = input("Enter the coordinates: ").split()
    if not user_play[0].isdigit() or not user_play[1].isdigit():
        print("You should enter numbers!")
        turn_play_o()
    elif int(user_play[0]) < 1 or int(user_play[1]) < 1 or int(user_play[0]) > 3 or int(user_play[1]) > 3:
        print("Coordinates should be from 1 to 3!")
        turn_play_o()
    elif matrix[int(user_play[0]) - 1][int(user_play[1]) - 1] != " ":
        print("This cell is occupied! Choose another one!")
        turn_play_o()
    else:
        matrix[int(user_play[0]) - 1][int(user_play[1]) - 1] = "O"
        print("---------")
        print("| {} {} {} |".format(matrix[0][0], matrix[0][1], matrix[0][2]))
        print("| {} {} {} |".format(matrix[1][0], matrix[1][1], matrix[1][2]))
        print("| {} {} {} |".format(matrix[2][0], matrix[2][1], matrix[2][2]))
        print("---------")
        update_matrix_rows()
        check_matrix_o()


def check_matrix_x():
    number_of_x = len([x for x in matrix if x == "X"])
    number_of_o = len([x for x in matrix if x == "O"])

    if ["X", "X", "X"] in matrix_rows:
        if ["O", "O", "O"] in matrix_rows:
            print("Impossible")
        else:
            print("X wins")
    elif ["O", "O", "O"] in matrix_rows:
        print("O wins")
    elif abs(number_of_x - number_of_o) > 1:
        print("Impossible")
    elif any(" " in matrix[i] for i in range(3)):
        turn_play_o()
    else:
        print("Draw")


def check_matrix_o():
    number_of_x = len([x for x in matrix if x == "X"])
    number_of_o = len([x for x in matrix if x == "O"])

    if ["X", "X", "X"] in matrix_rows:
        if ["O", "O", "O"] in matrix_rows:
            print("Impossible")
        else:
            print("X wins")
    elif ["O", "O", "O"] in matrix_rows:
        print("O wins")
    elif abs(number_of_x - number_of_o) > 1:
        print("Impossible")
    elif any(" " in matrix[i] for i in range(3)):
        turn_play_x()
    else:
        print("Draw")


turn_play_x()

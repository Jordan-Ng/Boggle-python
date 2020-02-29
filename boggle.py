import random
import string
import re

board = [['-', '-', '-', '-'], ['-', '-', '-', '-'],
         ['-', '-', '-', '-'], ['-', '-', '-', '-']]

dice = ['AAEEGN', 'ELRTTY', 'AOOTTW', 'ABBJOO', 'EHRTVW', 'CIMOTU', 'DISTTY', 'EIOSST',
        'DELRVY', 'ACHOPS', 'HIMNQU', 'EEINSU', 'EEGHNW', 'AFFKPS', 'HLNNRZ', 'DEILRX']
# for grid in board:
#     print(grid)
user_answer = []
play_board = []
board_inst = []

# defining functions


def randomize_letters():
    for die in dice:
        die_inst = random.choice(die)
        if die_inst == 'Q':
            die_inst = 'Qu'
            board_inst.append(die_inst)
        else:
            die_inst
            board_inst.append(die_inst)

    for row in board:
        for ind, space in enumerate(row):
            if ind == 0:
                board[0] = board_inst[0:4]
            if ind == 1:
                board[1] = board_inst[4:8]
            if ind == 2:
                board[2] = board_inst[8:12]
            if ind == 3:
                board[3] = board_inst[12:16]
                # row[ind] = board_inst[ind]
    print(board)

    print(board_inst)


def merge_board():
    for row in board:
        join_row = '  '.join(row)
        play_board.append(join_row)
    print(play_board)


def show_board():
    for row in play_board:
        print(row)


def check_horiz():
    user_input = input("find your word")
    for row in board:
        join_row = ''.join(row)
        print(join_row)
        result = re.search(user_input, join_row, flags=re.IGNORECASE)
        # print(result)
        if result:
            user_answer.append(user_input)
            print("got that right, buddy")
            print(user_answer)
        else:
            print("Nah fam")
        # if user_input in join_row:
        #     print('got that right, buddy')
        # else:
        #     print('nah fam')


# actual game
# randomize_letters()
# merge_board()
# show_board()
# check_horiz()
New_game = input("Do you want to play boggle? (yes/no)")
if New_game == "yes":
    randomize_letters()
    merge_board()
    show_board()
    check_horiz()
else:
    print("bye bye")

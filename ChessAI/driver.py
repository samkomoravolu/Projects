import chess
import intelligence
import random

#max recursion depth
kDepth = 5

def driver() -> int:
    #set bw = 0 to play white or 1 for black
    bw = random.randint(0,1)
    board = chess.Board()
    if bw == 0:
        ai = intelligence.AI(board, chess.BLACK)
    else:
        ai = intelligence.AI(board, chess.WHITE)
        move = ai.move(kDepth, True, -9999, 9999)[0]
        board.push_uci(str(move))
        print(str(board) + "\n\n")
    move_number = 1
    while not board.is_checkmate():
        player_move = input("Move " + str(move_number) + ": ")
        try:
            board.push_uci(str(player_move))
        except:
            if player_move == "r":
                driver()
                return -1
            print("wrong")
            continue
        if board.is_checkmate():
            print("you win!")
            return 1
        move = ai.move(kDepth, True, -9999, 9999)[0]
        board.push_uci(str(move))
        print(str(board) + "\n\n")
        move_number += 1
    print("you lose!")
    return 0

driver()
#!/usr/bin/python3

import chess
print ("Taking values ")
def enumerate_moves(x, y, type):

    possible_moves = []     # Intializing empty list
    print ("Position is: ",( x , y))
    print("Piece type is :", type)
    board = chess.Board()
    # resolving knight moves. 
    if type  == "Knight":
        print("Possible moves are: ")
        possible_moves += [(x+2, y+1), (x+2, y-1)
                           ,(x+1, y+2), (x+1,y-2)
                           ,(x-2, y-1), (x-2, y+1)
                           ,(x-1, y+2), (x-1, y-2)]
        print(possible_moves)

    elif type == "Rook":
        # resolving down side rook
        a = x + 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a+1][b][0] == "w":
                    possible_moves.append([[a+1], [b]])
            except IndexError:
                pass
            a += 1

        # resolving left side
        a = x
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a][b-1][0] == "w":
                    possible_moves.append([[a], [b-1]])
            except IndexError:
                pass
            b -= 1

        # resolving up side rook
        a = x - 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a-1][b][0] == "w":
                    possible_moves.append([[a-1], [b]])
            except IndexError:
                pass
            a -= 1

        # resolving right side rook
        a = x
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a][b+1][0] == "w":
                    possible_moves.append([[a], [b+1]])
            except IndexError:
                pass
            b += 1    

    elif type  == "Queen":
        # Resolving down and right side Queen
        a = x + 1
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a+1][b+1][0] == "w":
                    possible_moves.append([[a+1], [b+1]])
            except IndexError:
                pass
            a += 1
            b += 1

        # Resolving down and left side Queen
        a = x + 1
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a+1][b-1][0] == "w":
                    possible_moves.append([[a+1], [b-1]])
            except IndexError:
                pass
            a += 1
            b -= 1

        # resolving up and right
        a = x - 1
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a-1][b+1][0] == "w":
                    possible_moves.append([[a-1], [b+1]])
            except IndexError:
                pass
            a -= 1
            b += 1

        # Resolving up and left
        a = x - 1
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a-1][b-1][0] == "w":
                    possible_moves.append([[a-1], [b-1]])
            except IndexError:
                pass
            a -= 1
            b -= 1

        # Resolving down side Queen
        a = x + 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a+1][b][0] == "w":
                    possible_moves.append([[a+1], [b]])
            except IndexError:
                pass
            a += 1

        # Resolving left
        a = x
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a][b-1][0] == "w":
                    possible_moves.append([[a], [b-1]])
            except IndexError:
                pass
            b -= 1

        # Resolving up side
        a = x - 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a-1][b][0] == "w":
                    possible_moves.append([[a-1], [b]])
            except IndexError:
                pass
            a -= 1

        # Resolving right side
        a = x
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves.append([[a], [b]])
            try:
                if board[a][b+1][0] == "w":
                    possible_moves.append([[a], [b+1]])
            except IndexError:
                pass
            b += 1

enumerate_moves(2, 2, "Knight")

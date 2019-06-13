#!/usr/bin/python3

import chess
print ("Evaluating potential chess board positions ")
def evaluate_moves(position, type):
    pos = str(position)
    x = int(pos[0])
    y = int(pos[1])
    possible_moves = []     # Intializing empty list
    print ("Position is: ",( x , y))
    print("Piece type is :", type)
    board = chess.Board()
    # resolving knight moves. 
    if type  == "Knight":
        print("Possible Knight moves are: ")
        possible_moves += [(x+2, y+1), (x+2, y-1)
                           ,(x+1, y+2), (x+1,y-2)
                           ,(x-2, y-1), (x-2, y+1)
                           ,(x-1, y+2), (x-1, y-2)]
        print(possible_moves)
    
    #Resolving Rook moves
    elif type == "Rook":
        print("Possible Rook moves are: ")
        # resolving down side rook moves
        a = x + 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a+1][b][0] == "w":
                    possible_moves += ([[a+1], [b]])
            except IndexError:
                pass
            a += 1

        # resolving left side rook moves
        a = x
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a][b-1][0] == "w":
                    possible_moves += ([[a], [b-1]])
            except IndexError: 
                pass
            b -= 1

        # resolving up side rook
        a = x - 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a-1][b][0] == "w":
                    possible_moves += ([[a-1], [b]])
            except IndexError:
                pass
            a -= 1

        # resolving right side rook
        a = x
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a][b+1][0] == "w":
                    possible_moves += ([[a], [b+1]])
            except IndexError:
                pass
            b += 1    
    
    #Resolving Queen moves
    elif type  == "Queen":
        print("Possible Queen moves are: ")
        # Resolving down and right side Queen
        a = x + 1
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a+1][b+1][0] == "w":
                    possible_moves += ([[a+1], [b+1]])
            except IndexError:
                pass
            a += 1
            b += 1

        # Resolving down and left side Queen
        a = x + 1
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a+1][b-1][0] == "w":
                    possible_moves += ([[a+1], [b-1]])
            except IndexError:
                pass
            a += 1
            b -= 1

        # resolving up and right side
        a = x - 1
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a-1][b+1][0] == "w":
                    possible_moves += ([[a-1], [b+1]])
            except IndexError:
                pass
            a -= 1
            b += 1

        # Resolving up and left
        a = x - 1
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a-1][b-1][0] == "w":
                    possible_moves += ([[a-1], [b-1]])
            except IndexError:
                pass
            a -= 1
            b -= 1

        # Resolving down side Queen
        a = x + 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a+1][b][0] == "w":
                    possible_moves += ([[a+1], [b]])
            except IndexError:
                pass
            a += 1

        # Resolving left
        a = x
        b = y - 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a][b-1][0] == "w":
                    possible_moves += ([[a], [b-1]])
            except IndexError:
                pass
            b -= 1

        # Resolving up side
        a = x - 1
        b = y
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a-1][b][0] == "w":
                    possible_moves += ([[a-1], [b]])
            except IndexError:
                pass
            a -= 1

        # Resolving right side
        a = x
        b = y + 1
        while (7 > a >= 0 and 7 > b >= 0) and (board[a][b] == ""):
            possible_moves += ([[a], [b]])
            try:
                if board[a][b+1][0] == "w":
                    possible_moves += ([[a], [b+1]])
            except IndexError:
                pass
            b += 1

evaluate_moves(22, "Knight")

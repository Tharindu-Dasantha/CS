import sys
import re


board = {'1h': 'bking', '6c': 'wqueen',
'2g': 'bbishop', '5h': 'bqueen', '3e': 'wking'}

listcanbe = []

for i in range(1,9):
    for j in ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']:
        listcanbe.append(str(i)+j)

amountw_all = 0
amountw_king = 0
amountw_pawns = 0

amountb_all = 0
amountb_king = 0
amountb_pawns = 0

# Checking the board
for i in board:
    # Checking the places
    if i not in listcanbe:
        sys.exit("Invalid Board")
    # Checking the pieces
    # Checking the names
    if not re.match('^b|w[pawn|knight|bishop|rook|queen|king]', board[i]):
        sys.exit("Invalid Board")
    # Checking the amount of the pieces
    typeof = board[i][:1]
    name = board[i][1:]
    
    match typeof:
        case "w":
            amountw_all += 1
            match name:
                case "king":
                    amountw_king += 1
                case "pawns":
                    amountw_pawns += 1
        case "b":
            amountb_all += 1
            match name:
                case "king":
                    amountb_king += 1
                case "pawns":
                    amountb_pawns += 1


# Checking the total number of pieces 
if amountw_all > 16 or amountb_all > 16:
    sys.exit("Invalid Board")
elif amountw_king > 1 or amountb_king > 1:
    sys.exit("Invalid Board")
elif amountw_pawns > 8 or amountb_pawns > 8:
    sys.exit("Invalid Board")
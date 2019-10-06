#Coded by Ribhu Sengupta.
def solveKnightMove(board, n, move_no, currRow, currCol): #solveKnightMove(board, dimesion of board, Moves_already_done, currRoe, currCol)

    if move_no == n*n: #Lets say n=8, if no of moves knight covered 64 then it will stop further recursion.
        return True
    
    rowDir = [+2, +1, -1, -2, -2, -1, +2, +2] #x or Row Co-ordinates where knight can be placed in respective to its current co-ordinate.
    colDir = [+1, +2, +2, +1, -1, -2, -2, -1] #y or Column Co-ordinates where knight can be placed in respective to its current co-ordinate.

    for index in range(0, len(rowDir)): #Loop among row and column coordinates
        nextRow = currRow + rowDir[index]
        nextCol = currCol + colDir[index]

        if canPlace(board, n, nextRow, nextCol) is True: #checking weather next move is valid and not covered till yet.
            board[nextRow][nextCol] = move_no+1
            isSuccessfull = solveKnightMove(board, n, move_no+1, nextRow, nextCol) # can predict that the next valid move could cover all the cells of chess board or not.
            if isSuccessfull is True:
                return True
            board[nextRow][nextCol] = 0
    return False

def canPlace(board, n, row, col):  # Can Check the next moves of knight 
    if row>=0 and row<n and col>=0 and col<n:
        if board[row][col] == 0:
            return True
        return False
    return False        

def printBoard(board, n): #printing the board.
    for index1 in range(0, n):
        for index2 in range(0, n):
            print(board[index1][index2])
        print('\n')

n = int(input("Enter a Dimension of board: "))

#creation of chess Board
board = [[]]
for index in range(0, n):
    for index2 in range(0, n):
        board[index].append(0)
    board.append([])
board.pop(index+1)
# end of creation of chess board
board[0][0] = 1
ans = solveKnightMove(board, n, 1, 0, 0) #solveKnightMove(board, dimesion, Moves_already_done, currRoe, currCol)

if ans is True:
    printBoard(board, n)
    print(board)
else:
    print("Not able to solve the board.")

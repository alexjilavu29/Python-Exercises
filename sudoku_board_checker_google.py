import time

def isValidSudoku(board):
    """
    :type board: List[List[str]]
    :rtype: bool
    """
    hashTable = {}
    for i in range(len(board)):
        for j in range(len(board[0])):

            if board[i][j] != ".":

                row = "row " + str(i + 1)

                column = "column " + str(j + 1)

                if (i + 1) % 3 != 0:
                    codeRow = ((i + 1) // 3) * 3
                else:
                    codeRow = (((i + 1) // 3) - 1) * 3

                if (j + 1) % 3 != 0:
                    codeCol = ((j + 1) // 3) + 1
                else:
                    codeCol = ((j + 1) // 3)

                codeSquare = codeRow + codeCol
                square = "square " + str(codeSquare)

                print(row + " | " + column + " | " + square + " | value " + board[i][j])

                if row not in hashTable:
                    hashTable[row] = []
                if column not in hashTable:
                    hashTable[column] = []
                if square not in hashTable:
                    hashTable[square] = []

                if board[i][j] not in hashTable[row]:
                    hashTable[row].append(board[i][j])
                else:
                    return False

                if board[i][j] not in hashTable[column]:
                    hashTable[column].append(board[i][j])
                else:
                    return False

                if board[i][j] not in hashTable[square]:
                    hashTable[square].append(board[i][j])
                else:
                    return False
    return True

# Declare variables for isValidSudoku function

board = [["5","3",".",".","7",".",".",".","."],["6",".",".","1","9","5",".",".","."],[".","9","8",".",".",".",".","6","."],["8",".",".",".","6",".",".",".","3"],["4",".",".","8",".","3",".",".","1"],["7",".",".",".","2",".",".",".","6"],[".","6",".",".",".",".","2","8","."],[".",".",".","4","1","9",".",".","5"],[".",".",".",".","8",".",".","7","9"]]

# Time the function

start_time = time.time()

print(isValidSudoku(board))

print("--- %s seconds ---" % (time.time() - start_time))
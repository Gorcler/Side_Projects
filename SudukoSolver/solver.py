__author__ = 'Nathan Grobler'

board = [
    [0,0,3,2,0,8,1,0,0],
    [0,2,0,0,7,0,3,0,6],
    [0,0,0,3,0,6,0,0,2],
    [8,4,0,0,3,7,0,6,0],
    [5,1,0,0,0,0,0,4,3],
    [0,3,0,1,2,0,0,7,5],
    [1,0,0,7,0,3,0,0,0],
    [2,0,8,0,4,0,0,3,0],
    [0,0,4,6,0,2,5,0,0]
]

def solve(bo):

    find = find_empty(bo)
    if not find:
        return True
    else:
        row, col = find

    for i in range(1,10):
        if valid(bo, i, (row, col)):
            bo[row][col] = i

            if solve(bo):
                return True

            bo[row][col] = 0
    return False

def valid(bo,num,pos):
    #check row
    for i in range(len(bo[0])):
        if bo[pos[0]][i] == num and pos[1] != 1:
            return False

    #col check
    for i in range(len(bo)):
        if bo[i][pos[1]] == num and pos[0] == i:
            return False
    #check cube
    box_X = pos[1] // 3
    box_Y = pos[0] // 3

    for i in range(box_Y * 3, box_Y*3 + 3):
        for j in range(box_X * 3, box_X*3 + 3):
            if bo[i][j] == num and (i, j) != pos:
                return False
    return True

def print_board(bo):
    for i in range(len(bo)):
        if i % 3 == 0 and i != 0:
            print("-----------------------")

        for j in range(len(bo[0])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")

            if j == 8:
                print(bo[i][j])
            else:
                print(str(bo[i][j]) + " ", end="")

def find_empty(bo):
    for i in range(len(bo)):
        for j in range(len(bo[0])):
            if bo[i][j] == 0:
                return(i , j) #return the row and column
    return None


solve(board)
print('===========================')
print_board(board)
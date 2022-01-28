puzzle = [[0,0,0,0,0,0,0,0,2],
          [0,0,1,0,0,6,0,0,5],
          [3,0,0,0,0,4,0,0,0],
          [2,9,0,4,0,0,3,0,0],
          [0,0,0,0,2,0,0,6,1],
          [5,0,0,7,0,0,0,0,0],
          [0,5,0,0,0,0,9,0,0],
          [9,0,4,0,0,1,0,5,0],
          [7,0,0,0,0,0,0,0,3]]

def print_puzzle(puzzle):
    for i in range(len(puzzle)):
        if i == 3 or i == 6:
            print ("----------------------")
        for j in range(len(puzzle[i])):
            if j == 3 or j == 6:
                print ("|", end=" ")
            print(puzzle[i][j], end=" ")
        print()

def find_empty(puzzle):
    for i in range(len(puzzle)):
        for j in range(len(puzzle[i])):
            if puzzle[i][j] == 0:
                return i, j
    
    return None

def isvalid(board, row, col, try_num):
    #check row
    for value in board[row]:
        if value == try_num:
            return False
    #check col
    for i in range(len(board)):
        if board[i][col] == try_num:
            return False
    #check box
    box_x = col//3
    box_y = row//3

    for i in range(box_y*3, box_y*3 + 3):
        for j in range(box_x*3, box_x*3 + 3):
            if board[i][j] == try_num and i != row and j != col:
                return False

    return True

def solve(puzzle):
    
    pos = find_empty(puzzle)
    if pos:
        i, j = pos
    else:
        return True
        
    for x in range(1,10):
        if isvalid(puzzle, i, j, x):
            puzzle[i][j] = x

            if solve(puzzle):
                return True
                
            puzzle[i][j] = 0
    
    return False



print_puzzle(puzzle)
solve(puzzle)
print()
print_puzzle(puzzle)
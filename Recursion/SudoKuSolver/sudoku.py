

def sudokuSolver(sudoku, row = 0, col = 0):

    # if we at the end of the row then we will print the sudoku solved solution
    if row == 9:
        print("SOLUTION:")
        display_sudoku(sudoku)
        return
    # when we are finshed with the row we will move to another row 
    if col == 9:
        sudokuSolver(sudoku, row + 1, 0)
        return
    # if is postion is already filled we will move to next postion
    if sudoku[row][col] > 0:
        sudokuSolver(sudoku, row, col + 1)
    else:
        # where 10 is exclusive
        for number in range(1, 10):
            if is_valid(sudoku, row, col, number):
                sudoku[row][col] = number
                sudokuSolver(sudoku, row, col + 1)
                # backtracking
                sudoku[row][col] = 0

def is_valid(sudoku, row, col, value):

    # to check in entire row
    for r in range(9):
        if sudoku[r][col] == value:
            return False

    # check in entire column
    for c in range(9):
        if sudoku[row][c] == value:
            return False

    # we need to check inside the box
    # this will help to get the pos to the start of the box
    box_r = row - (row % 3)
    box_c = col - (col % 3)

    # check inside the box
    for r in range(box_r, box_r + 3):
        for c in range(box_c, box_c + 3):
            if sudoku[r][c] == value:
                return False
    return True


sudoku = [[8, 1, 0, 0, 3, 0, 0, 2, 7], 
            [0, 6, 2, 0, 5, 0, 0, 9, 0], 
            [0, 7, 0, 0, 0, 0, 0, 0, 0], 
            [0, 9, 0, 6, 0, 0, 1, 0, 0], 
            [1, 0, 0, 0, 2, 0, 0, 0, 4], 
            [0, 0, 8, 0, 0, 5, 0, 7, 0], 
            [0, 0, 0, 0, 0, 0, 0, 8, 0], 
            [0, 2, 0, 0, 1, 0, 7, 5, 0], 
            [3, 8, 0, 0, 7, 0, 0, 4, 2]]

grid = [ [3, 0, 6, 5, 0, 8, 4, 0, 0], 
         [5, 2, 0, 0, 0, 0, 0, 0, 0], 
         [0, 8, 7, 0, 0, 0, 0, 3, 1], 
         [0, 0, 3, 0, 1, 0, 0, 8, 0], 
         [9, 0, 0, 8, 6, 3, 0, 0, 5], 
         [0, 5, 0, 0, 9, 0, 6, 0, 0], 
         [1, 3, 0, 0, 0, 0, 2, 5, 0], 
         [0, 0, 0, 0, 0, 0, 0, 7, 4], 
         [0, 0, 5, 2, 0, 6, 3, 0, 0] ]

def display_sudoku(sudoku):
    for r in range(9):
            for c in range(9):
                if sudoku[r][c]:
                    print(sudoku[r][c], end="  ")
                else:
                    print("  ", end=" ")

                if (c + 1)%3 == 0 and c + 1 < 9:
                    print("|", end=" ")
            print("")
            if (r + 1) % 3 == 0 and r + 1 < 9:
                print("------------------------------")

grid2 =[[ 0, 0, 4,   0, 0, 0,   0, 6, 7 ],
        [ 3, 0, 0,   4, 7, 0,   0, 0, 5 ],
        [ 1, 5, 0,   8, 2, 0,   0, 0, 3 ],
        [ 0, 0, 6,   0, 0, 0,   0, 3, 1 ],
        [ 8, 0, 2,   1, 0, 5,   6, 0, 4 ],
        [ 4, 1, 0,   0, 0, 0,   9, 0, 0 ],
        [ 7, 0, 0,   0, 8, 0,   0, 4, 6 ],
        [ 6, 0, 0,   0, 1, 2,   0, 0, 0 ],
        [ 9, 3, 0,   0, 0, 0,   7, 1, 0 ] ]
display_sudoku(sudoku)
sudokuSolver(sudoku) # solution 
print()
display_sudoku(grid)
sudokuSolver(grid) # solution 
print()
display_sudoku(grid2)
sudokuSolver(grid2) # solution 
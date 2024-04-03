def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid(board, row, col, num):
    # Check if the number is not in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(10)]:
        return False
    
    # Check if the number is not in the same 2x5 subgrid
    subgrid_row, subgrid_col = 2 * (row // 2), 5 * (col // 5)
    for i in range(subgrid_row, subgrid_row + 2):
        for j in range(subgrid_col, subgrid_col + 5):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(10):
        for j in range(10):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    # If there is no empty location, the puzzle is solved
    if row is None:
        return True
    
    for num in range(1, 11):
        if is_valid(board, row, col, num):
            board[row][col] = num
            
            # Recursively try to fill the rest of the board
            if solve_sudoku(board):
                return True
            
            # If the current placement leads to an invalid solution, backtrack
            board[row][col] = 0
    
    # If no number can be placed, backtrack
    return False

if __name__ == "__main__":
    import time

    #for first puzzle
    print('\n Solving first sudoku puzzle  ')
    start_time1 = time.time()
    # Example 10x10 Sudoku puzzle (0 represents empty cells)
    puzzle1 = [
        [3, 0, 10, 5, 0, 8, 4, 0, 0, 7],
        [0, 0, 0, 0, 0, 0, 0, 2, 1, 10],
        [0, 4, 5, 10, 0, 1, 3, 0, 0, 0],
        [1, 9, 0, 3, 0, 10, 8, 5, 0, 0],
        [0, 0, 0, 0, 9, 0, 2, 0, 5, 0],
        [0, 8, 3, 0, 5, 0, 1, 10, 7, 0],
        [0, 7, 0, 8, 3, 2, 0, 4, 0, 0],
        [5, 0, 0, 0, 2, 6, 0, 0, 0, 8],
        [0, 0, 8, 1, 0, 0, 0, 3, 0, 4],
        [7, 0, 0, 0, 0, 0, 6, 9, 8, 0]
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle1)

    if solve_sudoku(puzzle1):
        print("Solved Sudoku:")
        print_board(puzzle1)
    else:
        print("No solution exists.")
    print('Execution time for puzzle 1: ', time.time()-start_time1, 'sec')


 #for second  puzzle
    print('\n Solving second sudoku puzzle  ')
    start_time2 = time.time()
    # Example 10x10 Sudoku puzzle (0 represents empty cells)
    puzzle2 = [
       [0, 0, 6, 0, 8, 0, 0, 0, 0, 0],
[0, 0, 0, 5, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 3, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 9, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 1, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 5],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
[0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ]

    print("Sudoku Puzzle:")
    print_board(puzzle2)

    if solve_sudoku(puzzle2):
        print("Solved Sudoku:")
        print_board(puzzle2)
    else:
        print("No solution exists.")
    print('Execution time for puzzle 2: ', time.time()-start_time2, 'sec')


    #for third  puzzle
    print('\n Solving third sudoku puzzle  ')
    start_time3 = time.time()
    # Example 10x10 Sudoku puzzle (0 represents empty cells)
    puzzle3 = [
      [7, 4, 5, 3, 8, 6, 9, 2, 1, 0],
      [8, 9, 6, 5, 1, 2, 3, 7, 4, 0],
      [3, 2, 1, 7, 4, 9, 8, 6, 5, 0],
      [4, 8, 7, 1, 2, 3, 6, 5, 9, 0],
      [2, 5, 9, 6, 7, 8, 4, 1, 3, 0],
      [1, 6, 3, 9, 5, 4, 7, 8, 2, 0],
      [5, 3, 2, 8, 9, 7, 1, 4, 6, 0],
      [6, 1, 4, 2, 3, 5, 0, 9, 7, 0],
      [9, 7, 8, 4, 6, 1, 2, 3, 0, 0],
      [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ]

    print("Sudoku Puzzle:")
    print_board(puzzle3)

    if solve_sudoku(puzzle3):
        print("Solved Sudoku:")
        print_board(puzzle3)
    else:
        print("No solution exists.")
    print('Execution time for puzzle 3: ', time.time()-start_time3, 'sec')




    #for fourth  puzzle
    print('\n Solving fourth sudoku puzzle  ')
    start_time4 = time.time()
    # Example 10x10 Sudoku puzzle (0 represents empty cells)
    puzzle4 = [
    [0, 0, 7, 0, 0, 0, 0, 0, 0, 6],
    [0, 0, 0, 0, 0, 0, 0, 0, 4, 0],
    [0, 0, 0, 0, 0, 0, 0, 8, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 9, 0, 0],
    [0, 0, 6, 0, 0, 0, 5, 0, 0, 0],
    [0, 0, 0, 0, 0, 2, 0, 0, 0, 0],
    [0, 0, 0, 0, 8, 0, 0, 0, 0, 0],
    [0, 0, 0, 0, 0, 0, 0, 0, 0, 0],
    [0, 5, 0, 0, 0, 0, 0, 0, 0, 0],
    [9, 0, 0, 0, 0, 0, 0, 0, 0, 0]

    ]

    print("Sudoku Puzzle:")
    print_board(puzzle4)

    if solve_sudoku(puzzle4):
        print("Solved Sudoku:")
        print_board(puzzle4)
    else:
        print("No solution exists.")
    print('Execution time for puzzle 4: ', time.time()-start_time4, 'sec')


 
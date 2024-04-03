def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid(board, row, col, num):
    # Check if the number is not in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(8)]:
        return False
    
    # Check if the number is not in the same 2x4 subgrid
    subgrid_row, subgrid_col = 2 * (row // 2), 4 * (col // 4)
    for i in range(subgrid_row, subgrid_row + 2):
        for j in range(subgrid_col, subgrid_col + 4):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(8):
        for j in range(8):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    # If there is no empty location, the puzzle is solved
    if row is None:
        return True
    
    for num in range(1, 9):
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

    #for first sudoku puzzle
    print('\n solving first sudoku puzzle')
    start_time1=time.time()

    puzzle1 = [
        [0, 6, 8, 3, 0, 0, 4, 7],
        [0, 0, 0, 0, 6, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [8, 4, 0, 0, 5, 0, 6, 2],
        [0, 7, 6, 2, 0, 8, 0, 0],
        [0, 8, 0, 0, 0, 0, 0, 0],
        [2, 0, 7, 0, 0, 1, 5, 8],
        [4, 1, 0, 0, 3, 0, 0, 6]
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle1)

    if solve_sudoku(puzzle1):
        print("\nSolved Sudoku:")
        print_board(puzzle1)
    else:
        print("No solution exists.")
    print('Execution time for sudoku puzzle 1: ', time.time() - start_time1, 'sec')

     #for second sudoku puzzle
    print('\n solving second sudoku puzzle')
    start_time2=time.time()

    puzzle2 = [
        [0, 0, 8, 4, 0, 6, 2, 3],
        [3, 0, 0, 1, 5, 4, 0, 0],
        [1, 0, 2, 0, 0, 0, 0, 6],
        [0, 7, 0, 0, 2, 0, 8, 0],
        [0, 0, 7, 2, 8, 5, 0, 0],
        [0, 6, 0, 0, 4, 0, 0, 0],
        [8, 0, 5, 0, 0, 3, 1, 0],
        [0, 0, 3, 7, 0, 0, 5, 0]
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle2)

    if solve_sudoku(puzzle2):
        print("\nSolved Sudoku:")
        print_board(puzzle2)
    else:
        print("No solution exists.")
    print('Execution time for sudoku puzzle 2: ', time.time() - start_time2, 'sec')

   
    #for third sudoku puzzle
    print('\n solving third sudoku puzzle')
    start_time3=time.time()

    puzzle3 = [
        [4, 0, 0, 2, 6, 0, 8, 0],
        [0, 3, 0, 0, 0, 7, 0, 0],
        [0, 8, 5, 0, 2, 0, 1, 4],
        [0, 2, 6, 0, 0, 0, 0, 3],
        [0, 0, 2, 1, 0, 5, 4, 0],
        [3, 5, 0, 0, 8, 0, 0, 2],
        [0, 7, 0, 0, 0, 0, 0, 0],
        [5, 0, 1, 0, 0, 0, 3, 6]
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle3)

    if solve_sudoku(puzzle3):
        print("\nSolved Sudoku:")
        print_board(puzzle3)
    else:
        print("No solution exists.")
    print('Execution time for sudoku puzzle 3: ', time.time() - start_time3, 'sec')

  
   #for fourth sudoku puzzle
    print('\n solving fourth sudoku puzzle')
    start_time4=time.time()

    puzzle4 = [
        [0, 1, 0, 2, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 3],
        [0, 0, 4, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 5, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 6, 0],
        [0, 0, 0, 0, 0, 0, 0, 0],
        [0, 0, 0, 0, 0, 7, 0, 0],
        [0, 0, 0, 0, 0, 0, 0, 8]

    ]

    print("Sudoku Puzzle:")
    print_board(puzzle4)

    if solve_sudoku(puzzle4):
        print("\nSolved Sudoku:")
        print_board(puzzle4)
    else:
        print("No solution exists.")
    print('Execution time for sudoku puzzle 4: ', time.time() - start_time4, 'sec')

  #for fifth sudoku puzzle
    print('\n solving fifth sudoku puzzle')
    start_time5=time.time()

    puzzle5 = [
        [0, 3, 0, 4, 0, 7, 0, 0],
        [0, 0, 2, 0, 0, 0, 0, 5],
        [0, 0, 0, 0, 5, 0, 0, 3],
        [5, 0, 7, 0, 0, 0, 0, 0],
        [0, 1, 0, 0, 0, 0, 0, 4],
        [0, 0, 0, 8, 0, 0, 7, 0],
        [6, 0, 0, 0, 4, 0, 0, 0],
        [0, 0, 0, 0, 0, 8, 0, 0]
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle5)

    if solve_sudoku(puzzle5):
        print("\nSolved Sudoku:")
        print_board(puzzle5)
    else:
        print("No solution exists.")
    print('Execution time for sudoku puzzle 5: ', time.time() - start_time5, 'sec')

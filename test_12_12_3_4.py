def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid(board, row, col, num):
    # Check if the number is not in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(12)]:
        return False
    
    # Check if the number is not in the same 3x4 subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 4 * (col // 4)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 4):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(12):
        for j in range(12):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    # If there is no empty location, the puzzle is solved
    if row is None:
        return True
    
    for num in range(1, 13):
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

    # For the 12x12 Sudoku puzzle
    start_time2 = time.time()
    puzzle2 = [
        [0, 3, 0, 0, 0, 6, 0, 7, 0, 9, 0, 0],
        [0, 0, 2, 0, 5, 0, 0, 0, 0, 11, 0, 0],
        [0, 0, 0, 0, 0, 1, 0, 0, 8, 0, 0, 0],
        [0, 0, 0, 0, 0, 0, 12, 0, 0, 0, 5, 0],
        [0, 0, 0, 0, 0, 4, 0, 0, 0, 0, 0, 6],
        [0, 0, 7, 0, 9, 0, 0, 0, 0, 0, 0, 0],
        [0, 4, 0, 0, 0, 0, 0, 1, 0, 0, 0, 7],
        [0, 0, 0, 3, 0, 0, 0, 0, 0, 0, 2, 0],
        [0, 0, 0, 0, 0, 0, 8, 0, 9, 0, 0, 4],
        [0, 0, 5, 0, 0, 0, 0, 0, 0, 10, 0, 0],
        [0, 0, 0, 8, 0, 0, 0, 0, 0, 0, 0, 11],
        [0, 0, 0, 0, 0, 3, 0, 0, 0, 0, 0, 0]
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle2)

    if solve_sudoku(puzzle2):
        print("Solved Sudoku:")
        print_board(puzzle2)
    else:
        print("No solution exists.")
    print('Execution time for puzzle 2: ', time.time()-start_time2, 'sec')

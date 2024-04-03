def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid(board, row, col, num):
    # Check if the number is not in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(15)]:
        return False
    
    # Check if the number is not in the same 3x5 subgrid
    subgrid_row, subgrid_col = 3 * (row // 3), 5 * (col // 5)
    for i in range(subgrid_row, subgrid_row + 3):
        for j in range(subgrid_col, subgrid_col + 5):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(15):
        for j in range(15):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    # If there is no empty location, the puzzle is solved
    if row is None:
        return True
    
    for num in range(1, 16):
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

    # Example 15x15 Sudoku puzzle (0 represents empty cells)
    puzzle = [
        [9, 0, 0, 15, 0, 0, 6, 4, 0, 3, 7, 11, 0, 12, 10],
        [0, 3, 7, 0, 12, 11, 0, 0, 13, 0, 15, 4, 0, 8, 0],
        [0, 0, 5, 11, 0, 7, 8, 15, 1, 12, 3, 9, 6, 0, 0],
        [0, 0, 4, 1, 9, 12, 7, 3, 0, 5, 10, 8, 0, 0, 0],
        [0, 11, 0, 0, 7, 13, 10, 0, 4, 0, 14, 15, 1, 9, 3],
        [8, 13, 10, 3, 0, 0, 11, 14, 9, 6, 2, 0, 4, 5, 0],
        [0, 0, 0, 14, 4, 9, 15, 11, 2, 1, 12, 13, 0, 6, 0],
        [0, 1, 15, 10, 2, 8, 13, 0, 0, 4, 0, 0, 0, 7, 14],
        [11, 0, 9, 0, 8, 3, 14, 12, 0, 7, 5, 2, 15, 1, 4],
        [13, 0, 14, 0, 11, 6, 2, 0, 12, 8, 1, 10, 3, 15, 7],
        [0, 0, 0, 8, 10, 4, 5, 0, 14, 15, 6, 0, 13, 0, 9],
        [0, 9, 6, 12, 0, 0, 3, 0, 0, 0, 4, 5, 8, 14, 2],
        [1, 12, 11, 9, 6, 5, 4, 2, 8, 10, 0, 14, 7, 3, 0],
        [0, 15, 13, 7, 0, 0, 12, 6, 3, 0, 8, 0, 2, 4, 0],
        [0, 2, 8, 4, 0, 15, 1, 0, 0, 13, 0, 6, 12, 10, 5]
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle)

    start_time = time.time()
    if solve_sudoku(puzzle):
        print("Solved Sudoku:")
        print_board(puzzle)
    else:
        print("No solution exists.")
    print('Execution time: ', time.time()-start_time, 'sec')

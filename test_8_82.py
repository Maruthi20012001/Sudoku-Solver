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

    puzzle = [
        [2, 0, 0, 0, 1, 0, 3, 8],
        [3, 1, 6, 0, 0, 7, 0, 2],
        [0, 4, 5, 0, 0, 0, 8, 0],
        [1, 0, 0, 2, 6, 4, 7, 5],
        [0, 0, 4, 7, 5, 0, 0, 0],
        [5, 2, 0, 0, 7, 0, 6, 0],
        [0, 7, 1, 3, 0, 0, 0, 6],
        [4, 6, 0, 0, 8, 0, 0, 0]
    ]

    print("Sudoku Puzzle:")
    print_board(puzzle)

    start_time = time.time()
    if solve_sudoku(puzzle):
        print("\nSolved Sudoku:")
        print_board(puzzle)
    else:
        print("No solution exists.")
    print('Execution time: ', time.time() - start_time, 'sec')

def read_sudoku_from_file(filename):
    with open(filename, 'r') as file:
        lines = file.readlines()
        sudoku = []
        for line in lines:
            row = [int(num) for num in line.strip().split(',')]
            sudoku.append(row)
        return sudoku
    
def print_board(board):
    for row in board:
        print(" ".join(map(str, row)))
    print()

def is_valid(board, row, col, num):
    # Check if the number is not in the same row or column
    if num in board[row] or num in [board[i][col] for i in range(6)]:
        return False
    
    # Check if the number is not in the same 2x3 subgrid
    subgrid_row, subgrid_col = 2 * (row // 2), 3 * (col // 3)
    for i in range(subgrid_row, subgrid_row + 2):
        for j in range(subgrid_col, subgrid_col + 3):
            if board[i][j] == num:
                return False
    
    return True

def find_empty_location(board):
    for i in range(6):
        for j in range(6):
            if board[i][j] == 0:
                return i, j
    return None, None

def solve_sudoku(board):
    row, col = find_empty_location(board)
    
    # If there is no empty location, the puzzle is solved
    if row is None:
        return True
    
    for num in range(1, 7):
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
    import streamlit as st

    st.title("Sudoku Solver") 

    puzzle1 = st.file_uploader('Upload your txt file')  

    # puzzle1 = read_sudoku_from_file('1_6_6.txt')
    puzzle2 = read_sudoku_from_file('2_6_6.txt.txt')
    print(puzzle1)
    print_board(puzzle1)

    if solve_sudoku(puzzle1):
        print("Solved Sudoku:")
        print_board(puzzle1)
    else:
        print("No solution exists.")

    print_board(puzzle2)
    if solve_sudoku(puzzle2):
        print("Solved Sudoku:")
        print_board(puzzle2)
    else:
        print("No solution exists.")    
import numpy as np
import random
import math
# Parameters to be varied
pm = 0.20  # Probability of mutation
pc = 0.80  # Probability of crossover
fit_penalty = 1  # Penalty in objective function for fitness value
sum_penalty = 0  # Penalty in objective function for sum value
square_penalty = 0  # Penalty in objective function for sum of square value

# Declaring global variables
N = 9  # Order of the sudoku matrix
level = 0  # Level of the problem
popsize = 10 * N  # Size of population
solution_found_index = popsize  # To determine the chromosome number of solution
givens = 0  # To count the number of givens
resetpoint = 0

# Dynamic allocation of memories
init_pop_objval = np.zeros(popsize)  # Fitness matrix for initial population
cross_pop_objval = np.zeros(popsize)  # Fitness matrix for crossover population
mut_pop_objval = np.zeros(popsize)  # Fitness matrix for mutated population

# Sudoku and blueprint matrices
sudoku = np.zeros((N, N), dtype=int)
blueprint = np.zeros((N, N), dtype=int)

# Initialize random seed
random.seed()

# Functions


def generate_init_pop(sudoku, blueprint, N, popsize):
    # CREATING THE INITIAL POPULATION
    init_pop = [[[0 for _ in range(popsize)] for _ in range(N)] for _ in range(N)]

    for k in range(popsize):
        for i in range(N):
            for j in range(N):
                if blueprint[i][j] == 0:
                    temp = random.randint(1, N)
                    init_pop[i][j][k] = temp
                else:
                    init_pop[i][j][k] = sudoku[i][j]

    return init_pop


def remove_repetition(pop, blueprint, sudoku, N, popsize):
    for k in range(popsize):
        # Row-wise
        for i in range(N):1
            track = [0] * N

            for t in range(N):
                track[pop[i][t][k] - 1] = 1

            for j in range(N):
                if blueprint[i][j] == 1:
                    for l in range(N):
                        if pop[i][l][k] == sudoku[i][j] and blueprint[i][l] == 0:
                            for m in range(N):
                                if track[m] == 0:
                                    pop[i][l][k] = m + 1
                                    track[m] = 1
                                    break

        # Column-wise
        for j in range(N):
            track = [0] * N

            for t in range(N):
                track[pop[t][j][k] - 1] = 1

            for i in range(N):
                if blueprint[i][j] == 1:
                    for l in range(N):
                        if pop[l][j][k] == sudoku[i][j] and blueprint[l][j] == 0:
                            for m in range(N):
                                if track[m] == 0:
                                    pop[l][j][k] = m + 1
                                    track[m] = 1
                                    break

def objval(obj_val, pop, N, popsize, fitpenalty, sumpenalty, squarepenalty):
    pop_fitness = [0] * popsize  # List for fitness values of the population

    # Calculate fitness value of the population
    fit_val(pop_fitness, pop, N, popsize)

    max_fitness = (3 * N * N * (N - 1)) // 2  # Calculate maximum fitness value

    max_sum = N * (N + 1) // 2  # Finding max sum of all elements of row/col/sub-box

    max_squaresum = N * (N + 1) * (2 * N + 1) // 6  # Finding max sum of squares of all elements of row/col/sub-box

    # Declaring penalties
    fitness_penalty = 0

    # Total penalties
    sum_penalty = 0
    squaresum_penalty = 0

    # Intermediate sums
    sum_col = 0
    sum_row = 0
    sum_box = 0
    squaresum_col = 0
    squaresum_row = 0
    squaresum_box = 0

    # Calculating objective values of population under consideration
    for k in range(popsize):
        sum_penalty = 0
        squaresum_penalty = 0

        # Finding fitness value
        fitness_penalty = max_fitness - pop_fitness[k]

        # Finding sum penalties

        # Find for rows
        for i in range(N):
            sum_row = sum(pop[i][:][k])
            sum_penalty += abs(max_sum - sum_row)

        # Find for columns
        for j in range(N):
            sum_col = sum(pop[:][j][k])
            sum_penalty += abs(max_sum - sum_col)

        # Find for sub-box
        M = int(math.sqrt(N))
        for l in range(0, N, M):
            for m in range(0, N, M):
                sum_box = sum([pop[i][j][k] for i in range(l, l + M) for j in range(m, m + M)])
                sum_penalty += abs(max_sum - sum_box)

        # Finding square sum penalty
        # Find for rows
        for i in range(N):
            squaresum_row = sum(pop[i][j][k] ** 2 for j in range(N))
            squaresum_penalty += abs(max_squaresum - squaresum_row)

        # Find for columns
        for j in range(N):
            squaresum_col = sum(pop[i][j][k] ** 2 for i in range(N))
            squaresum_penalty += abs(max_squaresum - squaresum_col)

        # Find for sub-box
        for l in range(0, N, M):
            for m in range(0, N, M):
                squaresum_box = sum([pop[i][j][k] ** 2 for i in range(l, l + M) for j in range(m, m + M)])
                squaresum_penalty += abs(max_squaresum - squaresum_box)

        # Now finally finding the objective function value
        obj_val[k] = fitpenalty * fitness_penalty + sumpenalty * abs(sum_penalty) + squarepenalty * abs(squaresum_penalty)

    # Main for loop ends here
    del pop_fitness


def is_solution_found(obj_val, popsize):
    sol_found = False
    i = 0  # It keeps track of the index

    while not sol_found and i < popsize:
        if obj_val[i] == 0:
            sol_found = True
            return i
        else:
            i += 1

    return i  # If a solution is not found, the function returns popsize indicating no solution is found



def generate_cross_pop(init_pop, cross_pop, blueprint, N, popsize, pc):
    for k in range(popsize):  # Copying init_pop into cross_pop
        for i in range(N):
            for j in range(N):
                cross_pop[i][j][k] = init_pop[i][j][k]

    for k in range(0, popsize-1, 2):  # Crossover starts here
        for i in range(N):
            prob = random.random()
            if prob <= pc:  # Checking probability of crossover
                for j in range(N):
                    if blueprint[i][j] == 0:
                        cross_pop[i][j][k], cross_pop[i][j][k+1] = cross_pop[i][j][k+1], cross_pop[i][j][k]


def generate_mut_pop(cross_pop, mut_pop, blueprint, N, popsize, pm):
    for k in range(popsize):  # Copying cross_pop into mut_pop
        for i in range(N):
            for j in range(N):
                mut_pop[i][j][k] = cross_pop[i][j][k]

    for k in range(popsize):  # Mutation starts here
        for i in range(N):
            for j in range(N):
                if blueprint[i][j] == 0:
                    prob = random.random()
                    if prob <= pm:  # Checking probability of mutation
                        mut_pop[i][j][k] = random.randint(1, N)


def generate_final_pop(init_pop, mut_pop, final_pop, init_pop_objval, mut_pop_objval, N, popsize):
    temp = []  # Create a list for temp
    for i in range(2 * popsize):
        temp.append([0, 0, 0])  # Initialize temp with three columns

    for i in range(popsize):
        temp[i][0] = init_pop_objval[i]
        temp[i][1] = i + 1
        temp[i][2] = 0

    for i in range(popsize, 2 * popsize):
        temp[i][0] = mut_pop_objval[i - popsize]
        temp[i][1] = 0
        temp[i][2] = i - popsize + 1

    # Bubble sort to arrange in order of increasing fitness values, also keep track of indices
    for _ in range(2 * popsize - 1):
        for j in range(2 * popsize - 1):
            if temp[j][0] > temp[j + 1][0]:
                temp[j][0], temp[j + 1][0] = temp[j + 1][0], temp[j][0]
                temp[j][1], temp[j + 1][1] = temp[j + 1][1], temp[j][1]
                temp[j][2], temp[j + 1][2] = temp[j + 1][2], temp[j][2]

    # Copy chromosomes in order of increasing fitness values to final_pop
    for i in range(popsize):
        if temp[i][1] == 0:  # Copy from mut_pop
            for k in range(N):
                for j in range(N):
                    final_pop[k][j][i] = mut_pop[k][j][temp[i][2] - 1]
        elif temp[i][2] == 0:  # Copy from init_pop
            for k in range(N):
                for j in range(N):
                    final_pop[k][j][i] = init_pop[k][j][temp[i][1] - 1]



# Main function
def main():
    global level, resetpoint, N, popsize, solution_found_index, givens

    print("\n\t\t\t GENERALIZED SUDOKU SOLVER")
    print('Inside the main function')

    # Dynamic allocation of memories
    init_pop = np.zeros((N, N, popsize), dtype=int)
    cross_pop = np.zeros((N, N, popsize), dtype=int)
    mut_pop = np.zeros((N, N, popsize), dtype=int)
    final_pop = np.zeros((N, N, popsize), dtype=int)

    print("\n\n Enter the level of problem: \n")
    print("\t \"1\" for EASY Level.\n")
    print("\t \"2\" for MEDIUM Level.\n")
    print("\t \"3\" for HARD Level.\n ")
    print("\t \"4\" for EXTRA Problem.\n ")
    level = int(input())

    # Read sudoku from a file
    file_name = ""
    if level == 1:
        file_name = "./Easy.txt"
    elif level == 2:
        file_name = "Medium.txt"
    elif level == 3:
        file_name = "Hard.txt"
    elif level == 4:
        file_name = "Extra.txt"
    else:
        file_name = "Extra.txt"

    blueprint = [[0] * N for _ in range(N)]
    sudoku = [[0] * N for _ in range(N)]
    with open(file_name, "r") as readsudoku:
        for i in range(N):
            sudoku[i] = list(map(int, readsudoku.readline().split()))

    for i in range(N):
        for j in range(N):
            if sudoku[i][j] == 0:
                blueprint[i][j] = 0
            else:
                blueprint[i][j] = 1

    # Counting the number of givens in the problem
    givens = np.count_nonzero(blueprint == 1)

    # Defining reset point
    if givens <= 27:
        resetpoint = 2000
    elif 28 <= givens <= 29:
        resetpoint = 350
    elif 30 <= givens <= 31:
        resetpoint = 300
    elif givens >= 32:
        resetpoint = 200

    print("\n\n\n Wait while I solve the sudoku")

    # Reset
    dcount = 0
    while True:
        dcount += 1

        # Initial population
        generate_init_pop(sudoku, blueprint, N, popsize)
        # Remove repetition of givens from initial population
        remove_repetition(init_pop, blueprint, sudoku, N, popsize)

        print(".", end="", flush=True)

        # Iterations
        for _ in range(resetpoint):
            # Find objective value
            objval(init_pop_objval, init_pop, N, popsize, fit_penalty, sum_penalty, square_penalty)
            # Check for solution
            solution_found_index = is_solution_found(init_pop_objval, popsize)
            if solution_found_index != popsize:
                index = 1
                break

            # Crossover (Uniform Row Wise)
            generate_cross_pop(init_pop, cross_pop, blueprint, N, popsize, pc)
            # Remove repetition
            remove_repetition(cross_pop, blueprint, sudoku, N, popsize)
            # Find objective value
            objval(cross_pop_objval, cross_pop, N, popsize, fit_penalty, sum_penalty, square_penalty)
            # Check for solution
            solution_found_index = is_solution_found(cross_pop_objval, popsize)
            if solution_found_index != popsize:
                index = 2
                break

            # Mutation (Random Number Generation Mutation)
            generate_mut_pop(cross_pop, mut_pop, blueprint, N, popsize, pm)
            # Remove repetition
            remove_repetition(mut_pop, blueprint, sudoku, N, popsize)
            # Find objective value
            objval(mut_pop_objval, mut_pop, N, popsize, fit_penalty, sum_penalty, square_penalty)
            # Check for solution
            solution_found_index = is_solution_found(mut_pop_objval, popsize)
            if solution_found_index != popsize:
                index = 3
                break

            # Elitism (Complete Elitism)
            generate_final_pop(init_pop, mut_pop, final_pop, init_pop_objval, mut_pop_objval, N, popsize)
            # Copying the Final Population into Initial Population
            init_pop[:, :, :] = final_pop[:, :, :]

        if solution_found_index != popsize:
            break

    # Solution found
    if index != 0:
        print("\n\n\n\t THE SUDOKU IS SOLVED.")
        print("\n\n\t Solution found in Iteration No. : ", dcount)
        print("\n\t The solution is as follows:\n\n")
        for i in range(N):
            print("\t\t", end="")
            for j in range(N):
                if index == 1:
                    print(init_pop[i, j, solution_found_index], "    ", end="")
                elif index == 2:
                    print(cross_pop[i, j, solution_found_index], "    ", end="")
                elif index == 3:
                    print(mut_pop[i, j, solution_found_index], "    ", end="")
            print("\n")

        print("\a\a")

    else:
        print("\n\n\n\t Sorry, the Sudoku could not be solved within 50000 iterations.\n\a")

    # Deallocating the dynamic memory

    # For init_pop
    init_pop = np.zeros((N, N, popsize), dtype=int)

    # For cross_pop
    cross_pop = np.zeros((N, N, popsize), dtype=int)

    # For mut_pop
    mut_pop = np.zeros((N, N, popsize), dtype=int)

    # For final_pop
    final_pop = np.zeros((N, N, popsize), dtype=int)

    # Delete objective value matrix of init_pop
    init_pop_objval = np.zeros(popsize)

    # For cross_pop_objval
    cross_pop_objval = np.zeros(popsize)

    # For mut_pop_objval
    mut_pop_objval = np.zeros(popsize)

    # For sudoku matrix
    sudoku = np.zeros((N, N), dtype=int)

    # For blueprint matrix
    blueprint = np.zeros((N, N), dtype=int)

    # Delete dynamic memory
    # For sudoku matrix
    # Deallocate the dynamic memory.
    for i in range(N):
        del sudoku[i]
    del sudoku

    # For blueprint matrix
    for i in range(N):
        del blueprint[i]
    del blueprint

    # For init_pop
    for i in range(N):
        for j in range(N):
            del init_pop[i][j]
        del init_pop[i]
    del init_pop

    # For cross_pop
    for i in range(N):
        for j in range(N):
            del cross_pop[i][j]
        del cross_pop[i]
        del cross_pop

    # For mut_pop
    for i in range(N):
        for j in range(N):
            del mut_pop[i][j]
        del mut_pop[i]
    del mut_pop

    # For final_pop
    for i in range(N):
        for j in range(N):
            del final_pop[i][j]
        del final_pop[i]
    del final_pop

    # Delete objective value matrix of init_pop
    del init_pop_objval

    # For cross_pop_objval
    del cross_pop_objval

    # For mut_pop_objval
    del mut_pop_objval

    # Output
    print("\n")
    input("Press Enter to exit")

if __name__ == "__main__":
    main()
                 
import random

def generate_population(size):
    population = []
    for _ in range(size):
        individual = list(range(1, 10))
        random.shuffle(individual)
        population.append(individual)
    return population

def crossover(parent1, parent2):
    crossover_point = random.randint(0, 8)
    child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    return child

def mutate(individual, mutation_rate):
    if random.random() < mutation_rate:
        swap_indices = random.sample(range(9), 2)
        individual[swap_indices[0]], individual[swap_indices[1]] = individual[swap_indices[1]], individual[swap_indices[0]]

def fitness(board):
    conflicts = 0
    for i in range(9):
        conflicts += len(set(board[i])) - 9  # Check row
        conflicts += len(set(board[j][i] for j in range(9))) - 9  # Check column

    for i in range(0, 9, 3):
        for j in range(0, 9, 3):
            conflicts += len(set(board[x][y] for x in range(i, i + 3) for y in range(j, j + 3))) - 9  # Check subgrid

    return conflicts

def genetic_algorithm(initial_population_size, generations, mutation_rate):
    population = generate_population(initial_population_size)

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x))
        fittest = population[0]

        if fitness(fittest) == 0:
            print("Solution found in generation", generation)
            return fittest

        new_population = [fittest]

        while len(new_population) < initial_population_size:
            parent1 = random.choice(population)
            parent2 = random.choice(population)
            child = crossover(parent1, parent2)
            mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    print("No solution found")
    return None

def display_board(board):
    for row in board:
        print(" ".join(map(str, row)))

if __name__ == "__main__":
    # Example Sudoku board (0 represents an empty cell)
    sudoku_board = [
        [5, 3, 0, 0, 7, 0, 0, 0, 0],
        [6, 0, 0, 1, 9, 5, 0, 0, 0],
        [0, 9, 8, 0, 0, 0, 0, 6, 0],
        [8, 0, 0, 0, 6, 0, 0, 0, 3],
        [4, 0, 0, 8, 0, 3, 0, 0, 1],
        [7, 0, 0, 0, 2, 0, 0, 0, 6],
        [0, 6, 0, 0, 0, 0, 2, 8, 0],
        [0, 0, 0, 4, 1, 9, 0, 0, 5],
        [0, 0, 0, 0, 8, 0, 0, 7, 9]
    ]

    initial_population_size = 100
    generations = 1000
    mutation_rate = 0.1

    initial_population = generate_population(initial_population_size)
    solution = genetic_algorithm(initial_population_size, generations, mutation_rate)

    if solution:
        print("Sudoku Solution:")
        display_board(solution)

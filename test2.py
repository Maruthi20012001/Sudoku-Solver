import random

def generate_population(size, puzzle):
    population = []
    for _ in range(size):
        individual = []
        for row in puzzle:
            individual.extend([val if val != 0 else random.randint(1, 6) for val in row])
        population.append(individual)
    return population

def fitness(individual, puzzle):
    conflicts = 0
    for i in range(0, len(individual), 6):
        row = set([val for val in individual[i:i+6] if val != 0])
        conflicts += len(row) - len(set([val for val in individual[i:i+6] if val != 0]))

    for i in range(6):
        col = set([individual[j] for j in range(i, len(individual), 6) if individual[j] != 0])
        conflicts += len(col) - len(set([individual[j] for j in range(i, len(individual), 6) if individual[j] != 0]))

    return conflicts

def crossover(parent1, parent2):
    crossover_point = random.randint(0, len(parent1))
    child = parent1[:crossover_point] + parent2[crossover_point:]
    
    # Ensure unique values in rows
    for i in range(0, len(child), 6):
        row_values = set()
        for j in range(i, i+6):
            if child[j] != 0 and child[j] in row_values:
                available_values = list(set(range(1, 7)) - row_values)
                child[j] = random.choice(available_values)
            row_values.add(child[j])

    return child

def mutate(individual, mutation_rate):
    for i in range(len(individual)):
        if random.random() < mutation_rate and individual[i] == 0:
            row = i // 6
            valid_values = list(set(range(1, 7)) - set([individual[j] for j in range(row*6, (row+1)*6)]))
            if valid_values:
                individual[i] = random.choice(valid_values)
    return individual

def genetic_algorithm(puzzle, population_size=100, generations=1000, mutation_rate=0.1):
    population = generate_population(population_size, puzzle)

    for generation in range(generations):
        population = sorted(population, key=lambda x: fitness(x, puzzle))
        if fitness(population[0], puzzle) == 0:
            print("Solution found in generation", generation)
            return population[0]

        new_population = [population[0]]  # Elitism - keep the best individual
        while len(new_population) < population_size:
            parent1 = random.choice(population[:10])  # Select from the top 10 individuals
            parent2 = random.choice(population[:10])
            child = crossover(parent1, parent2)
            child = mutate(child, mutation_rate)
            new_population.append(child)

        population = new_population

    print("Solution not found.")
    return None

# Example puzzle with missing values represented as zeros
sudoku_puzzle = [
    [1, 0, 0, 0, 5, 6],
    [0, 0, 6, 0, 2, 3],
    [0, 3, 4, 0, 0, 0],
    [5, 0, 0, 0, 0, 4],
    [3, 4, 0, 6, 0, 2],
    [0, 1, 0, 0, 4, 0]
]

flat_puzzle = [val for row in sudoku_puzzle for val in row]
solution = genetic_algorithm(sudoku_puzzle, population_size=200, generations=1000, mutation_rate=0.2)
print("Original Puzzle:")
for row in sudoku_puzzle:
    print(row)
print("\nSolution:")
for i in range(0, len(solution), 6):
    print(solution[i:i+6])

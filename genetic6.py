import random

def create_individual():
    """Create a random individual representing a 6x6 Sudoku solution."""
    individual = [i + 1 for i in range(6)] * 6
    random.shuffle(individual)
    return individual

def fitness(individual):
    """Calculate the fitness of an individual (Sudoku solution)."""
    conflicts = 0

    for i in range(6):
        row = set(individual[i * 6: (i + 1) * 6])
        conflicts += 6 - len(row)

        col = set(individual[i::6])
        conflicts += 6 - len(col)

    return conflicts

def crossover(parent1, parent2):
    """Perform crossover between two parents to produce offspring."""
    crossover_point = random.randint(1, 5)
    child = parent1[:crossover_point] + [gene for gene in parent2 if gene not in parent1[:crossover_point]]
    return child

def mutate(individual):
    """Perform mutation on an individual."""
    mutation_point1, mutation_point2 = random.sample(range(6), 2)
    individual[mutation_point1], individual[mutation_point2] = individual[mutation_point2], individual[mutation_point1]
    return individual

def print_sudoku(solution):
    """Print the Sudoku solution in a readable format."""
    for i in range(6):
        print(solution[i*6 : (i+1)*6])

if __name__ == "__main__":
    # Example of a 6x6 Sudoku puzzle (0 represents an empty cell).
    sudoku_puzzle = [
        [0, 0, 0, 4, 6, 0],
        [3, 6, 0, 0, 0, 0],
        [0, 0, 5, 0, 0, 0],
        [5, 0, 0, 0, 0, 6],
        [0, 0, 0, 0, 0, 0],
        [0, 2, 0, 0, 0, 4]
    ]

    initial_individual = [value if value != 0 else 0 for row in sudoku_puzzle for value in row]

    def genetic_algorithm(population_size, generations):
        """Run the genetic algorithm to solve the Sudoku puzzle."""
        population = [create_individual() for _ in range(population_size)]

        for generation in range(generations):
            population = sorted(population, key=fitness)
            if fitness(population[0]) == 0:
                print("Solution found!")
                print("Generation:", generation + 1)
                print("Solution:")
                print_sudoku(population[0])
                break

            new_population = [population[0]]  # Keep the best individual

            for _ in range(population_size - 1):
                parent1 = random.choice(population[:5])
                parent2 = random.choice(population[:5])
                child = crossover(parent1, parent2)

                if random.random() < 0.1:
                    child = mutate(child)

                new_population.append(child)

            population = new_population

        else:
            print("Solution not found.")

    genetic_algorithm(population_size=50, generations=1000)



# SIMPLY RUN THE CODE , NO ADDITIONS STEPS INVOLVED

import numpy as np

# Define the Sphere function to be optimized
def sphere_function(x):
    return np.sum(x**2)

# Define the Clonal Selection Algorithm
def clonal_selection_algorithm(objective_function, dim, pop_size, max_iter, mutation_rate):
    # Initialize population randomly
    population = np.random.uniform(-5, 5, size=(pop_size, dim))
    # print(population)
    # return
    
    for iter in range(max_iter):
        # Evaluate fitness for each individual
        fitness = np.array([objective_function(ind) for ind in population])
        # print(fitness)
        # break
        
        # Sort population based on fitness
        sorted_indices = np.argsort(fitness)
        population = population[sorted_indices]
        fitness = fitness[sorted_indices]
        # print(fitness)
        # break

        # ('p1',1) ('p2',3) ....

        

        # Clone individuals based on their fitness
        num_clones = int(pop_size * 0.5)
        clones = population[:num_clones]
        
        # Mutate clones
        mutated_clones = clones + np.random.normal(scale=mutation_rate, size=clones.shape)
        
        # Select the best individuals from the original population and mutated clones
        new_population = np.vstack((population[-num_clones:], mutated_clones))
        
        population = new_population
    
    # Return the best solution found
    best_solution = population[np.argmin(fitness)]
    best_fitness = fitness.min()

    # min fitness -> best
    
    return best_solution, best_fitness

# Define parameters
dim = 5           # Dimensionality of the problem
pop_size = 100     # Population size
max_iter = 100     # Maximum number of iterations
mutation_rate = 0.1  # Mutation rate

# Run Clonal Selection Algorithm
best_solution, best_fitness = clonal_selection_algorithm(sphere_function, dim, pop_size, max_iter, mutation_rate)

print("Best solution:", best_solution)
print("Best fitness:", best_fitness)

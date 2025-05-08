import numpy as np

def sphere_function(x):
    return np.sum(x**2)

def find_best_population(obj_fun, pop_size, dim_size, iters, mutation_rate):
    population = np.random.uniform(-5, 5, size=(pop_size, dim_size))
    # print(population)

    for _ in range(iters):
        fitness = np.array([obj_fun(individual) for individual in population])

        sorted_indices = np.argsort(fitness)
        sorted_fitness = fitness[sorted_indices]
        sorted_population = population[sorted_indices]

        clones = sorted_population[:pop_size//2]
        mutated_clones = clones + np.random.normal(scale=mutation_rate)

        new_population = np.vstack((mutated_clones, clones[pop_size//2:]))

        population = new_population
    
    best_individual = np.min(population)
    best_fitness = obj_fun(best_individual)

    return best_individual, best_fitness

pop_size = 100
dim_size = 5
iters = 100
mutation_rate = 0.1

best_individual, best_fitness = find_best_population(sphere_function, pop_size=pop_size, dim_size=dim_size, iters=iters, mutation_rate=mutation_rate)

print("Best Individual:", best_individual)
print("Best possible fitness:", best_fitness)

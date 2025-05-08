import numpy as np
from deap import tools, creator, algorithms, base

def evaluate(individual):
    x = individual[0]
    return x * float(np.sin(x)),

creator.create("FitnessMax", base.Fitness, weights = [1.0])
creator.create("Individual", list, fitness=creator.FitnessMax)

toolbox = base.Toolbox()
toolbox.register("attr_float", np.random.uniform, 0, 10)
toolbox.register("individual", tools.initRepeat, creator.Individual, toolbox.attr_float, n=1)
toolbox.register("population", tools.initRepeat, list, toolbox.individual)

toolbox.register("evaluate", evaluate)
toolbox.register("mate", tools.cxBlend, alpha = 0.5)
toolbox.register("mutate", tools.mutGaussian, mu = 0, sigma = 1, indpb = 0.1)
toolbox.register("select", tools.selTournament, tournsize = 3)

pop = toolbox.population(n=10)
algorithms.eaSimple(pop, toolbox, cxpb=0.5, mutpb=0.2, ngen = 10)
best = tools.selBest(pop, k = 1)[0]
print("best:", best[0])
print("fitness value:", evaluate(best))
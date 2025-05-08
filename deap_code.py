import random
import numpy as np
from deap import base,tools,algorithms,creator

# Fitness Function
def evaluate(individual):
    x = individual[0]
    return x * np.sin(x),

# Deap Setup
creator.create("FitnessMax",base.Fitness,weights=[1.0])
creator.create("individual",list,fitness=creator.FitnessMax)

toolbox=base.Toolbox()
toolbox.register("attr_float",random.uniform,0,10)
toolbox.register("individual", tools.initRepeat, creator.individual, toolbox.attr_float, 1)
toolbox.register("population",tools.initRepeat,list,toolbox.individual)

# Ga Operators
toolbox.register("evaluate",evaluate)
toolbox.register("mate",tools.cxBlend,alpha=0.5)
toolbox.register("mutate",tools.mutGaussian,mu=0,sigma=1.0,indpb=1.0)
toolbox.register("select",tools.selTournament,tournsize=3)

# Main execution
pop = toolbox.population(n=3)
# print("\nbefore:",pop)
# print("evaluation:",[round(evaluate(individual)[0],2) for individual in pop])
algorithms.eaSimple(pop,toolbox,cxpb=0.5,mutpb=0.2,ngen=10,verbose=False)
# print("\nafter:",pop)
# print("evaluation:",[round(evaluate(individual)[0],2) for individual in pop])

# Results
best = tools.selBest(pop,k=1)[0]
print("\nBest x: ",best[0])
print("Best fitness: ",evaluate(best)[0])

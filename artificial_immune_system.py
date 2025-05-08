import numpy as np

def create_antibody(size):
  return np.random.rand(size) 

def euclidean_distance(a1, a2):
  return np.sum((a1 - a2) ** 2)


# Affinity (closeness)
def affinity(antibody, datapoint):
  distance = euclidean_distance(antibody, datapoint)
  return 1 / (1 + distance)


# Simulate sensor data with potential damage (replace with actual data)
healthy_data = np.array([[1.0, 2.0, 3.0], [1.1, 1.9, 3.2]])
damaged_data = np.array([[1.2, 1.7, 2.8], [1.4, 1.5, 3.5]])

num_antibodies = 10
antibody_population = [create_antibody(healthy_data.shape[1]) for i in range(num_antibodies)]
 
for i in range(2):
  healthy_affinities = np.array([affinity(ab, datapoint) for ab in antibody_population for datapoint in healthy_data])
  # Select top 'n' antibodies based on affinity (healthy data)
  # print(list(zip(antibody_population, healthy_affinities)))
  top_antibodies = sorted(zip(antibody_population, healthy_affinities), key=lambda x: x[1], reverse=True)[:num_antibodies//2]
  # Clone and introduce random mutations (simplified)
  new_population = []
  for ab, i in top_antibodies:
    new_population.append(ab + np.random.randn(ab.shape[0]) * 0.1)  # Introduce small mutation
    
  antibody_population = new_population
  print(antibody_population.__len__())

# Check affinity for damaged data
damaged_affinities = [affinity(ab, damaged_data[0]) for ab in antibody_population]
# Identify potential damage based on high affinity for damaged data
potential_damage_index = damaged_affinities.index(max(damaged_affinities))
print("Potential damage detected with antibody:", antibody_population[potential_damage_index])

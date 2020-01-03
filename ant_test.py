import numpy as np
from antColony import AntColony

if __name__ == '__main__':
    distances = np.array([[0, 5, 2, 5, 7],
                          [2, 0, 4, 8, 2],
                          [2, 4, 0, 1, 5],
                          [5, 8, 1, 0, 2],
                          [7, 2, 3, 1, 0]])

    ant = AntColony(5, 12, 0.4, 0.5, 0.25, 1, distances)
    print(ant.antSolver())

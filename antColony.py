import random
import math
import numpy as np

class AntColony():
    def __init__(self, antsCountity, generations, alfa, beta, evaporationRatio, pheromoneZero, graph):
        """
        :antsCountity:
        :generations:
        :alfa - wzgledny wplyw wartosci feromonu:
        :beta - wzgledny wplyw wartosci heurystycznej:
        :evaporationRatio - wspolczynnik parowania feromonu:
        :bestAntValue - najlepsza uzyskana jakosc sciezki:
        :bestRoute - najlepsza znaleziona sciezka:
        :pheromoneZero - wartosc poczatkowa ilosci feromonu:
        """

        self.antsCountity = antsCountity
        self.generations = generations
        self.alfa = alfa
        self.beta = beta
        self.evaporationRatio = evaporationRatio
        self.pheromoneZero = pheromoneZero
        self.graph = graph
        self.bestAntValue = math.inf
        self.bestRoute = []
        self.bestDelta = 0.0


    def antSolver(self):
        """
        :network - graf w postaci macierzy, odpowiadajacy sieci miast wraz z wagami krawedzi:
        """
        #Inicjalizacja macierzy feromonu wartoscia poczaktowa
        self.pheromoneMatrix = np.random.randn(*self.graph.shape)
        for i in range(len(self.pheromoneMatrix)):
            for j in range(len(self.pheromoneMatrix[i])):
                self.pheromoneMatrix[i][j] = self.pheromoneZero

        #ants = np.array([])
        #for i in range(self.antsCountity):
        #    ants.append(Ant(self, network, [0,0], [3,3]))

        for iter in range(self.generations):
            # Tworzenie mrowek
            ants = []
            for i in range(self.antsCountity):
                ants.append(Ant(self, 0, 4))

            #Symulacja sciezki kazdej mrowki
            for i in range(len(ants)):
                while(ants[i].end != 1):
                    ants[i].nextNode()
                ants[i].delta = 1/ants[i].routeCost
                #Sprawdzanei jakosci znalezionej sciezki przez dana mrowke
                if ants[i].routeCost < self.bestAntValue:
                    self.bestAntValue = ants[i].routeCost
                    self.bestRoute = ants[i].route

            #Aktualizacja macierzy feromonu
            self.pheromoneUpdate(ants)

        return self.bestRoute, self.bestAntValue


    def pheromoneUpdate(self, ants):
        deltaSum = 0.0
        for k in range(self.antsCountity):
            deltaSum += ants[k].delta
        for i in range(len(self.pheromoneMatrix)):
            for j in range(len(self.pheromoneMatrix[i])):
                self.pheromoneMatrix[i][j] += (1-self.evaporationRatio)*self.pheromoneMatrix[i][j] + deltaSum + self.evaporationRatio*self.bestDelta

class Ant():
    def __init__(self, colony, startNode, finishNode):
        self.colony = colony
        self.routeCost = 0.0
        self.delta = 0.0
        self.route =  []
        self.actualNode = startNode
        self.finishNode = finishNode
        self.end = 0

        self.route.append(self.actualNode) #Wpisanie do sciezki poczatkowego wezla
        
    #Wybranie kolejnego wezla w sciezce
    def nextNode(self):
        allowed = []
        for i in range(len(self.colony.graph)):
            if self.colony.graph[self.actualNode][i] != 0:
                inRoute = 0
                for j in range(len(self.route)):
                    if self.route[j] == i:
                        inRoute = 1
                        
                if inRoute == 0:
                    allowed.append(i)
  
        probabilities = self.nodeProbabilities(allowed)

        randNumber = random.random()

        for i, probability in enumerate(probabilities):
            randNumber -= probability
            if randNumber <= 0:
                pickedNode = allowed[i]
                break
        self.routeCost += self.colony.graph[self.actualNode][pickedNode]
        self.actualNode = pickedNode
        self.route.append(self.actualNode)
        
        if self.actualNode == self.finishNode:
            self.end = 1

    #Obliczenie prawdpodobniestwa wyboru danego wezla
    def nodeProbabilities(self, allowed):
        probabilities = []
        probabilitySum = 0.0
        for i, node in enumerate(allowed):
            propability = (self.colony.pheromoneMatrix[self.actualNode][node])**self.colony.alfa * \
                self.heuristic(node)**self.colony.beta
            probabilities.append(propability)

        probabilitySum = sum(probabilities)
        for i in range(len(allowed)):
            probabilities[i] = probabilities[i]/probabilitySum

        return probabilities

    #Funkcja heurystyczna
    def heuristic(self, wezel):
        return 0.9


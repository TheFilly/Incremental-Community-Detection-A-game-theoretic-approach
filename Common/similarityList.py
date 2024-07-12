import numpy as np
import time
from numba import jit

from Common.adjacencyMatrix import getAdjMatrix
from Common.agent import Agent

global similarityList

"""
Calculates the whole Similarity List 
Input: List of Agents, Number of Nodes and the Adjacency Matrix
Output: SimilarityList
"""


def createSimilarityList(agents, numNodes, adjacencyMatrix):
    global similarityList

    adjMatrix = getAdjMatrix()

    start = time.time()
    similarityList = np.zeros((numNodes, numNodes), dtype=float)

    for i in range(numNodes):
        print(f"{i} / {numNodes}")
        for j in range(i + 1, numNodes):
            x = calculateSimilarities(agents[i].id, agents[j].id, adjMatrix)
            similarityList[i, j] = x
            similarityList[j, i] = x

    dur = time.time() - start

    print(f"Similarity List created in: {dur} seconds")


"""
Calculates Similarities between two agents
Input: Two Nodes and a Numpy Adjacency Matrix
Output: Neighborhood Similarity (double)

All of the following equations are from paper ACM Alvari 2014
"""


@jit
def calculateSimilarities(n1, n2, adjMatrix):
    # w = number of common neighbours
    neighbors_node1 = adjMatrix[n1, :] == 1
    neighbors_node2 = adjMatrix[n2, :] == 1
    w = np.sum(neighbors_node1 & neighbors_node2)

    # a = 1 if a1 and a2 adjacent, 0 if not
    a = adjMatrix[n1][n2]

    # m = numbers of edges at t
    m = np.sum(adjMatrix) // 2

    # d = degree of node (edges that connect to node)
    d1 = np.sum(adjMatrix[n1, :])
    d2 = np.sum(adjMatrix[n2, :])

    if a == 1:  # If nodes are neighbors
        if w >= 1.0:
            temp = w * (1.0 - ((d1 * d2) / (2.0 * m)))
            return max(0, min(1, temp))
        else:
            return d1 * d2 / (4.0 * m)
    else:  # If nodes are not neighbors
        if w >= 1.0:
            n = float(len(adjMatrix))
            return w / n
        else:
            return -d1 * d2 / (4.0 * m)


"""
Returns similarity value between two nodes
"""


def getSimilarity(n1, n2):
    return similarityList[n1][n2]


"""
Returns similarity list
"""


def getSimilarityList():
    return similarityList


"""
Changes the similarity list
"""


def setSimilarityList(simList):
    global similarityList
    similarityList = simList


"""
Updates the Similarity List based on one agents row/column
"""


def updateSimilarityList(n1: Agent, agents, numNodes):
    adjMatrix = getAdjMatrix()
    for i in (j for j in range(numNodes) if j != n1.id):
        x = calculateSimilarities(n1.id, agents[i].id, adjMatrix)
        similarityList[i, n1.id] = x
        similarityList[n1.id, i] = x

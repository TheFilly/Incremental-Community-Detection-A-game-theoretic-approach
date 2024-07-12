import numpy as np
from numba import jit

global adjMatrix

"""
Create Adjacency Matrix from a text file with format: node1 node2
Input: File Path and Number of Nodes in Graph
Output: Numpy Array Adjacency Matrix
"""


def createAdjacencyMatrix(file_path, numNodes):
    global adjMatrix

    adjMatrix = np.zeros((numNodes, numNodes), dtype=int)
    with open(file_path, 'rb') as f:
        for line in f:
            weight, node1, node2 = map(int, line.strip().split())
            adjMatrix[node1 - 1, node2 - 1] = 1
            adjMatrix[node2 - 1, node1 - 1] = 1
    return adjMatrix


"""
Create Adjacency Matrix from a text file with format: node1 node2
Input: File Path
Output: Numpy Array Adjacency Matrix
"""


def haggleAdjacencyMatrix(file_path):
    global adjMatrix

    n = 0
    with open(file_path, 'rb') as f:
        for line in f:
            node1, node2 = map(int, line.strip().split()[1:])
            n = max(n, node1, node2)
    adjMatrix = np.zeros((n, n))

    with open(file_path, 'rb') as f:
        for line in f:
            edge_weight, node1, node2 = map(int, line.strip().split())
            adjMatrix[node1 - 1][node2 - 1] = 1
            adjMatrix[node2 - 1][node1 - 1] = 1

    return adjMatrix


"""
Create Adjacency Matrix from a text file with format: node1 node2
Input: File Path
Output: List of Updated Agents
"""


def updateAdjacencyMatrix(file_path, agents):
    global adjMatrix

    agentsDict = {}
    updatedAgents = []

    with open(file_path, 'rb') as f:
        for line in f:
            edge_weight, node1, node2 = map(int, line.strip().split())
            adjMatrix[node1 - 1][node2 - 1] = 1
            adjMatrix[node2 - 1][node1 - 1] = 1
            updatedAgents = getUpdatedAgents((node1 - 1), (node2 - 1), agents, updatedAgents)

    for agent in updatedAgents:
        agentsDict[agent.id] = agent

    return list(agentsDict.values())


"""
Returns a list of neighbors for a given node index from an adjacency matrix.
Input:adjacencyMatrix, The index of the node
Output: list of neighbors
"""


def get_neighbors(index, agents):
    neighbors = []
    for i in range(len(adjMatrix)):
        if adjMatrix[index, i] == 1:
            neighbors.append(agents[i])
    return neighbors


"""
Returns a list of updated agents based on changes in a matrix
Input: 2 affected agents, list of agents and an list to add the values to
Output: list of affected neighbors
"""


def getUpdatedAgents(n1, n2, agents, updatedAgents):
    agents1 = get_neighbors(n1, agents)
    agents2 = get_neighbors(n2, agents)
    unique_agents = {agent.id: agent for agent in agents1 + agents2}
    for a in list(unique_agents.values()):
        updatedAgents.append(a)
    return updatedAgents


"""
Calculate the number of common neighbors of two nodes in a graph
Input: 2 nodes(int): number of these nodes and the Adjacency Matrix of the graph
Output: Common neighbors of these nodes (int)
"""


def calculateCommonNeighbours(node1, node2):
    neighbors_node1 = adjMatrix[node1, :] == 1
    neighbors_node2 = adjMatrix[node2, :] == 1
    common_neighbors = np.sum(neighbors_node1 & neighbors_node2)
    return common_neighbors


"""
Calculate the number of edges in a graph
Input: Numpy Array Adjacency Matrix
Output: Number of edges in that matrix (int)
"""


def calculateNumberOfEdges():
    num_edges = np.sum(adjMatrix) // 2
    return num_edges


"""    
Calculate the degree of a node in a graph ( the number of edges going in/out of a node )
Input: node(int): Number of the Node and the Adjacency Matrix of the graph
Output: Degree of node (int)
"""


def calculateNodeDegree(node):
    degree = np.sum(adjMatrix[node, :])
    return degree


"""    
Returns 1 if nodes are neighbors, 0 else
"""


def getAdjMatrixValue(node1, node2):
    return adjMatrix[node1, node2]


"""    
Returns the adjacency matrix
"""


@jit
def getAdjMatrix():
    return adjMatrix

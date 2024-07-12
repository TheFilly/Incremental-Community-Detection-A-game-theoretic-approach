import networkx as nx
import numpy as np

from Common.adjacencyMatrix import haggleAdjacencyMatrix

"""
Runs Louvain on a static graph
Input: Filepath of snapshot
Output: List of Communities at that time
"""


def runStaticLouvain(filepath):
    adjacency_matrix = np.matrix(haggleAdjacencyMatrix(filepath))
    return runLouvain(adjacency_matrix)


"""
Runs Louvain on an adjacency matrix
Input: Adj Matrix
Output: List of Communities
"""


def runLouvain(adjMatrix):
    G = nx.from_numpy_array(adjMatrix)
    partition = nx.community.louvain_communities(G)
    return partition

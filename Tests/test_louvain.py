import unittest
import time

import numpy as np

from Algorithms.louvain import runStaticLouvain, runLouvain
from Common.adjacencyMatrix import haggleAdjacencyMatrix, getAdjMatrix, updateAdjacencyMatrix, calculateNumberOfEdges
from Common.start_helper import getAgents, createAgentsAndCommunities


class MyTestCase(unittest.TestCase):

    # Static Louvain Haggle
    def test_louvain_haggle(self):
        filePath = '../Datasets/haggle/haggle.txt'
        start = time.time()
        c = runStaticLouvain(filePath)
        dur = time.time() - start
        print(f"speed:{dur}")
        print(f"length:{len(c)}")
        sumOfMember = 0
        for i in range(len(c)):
            sumOfMember += len(c[i])
        print(f"avg mem / comm = {sumOfMember/len(c)}")
        print(f"Edges: {calculateNumberOfEdges()}")

    # Incremental Louvain Haggle
    def test_incremental_louvain_haggle(self):
        start = time.time()
        for i in range(0, 5):
            filePath = f"../Datasets/haggle/haggle_dynamic_{i}.txt"
            if i == 0:
                adjMatrix = np.matrix(haggleAdjacencyMatrix(filePath))
                numNodes = len(adjMatrix)
                createAgentsAndCommunities(numNodes)
            else:
                updateAdjacencyMatrix(filePath, getAgents())
                adjMatrix = getAdjMatrix()
            print(f"Edges: {calculateNumberOfEdges()}")
            c = runLouvain(adjMatrix)
            print(f"length:{len(c)}")
            sumOfMember = 0
            for j in range(len(c)):
                sumOfMember += len(c[j])
            print(f"avg mem / comm = {sumOfMember / len(c)}")
        dur = time.time() - start
        print(f"speed:{dur}")

    # Louvain DNC
    def test_louvain_dnc(self):
        filePath = '../Datasets/dnc-temporalGraph/dnc-temporalGraph.txt'
        start = time.time()
        c = runStaticLouvain(filePath)
        dur = time.time() - start
        print(f"speed:{dur}")
        print(f"length:{len(c)}")
        sumOfMember = 0
        for i in range(len(c)):
            sumOfMember += len(c[i])
        print(f"avg mem / comm = {sumOfMember / len(c)}")

    # Dynamic Louvain DNC
    def test_incremental_louvain_dnc(self):
        start = time.time()
        for i in range(0, 3):
            filePath = f"../Datasets/dnc-temporalGraph/dnc-temporalGraph_dynamic_{i}.txt"
            if i == 0:
                adjMatrix = np.matrix(haggleAdjacencyMatrix(filePath))
                numNodes = len(adjMatrix)
                createAgentsAndCommunities(numNodes)
            else:
                updateAdjacencyMatrix(filePath, getAgents())
                adjMatrix = getAdjMatrix()
            print(f"Edges: {calculateNumberOfEdges()}")
            c = runLouvain(adjMatrix)
            print(f"length:{len(c)}")
            sumOfMember = 0
            for j in range(len(c)):
                sumOfMember += len(c[j])
            print(f"avg mem / comm = {sumOfMember / len(c)}")
        dur = time.time() - start
        print(f"speed:{dur}")

    # Louvain DNC
    def test_louvain_sociopattern(self):
        filePath = '../Datasets/sociopattern/sociopatterns-infections.txt'
        start = time.time()
        c = runStaticLouvain(filePath)
        dur = time.time() - start
        print(f"speed:{dur}")
        print(f"length:{len(c)}")
        sumOfMember = 0
        for i in range(len(c)):
            sumOfMember += len(c[i])
        print(f"avg mem / comm = {sumOfMember / len(c)}")

    # Dynamic Louvain DNC
    def test_incremental_louvain_sociopattern(self):
        start = time.time()
        for i in range(0, 3):
            filePath = f"../Datasets/sociopattern/sociopatterns-infections_dynamic_{i}.txt"
            if i == 0:
                adjMatrix = np.matrix(haggleAdjacencyMatrix(filePath))
                numNodes = len(adjMatrix)
                createAgentsAndCommunities(numNodes)
            else:
                updateAdjacencyMatrix(filePath, getAgents())
                adjMatrix = getAdjMatrix()
            print(f"Edges: {calculateNumberOfEdges()}")
            c = runLouvain(adjMatrix)
            print(f"length:{len(c)}")
            sumOfMember = 0
            for j in range(len(c)):
                sumOfMember += len(c[j])
            print(f"avg mem / comm = {sumOfMember / len(c)}")
        dur = time.time() - start
        print(f"speed:{dur}")


if __name__ == '__main__':
    unittest.main()

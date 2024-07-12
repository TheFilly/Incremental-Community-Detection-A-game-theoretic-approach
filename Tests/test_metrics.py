import unittest
import time

from Algorithms.algorithm import setUpAndRunCD, runCDWithFileInput
from Common.metrics import *
from Common.adjacencyMatrix import haggleAdjacencyMatrix
from Common.utility import allAgentsUtility

#filePath = '../Datasets/dnc-temporalGraph/dnc-temporalGraph.txt'
#simListPath = "../Similarity/dncGraphSimilarityList.txt"

#filePath = '../Datasets/sociopattern/sociopatterns-infections.txt'
#simListPath = "../Similarity/sociopattern.txt"

filePath ='../Datasets/haggle/haggle.txt'
simListPath = "../Similarity/haggleSimilarityList.txt"

class MyTestCase(unittest.TestCase):

    def test_mainMetrics(self):

        adjMatrix = haggleAdjacencyMatrix(filePath)
        communities = runCDWithFileInput(adjMatrix, 0, simListPath)

        start = time.time()
        print("Calling Average")
        print(calculateAverageMemberPerCommunity(communities))
        dur = time.time() - start
        print(f"Speed {dur}")

        start = time.time()
        print("Calling DFT")
        print(calculateDFT(communities, 1))
        dur = time.time() - start
        print(f"Speed {dur}")

        start = time.time()
        print("Calling Modularity")
        print(calculateModularity())
        dur = time.time() - start
        print(f"Speed {dur}")

        start = time.time()
        print("Calling Utility")
        print(allAgentsUtility(getAgents(), adjMatrix, calculateNumberOfEdges()))
        dur = time.time() - start
        print(f"Speed {dur}")


    def test_calculateAllMetrics(self):
        print("Testing All Metrics")

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 100)

        length = len(communities)

        avg = sum(list(map(lambda x: len(x.member) / length, communities)))
        print(f"Number of communities: {length}")
        print(f"Average number of members per community: {avg}")
        print("Calling Average")
        print(calculateAverageMemberPerCommunity(communities))
        print("Calling StandardDeviation")
        print(calculateStandardDeviation(communities))
        print("Calling Autocorrelation")
        print(calculateAutoCorrelation(communities, communities))
        print("Calling DFT")
        print(calculateDFT(communities, 1))
        print("Calling Modularity")
        print(calculateModularity())

    def test_calculateAverageMemberPerCommunity(self):
        print("Testing Average")

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 100)

        length = len(communities)

        avg = sum(list(map(lambda x: len(x.member) / length, communities)))
        print(f"Number of communities: {length}")
        print(f"Average number of members per community: {avg}")
        print("Calling Average")
        print(calculateAverageMemberPerCommunity(communities))

    def test_calculateAverageCommunityPerAgent(self):
        print("calculateAverageCommunityPerAgent")

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 100)

        length = len(communities)

        avg = sum(list(map(lambda x: len(x.member) / length, communities)))
        print(f"Number of communities: {length}")
        print(f"Average number of members per community: {avg}")
        print("Calling calculateAverageCommunityPerAgent")
        print(calculateAverageCommunityPerAgent(getAgents()))

    def test_calculateStandardDeviation(self):
        print("Testing Autocorrelation")

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 100)

        length = len(communities)

        avg = sum(list(map(lambda x: len(x.member) / length, communities)))
        print(f"Number of communities: {length}")
        print(f"Average number of members per community: {avg}")

        print("Calling StandardDeviation")
        print(calculateStandardDeviation(communities))

    def test_calculateAutocorrelation(self):
        print("Testing Autocorrelation")

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 100)

        length = len(communities)

        avg = sum(list(map(lambda x: len(x.member) / length, communities)))
        print(f"Number of communities: {length}")
        print(f"Average number of members per community: {avg}")

        print("Calling Autocorrelation")
        print(calculateAutoCorrelation(communities, communities))

    def test_calculateDFT(self):
        print("Testing DFT")

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 100)

        length = len(communities)

        avg = sum(list(map(lambda x: len(x.member) / length, communities)))
        print(f"Number of communities: {length}")
        print(f"Average number of members per community: {avg}")

        print("Calling DFT")
        print(calculateDFT(communities, 1))

    def test_calculateModularity(self):
        print("Testing Modularity")

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 100)

        length = len(communities)

        avg = sum(list(map(lambda x: len(x.member) / length, communities)))
        print(f"Number of communities: {length}")
        print(f"Average number of members per community: {avg}")
        print("Calling Modularity")
        print(calculateModularity())


if __name__ == '__main__':
    unittest.main()

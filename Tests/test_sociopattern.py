import unittest
import time

from Common.start_helper import agents
from Common.metrics import *
from Common.adjacencyMatrix import haggleAdjacencyMatrix, updateAdjacencyMatrix, getAdjMatrix
from Algorithms.algorithm import setUpAndRunCD, runCDWithFileInput, incrementalCDWithFileInput
from Common.similarityList import getSimilarityList
from Common.utility import allAgentsUtility
from Common.writeAndReadSimilarityToFile import writeMatrixToText, readMatrixFromText

filePath = '../Datasets/sociopattern/sociopatterns-infections.txt'

simListPath = "../Similarity/sociopattern.txt"


class MyTestCase(unittest.TestCase):

    # Static
    def test_socio_DGT(self):
        start = time.time()

        adjMatrix = haggleAdjacencyMatrix(filePath)
        print("Adjacency Matrix created")
        print(adjMatrix)

        communities = setUpAndRunCD(adjMatrix, 1000)

        dur = time.time() - start

        avg = 0
        for c in communities:
            avg = avg + len(c.member)

        print(f"speed:{dur}")
        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {avg / len(communities)}")
        print(f"Acg community per membr = {calculateAverageCommunityPerAgent(agents)}")
        print(f"Standard Devi = {calculateStandardDeviation(communities)}")
        print(f"Modularity =  {calculateModularity()}")
        print(f"Overlapping Modularity = {overlappingModularity(communities)}")
        print(f"Sum of Utilities = {allAgentsUtility(agents, adjMatrix, calculateNumberOfEdges())}")

    # Incremental
    def test_incrementalFile(self):
        crit = 100
        for i in range(0, 3):
            start = time.time()
            print(f"Iteration {i}")
            if i == 0:
                adjMatrix = haggleAdjacencyMatrix(filePath)
                print("Adjacency Matrix created")
                communities = runCDWithFileInput(adjMatrix, 1000, simListPath)
            else:
                updatedAgents = updateAdjacencyMatrix(
                    f'../Datasets/sociopattern/sociopatterns-infections_dynamic_{i}.txt', agents)
                adjMatrix = getAdjMatrix()
                communities = incrementalCDWithFileInput(adjMatrix, crit, simListPath)
            dur = time.time() - start

            avg = 0
            for c in communities:
                avg = avg + len(c.member)

            print(f"speed:{dur}")
            print(f"Iteration {i}")
            print(f"Number of communities: {len(communities)}")
            print(f"Average number of members per community: {avg / len(communities)}")
            print(f"Acg community per membr = {calculateAverageCommunityPerAgent(agents)}")
            print(f"Standard Devi = {calculateStandardDeviation(communities)}")
            print(f"Modularity =  {calculateModularity()}")
            print(f"Overlapping Modularity = {overlappingModularity(communities)}")
            print(f"Sum of Utilities = {allAgentsUtility(agents, adjMatrix, calculateNumberOfEdges())}")

    def test_writeAndReadMatrix(self):
        print("Testing read and write to Text function")
        adjacency_matrix = haggleAdjacencyMatrix(filePath)
        print("Adjacency Matrix created")
        communities = setUpAndRunCD(adjacency_matrix, 1000)

        simList = getSimilarityList()
        print("Writing to text file")
        writeMatrixToText(simList, simListPath)
        print("Reading from file")
        simList2 = readMatrixFromText(simListPath)

        self.assertEqual(simList, simList2)

    def test_readMatrix(self):
        print("Testing read and write to Text function")
        adjacency_matrix = haggleAdjacencyMatrix(filePath)
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 1000)

        simList = getSimilarityList()
        print("Reading from file")
        simList2 = readMatrixFromText(simListPath)
        flag = True
        for i in range(len(simList)):
            for j in range(len(simList)):
                if simList[i][j] != simList2[i][j]:
                    flag = False

        self.assertEqual(flag, True)

    def test_runCDFromFile(self):

        adjacency_matrix = haggleAdjacencyMatrix(filePath)
        communities = runCDWithFileInput(adjacency_matrix, 1000, simListPath)

        avg = 0
        for c in communities:
            avg = avg + len(c.member)

        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {avg / len(communities)}")


if __name__ == '__main__':
    unittest.main()

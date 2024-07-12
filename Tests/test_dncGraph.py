import unittest
import time

from Common.start_helper import agents
from Common.metrics import *
from Common.adjacencyMatrix import haggleAdjacencyMatrix, updateAdjacencyMatrix, getAdjMatrix, \
    createAdjacencyMatrix
from Algorithms.algorithm import setUpAndRunCD, applyIncrementalCD, runCDWithFileInput, incrementalCDWithFileInput
from Common.similarityList import getSimilarityList
from Common.utility import allAgentsUtility
from Common.writeAndReadSimilarityToFile import writeMatrixToText, readMatrixFromText

filePath = '../Datasets/dnc-temporalGraph/dnc-temporalGraph.txt'

simListPath = "../Similarity/dncGraphSimilarityList.txt"

class MyTestCase(unittest.TestCase):

    # Static
    def test_runCDFromFile(self):

        start = time.time()
        adjMatrix = haggleAdjacencyMatrix(filePath)
        communities = runCDWithFileInput(adjMatrix, 1000, simListPath)
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
                updatedAgents = updateAdjacencyMatrix(f'../Datasets/dnc-temporalGraph/dnc-temporalGraph_dynamic_{i}.txt', agents)
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

    def test_dnctempGraph_DGT(self):
        adjacency_matrix = haggleAdjacencyMatrix(filePath)

        print("Adjacency Matrix created")
        print(adjacency_matrix)
        communities = setUpAndRunCD(adjacency_matrix, 1000)

        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {len(adjacency_matrix) / len(communities)}")

    def test_dncGraph_dynamic_1000(self):
        length = 2029

        adjMatrix = createAdjacencyMatrix(filePath, length)

        crit = 100
        print(f"Running CD with Criterion: NoAction = {crit}")

        print("Adjacency Matrix created")
        print(adjMatrix)

        communities = setUpAndRunCD(adjMatrix, crit)
        print("Iteration 0")
        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {len(adjMatrix) / len(communities)}")

        print("Iteration 1")
        updatedAgents = updateAdjacencyMatrix('../Datasets/dnc-temporalGraph/dnc-temporalGraph_dynamic_1.txt', agents)
        adjMatrix = getAdjMatrix()
        communities = applyIncrementalCD(adjMatrix, updatedAgents, communities, crit)
        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {len(adjMatrix) / len(communities)}")

    def test_writeAndReadMatrix(self):
        print("Testing read and write to Text function")
        adjacency_matrix = haggleAdjacencyMatrix(filePath)
        print("Adjacency Matrix created")
        communities = setUpAndRunCD(adjacency_matrix, 1000)

        simList = getSimilarityList()
        print("Writing to text file")
        writeMatrixToText(simList, )
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


if __name__ == '__main__':
    unittest.main()

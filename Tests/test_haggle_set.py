import unittest
import time

from Common.metrics import *
from Common.start_helper import agents
from Common.adjacencyMatrix import haggleAdjacencyMatrix, updateAdjacencyMatrix, getAdjMatrix
from Algorithms.algorithm import setUpAndRunCD, applyIncrementalCD, runCDWithFileInput
from Common.similarityList import getSimilarityList
from Common.utility import allAgentsUtility
from Common.writeAndReadSimilarityToFile import writeMatrixToText, readMatrixFromText


class TestHaggleDatasets(unittest.TestCase):

    #Static
    def test_haggle_static(self):
        start = time.time()
        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')

        print("Adjacency Matrix created")
        print(adjacency_matrix)

        communities = setUpAndRunCD(adjacency_matrix, 0)

        avg = 0
        for c in communities:
            avg = avg + len(c.member)
        dur = time.time() - start

        print(f"speed:{dur}")
        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {avg / len(communities)}")
        print(f"Acg community per membr = {calculateAverageCommunityPerAgent(agents)}")
        print(f"Standard Devi = {calculateStandardDeviation(communities)}")
        print(f"Modularity =  {calculateModularity()}")
        print(f"Overlapping Modularity = {overlappingModularity(communities)}")
        print(f"Sum of Utilities = {allAgentsUtility(agents, adjacency_matrix, calculateNumberOfEdges())}")

    # Incremental
    def test_haggle_dynamic(self):

        for i in range(0, 5):
            start = time.time()
            print(f"Iteration {i}")
            if i == 0:
                adjMatrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle_dynamic_0.txt')
                print("Adjacency Matrix created")
                communities = setUpAndRunCD(adjMatrix, i)
            else:
                updatedAgents = updateAdjacencyMatrix(f'../Datasets/haggle/haggle_dynamic_{i}.txt', agents)
                adjMatrix = getAdjMatrix()
                communities = applyIncrementalCD(adjMatrix, updatedAgents, communities, i)
            dur = time.time() - start
            avg = 0
            for c in communities:
                avg = avg + len(c.member)
            print(f"Iteration {i}")
            print(f"speed:{dur}")
            print(f"Number of communities: {len(communities)}")
            print(f"Average number of members per community: {avg / len(communities)}")
            print(f"Acg community per membr = {calculateAverageCommunityPerAgent(agents)}")
            print(f"Standard Devi = {calculateStandardDeviation(communities)}")
            print(f"Modularity =  {calculateModularity()}")
            print(f"Overlapping Modularity = {overlappingModularity(communities)}")
            print(f"Sum of Utilities = {allAgentsUtility(agents, adjMatrix, calculateNumberOfEdges())}")

    def test_writeAndReadMatrix(self):
        print("Testing read and write to Text function")

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")

        communities = setUpAndRunCD(adjacency_matrix, 1000)

        simList = getSimilarityList()
        print("Writing to text file")
        writeMatrixToText(simList, "../Similarity/haggleSimilarityList.txt")
        print("Reading from file")
        simList2 = readMatrixFromText("../Similarity/haggleSimilarityList.txt")

        flag = True
        for i in range(len(simList)):
            for j in range(len(simList)):
                if simList[i][j] != simList2[i][j]:
                    flag = False
        self.assertEqual(flag, True)

    def test_runCDFromFile(self):

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')

        communities = runCDWithFileInput(adjacency_matrix, 1000, "../Similarity/haggleSimilarityList.txt")
        avg = 0
        for c in communities:
            avg = avg + len(c.member)

        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {avg / len(communities)}")


if __name__ == '__main__':
    unittest.main()

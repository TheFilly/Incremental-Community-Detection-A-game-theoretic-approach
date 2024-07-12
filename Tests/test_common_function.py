import unittest

import numpy as np

from Common.similarityList import calculateSimilarities
from Common.utility import calculateUtility
from Common.adjacencyMatrix import haggleAdjacencyMatrix, calculateNumberOfEdges, calculateCommonNeighbours
from Common.agent import Agent
from Common.community import Community


class MyTestCase(unittest.TestCase):

    def test_calculate_similarities_small(self):

        adj_matrix = np.array([[0, 0, 1, 0],
                               [0, 0, 0, 1],
                               [1, 0, 0, 1],
                               [0, 1, 1, 0]])

        agent1 = Agent(0)
        agent2 = Agent(1)

        similarity = calculateSimilarities(agent1.id, agent2.id, adj_matrix)
        print(f"Similarity of Agent1 and 2 is {similarity}")
        self.assertIsInstance(similarity, (int, float))
        self.assertGreaterEqual(similarity, -1)
        self.assertLessEqual(similarity, 1)

    def test_calculate_similarities_haggle(self):

        adj_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')

        # No Neighbor, No common edge
        # agent1 = Agent(12)
        # agent2 = Agent(120)
        # adj_matrix[12][31] = 0

        # Neighbor, No common edge
        # agent1 = Agent(12)
        # agent2 = Agent(120)
        # adj_matrix[12][31] = 0
        # adj_matrix[12][120] = 1

        # CommonNeighbors,CommonEdge
        agent1 = Agent(1)
        agent2 = Agent(2)

        # CommonNeighbors,No Edge
        # agent1 = Agent(1)
        # agent2 = Agent(2)
        # adj_matrix[1][2] = 0

        similarity = calculateSimilarities(agent1.id, agent2.id, adj_matrix)

        print(f"Similarity of Agent1 and 2 is {similarity}")

        print(f"Common Neighbors: {calculateCommonNeighbours(agent1.id, agent2.id, adj_matrix)}")

        print(f"Connection Type: {adj_matrix[agent1.id][agent2.id]}")

        print(f"Num_edges: {calculateNumberOfEdges(adj_matrix)}")

        print(f"Agent {agent1.id} neighbor: {adj_matrix[agent1.id]}")

        print(f"Agent {agent2.id} neighbor: {adj_matrix[agent2.id]}")

        self.assertIsInstance(similarity, (int, float))
        self.assertGreaterEqual(similarity, -1)
        self.assertLessEqual(similarity, 1)

    def test_calculate_similarities_dnc(self):

        adj_matrix = haggleAdjacencyMatrix('../Datasets/dnc-temporalGraph/dnc-temporalGraph.txt')

        # No Neighbor, No common edge
        # agent1 = Agent(12)
        # agent2 = Agent(120)
        # adj_matrix[12][31] = 0

        # Neighbor, No common edge
        # agent1 = Agent(12)
        # agent2 = Agent(120)
        # adj_matrix[12][31] = 0
        # adj_matrix[12][120] = 1

        # CommonNeighbors,CommonEdge
        agent1 = Agent(0)
        agent2 = Agent(1)

        # CommonNeighbors,No Edge
        # agent1 = Agent(1)
        # agent2 = Agent(2)
        # adj_matrix[1][2] = 0

        similarity = calculateSimilarities(agent1.id, agent2.id, adj_matrix)

        print(f"Similarity of Agent1 and 2 is {similarity}")

        print(f"Common Neighbors: {calculateCommonNeighbours(agent1.id, agent2.id, adj_matrix)}")

        print(f"Connection Type: {adj_matrix[agent1.id][agent2.id]}")

        print(f"Num_edges: {calculateNumberOfEdges(adj_matrix)}")

        print(f"Num_Nodes: {len(adj_matrix)}")

        self.assertIsInstance(similarity, (int, float))
        self.assertGreaterEqual(similarity, -1)
        self.assertLessEqual(similarity, 1)

    def test_calculate_utility(self):

        adjMatrix = np.array([[0, 1, 1, 0],
                              [1, 0, 1, 1],
                              [1, 1, 0, 1],
                              [0, 1, 1, 0]])

        a0 = Agent(0)
        a1 = Agent(1)
        a2 = Agent(2)
        a3 = Agent(3)

        agents = [a0, a1, a2, a3]

        c0 = Community(0)
        c1 = Community(1)

        a0.join(c1)
        a1.join(c0)
        a2.join(c0)
        a3.join(c1)

        m = calculateNumberOfEdges(adjMatrix)

        similarityList = np.zeros((len(agents), len(agents)), dtype=float)

        for i in range(len(agents)):
            for j in range(i + 1, len(agents)):
                x = calculateSimilarities(agents[i], agents[j], adjMatrix)
                similarityList[i, j] = x
                similarityList[j, i] = x

        utility = calculateUtility(a0, similarityList, m)

        print(f"Utility of Agent0 is {utility}")

        self.assertIsInstance(utility, float)

    def test_common_Neighbors(self):

        adj_matrix = np.array([[0, 1, 1, 0],
                               [1, 0, 1, 1],
                               [1, 1, 0, 1],
                               [0, 1, 1, 0]])

        agent1 = Agent(1)
        agent2 = Agent(2)

        comm = calculateCommonNeighbours(agent1.id, agent2.id, adj_matrix)
        print(f"CommonNeighbors of Agent1 and 2 is {comm}")


if __name__ == '__main__':
    unittest.main()

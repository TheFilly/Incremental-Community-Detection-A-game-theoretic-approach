import unittest

from Common.adjacencyMatrix import haggleAdjacencyMatrix
from Algorithms.ray_functions import runRayCD


class MyTestCase(unittest.TestCase):

    def test_ray_haggle_DGT(self):

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/haggle/haggle.txt')
        print("Adjacency Matrix created")
        print(adjacency_matrix)

        communities = runRayCD(adjacency_matrix, 1000)

        avg = 0
        for c in communities:
            avg = avg + len(c.member)

        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {avg / len(communities)}")

    def test_ray_dnctempGraph_DGT(self):

        adjacency_matrix = haggleAdjacencyMatrix('../Datasets/dnc-temporalGraph/dnc-temporalGraph.txt')
        print("Adjacency Matrix created")
        print(adjacency_matrix)

        communities = runRayCD(adjacency_matrix, 1000)

        avg = 0
        for c in communities:
            avg = avg + len(c.member)

        print(f"Number of communities: {len(communities)}")
        print(f"Average number of members per community: {avg / len(communities)}")


if __name__ == '__main__':
    unittest.main()

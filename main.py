import networkx as nx

from Algorithms.algorithm import setUpAndRunCD
from Common.adjacencyMatrix import haggleAdjacencyMatrix
from Common.metrics import calculateAverageMemberPerCommunity

"""
Test run of community detection with the dnc-temporal-Graph dataset.
"""


def main():
    # Create a numpy adjacency matrix
    adjacency_matrix = haggleAdjacencyMatrix('Datasets/dnc-temporalGraph/dnc-temporalGraph.txt')
    print("Adjacency Matrix created")

    # Call the runDGTCD function
    communities = setUpAndRunCD(adjacency_matrix, 1000)

    print(f"Number of communities: {len(communities)}")
    print(f"Average number of members per community: {calculateAverageMemberPerCommunity(communities)}")


if __name__ == "__main__":
    main()

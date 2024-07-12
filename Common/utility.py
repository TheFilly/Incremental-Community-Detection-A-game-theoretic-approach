from Common.agent import Agent
from Common.similarityList import getSimilarity

"""
Calculates the Utility of an Agent
Input: Agent (Node), the List of adjacencyMatrix and number of edges m
Output: Utility of that Agent (double)

All of the following equations are from paper ACM Alvari 2014
"""


def calculateUtility(node: Agent, adjMatrix, m):
    x = calculateGain(node, m, adjMatrix) - calculateLoss(len(node.communities), m)
    return x


"""
Calculates the Gain of an Agent for joining or leaving a community
Input: Agent (Node), the number of Edges in the Graph and List of SimilarityValues
Output: Gain of that Agent (double)

All of the following equations are from paper ACM Alvari 2014
"""


def calculateGain(node: Agent, m, adjMatrix):
    sumOfSim = 0.0
    for c in node.communities:
        for n in c.member:
            if n.id != node.id:
                sumOfSim += getSimilarity(n.id, node.id)
    return sumOfSim / m


"""
Calculates the Loss (overhead costs) of an Agent
Input: Number of labels of agent (communities the agent belongs to) and the number of Edges in the Graph
Output: Loss of that Agent (double)

All of the following equations are from paper ACM Alvari 2014
"""


def calculateLoss(labels, m):
    if labels == 1:
        labels = 0.0
    return (1.0 / m) * (float(labels) - 1.0)


"""
Calculates the sum of all agents utilities
Input:List of agents, adjMatrix and number of all edges
Output: Sum of Utility
"""


def allAgentsUtility(agents, adjMatrix, m):
    sumUtility = 0
    for agent in agents:
        sumUtility += calculateUtility(agent, adjMatrix, m)
    return sumUtility

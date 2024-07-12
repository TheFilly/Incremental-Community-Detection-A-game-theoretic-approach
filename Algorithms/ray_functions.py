import ray
import time

"""
This file includes all algorithm related functions that are called with ray

Most functions are outdated since ray showed issue early on
"""

from Common.utility import *
from Common.adjacencyMatrix import *
from Common.agent import *
from Common.community import *
from Common.similarityList import calculateSimilarities


"""
Run community detection with ray
Input: Adjacency Matrix and convergence criterium
Output: List of Communities
"""


def runRayCD(adjMatrix, criterium):

    ray.init()

    numNodes = len(adjMatrix)
    m = float(calculateNumberOfEdges(adjMatrix))

    agents = []
    communities = []
    for i in range(numNodes):
        agents.append(Agent(i))
        communities.append(Community(i))
        agents[i].join(communities[i])
    print("Agents and Communities created")

    start = time.time()
    similarityList = np.zeros((numNodes, numNodes), dtype=float)
    x = 0
    while x < numNodes:
        y = x
        x = x + 50
        if x > numNodes:
            x = numNodes
        futures = [calculateSimilarityList.remote(numNodes, ray.put(adjMatrix), agents, i) for i in range(y, x)]
        t = ray.get(futures)
        for j in range(len(t)):
            similarityList[y + j, :] = t[j]

    dur = time.time() - start
    print(f"Similarity List created in: {dur} seconds")

    i = 0
    while i < criterium:
        futures = [par_bestAction.remote(agents[i], communities, similarityList, m) for i in range(len(agents))]
        [ready], futures = ray.wait(futures)
        for t in ready:
            if t is None:
                i = i + 1
    return communities


"""
Calculates the Similarity List for all agents
Input: The number of nodes, the adjacency matrix, number of agents and one row index
Output: The filled similarity list
"""


@ray.remote
def calculateSimilarityList(numNodes: int, adjMatrix, agents, i):

    similarityList = np.zeros((1, numNodes), dtype=float)

    for j in range(0, numNodes):
        x = calculateSimilarities(agents[i], agents[j], adjMatrix)
        similarityList[0, j] = x

    return similarityList


"""
Calculates Similarities between two agents
Input: Two Nodes and a Numpy Adjacency Matrix
Output: Neighborhood Similarity (double)
"""


@ray.remote
def parallelCalculateSimilarities(n1: Agent, n2: Agent, adjMatrix):
    # w = number of common neighbours
    w = float(calculateCommonNeighbours(n1.id, n2.id, adjMatrix))

    # d = degree of node (edges that connect to node)
    d1 = float(calculateNodeDegree(n1.id, adjMatrix))
    d2 = float(calculateNodeDegree(n2.id, adjMatrix))

    # m = numbers of edges at t
    m = float(calculateNumberOfEdges(adjMatrix))

    # n = number of nodes/vertices
    n = float(len(adjMatrix))

    # a = 1 if a1 and a2 adjacent, 0 if not
    a = adjMatrix[n1.id][n2.id]

    if n2.id == n - 1:
        print(f"{n1.id} / {n}")

    if a == 1:  # If nodes are neighbors
        if w >= 1.0:
            return w * (1.0 - (d1 * d2 / (2.0 * m)))
        else:
            return d1 * d2 / (4.0 * m)
    else:  # If nodes are not neighbors
        if w >= 1.0:
            return w / n
        else:
            return -d1 * d2 / (4.0 * m)


"""
Determines the best Action for given Agent
Input: Agent, list of all communities, the similarity-value-list and the number of edges
Output: Best Action
"""


@ray.remote
def par_bestAction(agent, communities, similarityList, m):
    current_utility = calculateUtility(agent, similarityList, m)
    best_utility = current_utility
    best_action = None

    for community in communities:
        if community in agent.communities:
            agent.leave(community)
            new_utility = calculateUtility(agent, similarityList, m)
            if new_utility > best_utility:
                best_utility = new_utility
                best_action = ("leave", community)
            agent.join(community)

        else:
            agent.join(community)
            new_utility = calculateUtility(agent, similarityList, m)
            if new_utility > best_utility:
                best_utility = new_utility
                best_action = ("join", community)
            agent.leave(community)

            for current_community in agent.communities:
                agent.switch(community, current_community)
                new_utility = calculateUtility(agent, similarityList, m)
                if new_utility > best_utility:
                    best_utility = new_utility
                    best_action = ("switch", community, current_community)
                agent.switch(current_community, community)

    t = 0
    if best_action:
        if best_action[0] == "join":
            agent.join(best_action[1])
        elif best_action[0] == "leave":
            t = agent.leave(best_action[1])
            if t == -1:
                communities.remove(best_action[1])
        elif best_action[0] == "switch":
            t = agent.switch(best_action[1], best_action[2])
            if t == -1:
                communities.remove(best_action[2])

    return best_action

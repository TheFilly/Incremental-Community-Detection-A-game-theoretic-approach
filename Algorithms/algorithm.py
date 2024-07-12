from Common.bestAction import bestAction
from Common.convergence import checkConvergence
from Common.metrics import *
from Common.similarityList import createSimilarityList, updateSimilarityList, setSimilarityList
from Common.start_helper import createAgentsAndCommunities, agents, communities
from Common.adjacencyMatrix import *
from Common.agent import chooseAgent
from Common.writeAndReadSimilarityToFile import readMatrixFromText

"""
Run static Community Detection based on an Adjacency Matrix
Input: Adjacency Matrix
Output: List of Communities at that time
"""


def setUpAndRunCD(adjacencyMatrix, criterium):
    numNodes = len(adjacencyMatrix)
    m = float(calculateNumberOfEdges())

    createAgentsAndCommunities(numNodes)
    print("Agents and Communities created")

    createSimilarityList(agents, numNodes, adjacencyMatrix)

    return runOptimization(criterium, adjacencyMatrix, m)


"""
Run incremental Community Detection based on an Adjacency Matrix
Input: Adjacency Matrix and list of agents
Output: List of Communities at that time
"""


def applyIncrementalCD(adjacencyMatrix, updatedAgents, communities, criterium):
    m = float(calculateNumberOfEdges())

    numNodes = len(adjacencyMatrix)

    for agent in updatedAgents:
        updateSimilarityList(agent, agents, numNodes)
    print("Updating Similarity List Done")

    return runOptimization(criterium, adjacencyMatrix, m, a=updatedAgents)


"""
Run static Community Detection based on an Adjacency Matrix with file input for a similarity list
Input: Adjacency Matrix and file path to a similarity list
Output: List of Communities at that time
"""


def runCDWithFileInput(adjacencyMatrix, criterium, filePath):
    numNodes = len(adjacencyMatrix)
    m = float(calculateNumberOfEdges())

    createAgentsAndCommunities(numNodes)
    print("Agents and Communities created")

    simList = readMatrixFromText(filePath)
    setSimilarityList(simList)
    c = runOptimization(criterium, adjacencyMatrix, m)
    return c


"""
Run incremental Community Detection based on an Adjacency Matrix with file input for a similarity list
Input: Adjacency Matrix and file path to a similarity list
Output: List of Communities at that time
"""


def incrementalCDWithFileInput(adjacencyMatrix, criterium, filePath):
    m = float(calculateNumberOfEdges())
    c = runOptimization(criterium, adjacencyMatrix, m)
    return c


"""
Run the algorithmic part of the Community detection, which is called by the above functions
Input: Adjacency Matrix, number of edges and list of agents
Output: List of Communities at that time
"""


def runOptimization(criterium, adjacencyMatrix, m, a=agents):
    # change here
    tolerance = 0.1
    minIter = 25
    threshold = 1

    metric = calculateAverageMemberPerCommunity(communities)
    pV = []
    while not checkConvergence(metric, pV, threshold, tolerance, minIter):
        randomAgent = chooseAgent(a)

        t = bestAction(randomAgent, communities, adjacencyMatrix, m)
        metric = calculateAverageMemberPerCommunity(communities)
        print(metric)

    return communities

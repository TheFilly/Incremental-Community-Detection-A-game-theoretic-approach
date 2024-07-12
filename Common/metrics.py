import cmath
import math

from Common.adjacencyMatrix import calculateNumberOfEdges, calculateNodeDegree, getAdjMatrix
from Common.agent import checkSameCommunity
from Common.start_helper import getAgents

"""
Calculates the average number of members per community
Input: List of communities
Output: average number of members per community
"""


def calculateAverageMemberPerCommunity(c):
    w = len(c)
    avg = sum(list(map(lambda s: len(s.member) / w, c)))
    return avg


"""
Calculates the average number of communities per agent
Input: List of communities
Output: average number of members per community
"""


def calculateAverageCommunityPerAgent(agents):
    w = len(agents)
    avg = sum(list(map(lambda a: len(a.communities) / w, agents)))
    return avg


"""
Calculates the standard deviation of a community structure
Input: A community structure
Output: The communities standard deviation
"""


def calculateStandardDeviation(c):
    w = len(c)
    avg = sum(list(map(lambda s: len(s.member) / w, c)))
    s_member = list(map(lambda s: len(s.member), c))
    deviation = math.sqrt(((1 / w) * sum(list(map(lambda s: math.pow(s - avg, 2), s_member)))))
    return deviation


"""
Calculates the autocorrelation of a stream with itself at an earlier time
Input: Two community structures
Output: The correlation value. If c1 and c2 are equal, the correlation should be 1
"""


def calculateAutoCorrelation(c1, c2):
    w = len(c1)

    s_avg = sum(list(map(lambda s: len(s.member) / w, c1)))
    r_avg = sum(list(map(lambda r: len(r.member) / w, c2)))

    s_member = list(map(lambda s: len(s.member), c1))

    r_member = list(map(lambda s: len(s.member), c2))

    f1 = sum(list(map(lambda s, r: (s * r) - (s_avg * r_avg), s_member, r_member)))

    f2 = math.sqrt(sum(list(map(lambda s: math.pow(s - s_avg, 2), s_member))))

    f3 = math.sqrt(sum(list(map(lambda r: math.pow(r - r_avg, 2), r_member))))

    corr = f1 / (f2 * f3)

    return corr


"""
Determines the Discrete Fourier Transformation
Input: The list of communities c and the timepoint f
Output: Discrete Fourier Transformation of that series
"""


def calculateDFT(c, F):
    w = len(c)
    e = math.e
    j = cmath.sqrt(-1)
    pi = math.pi
    c_member = list(map(lambda s: len(s.member), c))
    dft = (1 / math.sqrt(w)) * sum(
        list(map(lambda x, i: x * cmath.exp(-2 * pi * F * j * i / w), c_member, range(w - 1))))
    return dft


"""
Calculates the modularity of a community structure
Input: One community
Output: The Modularity (double)
"""


def calculateModularity():
    adjMatrix = getAdjMatrix()

    agents = getAgents()

    m = calculateNumberOfEdges() * 2
    Q = 0
    for i in range(len(adjMatrix)):
        for j in range(i+1, len(adjMatrix[i])):
            if i != j:  # to avoid self-loops
                Q += (1/m) * (adjMatrix[i][j] - (calculateNodeDegree(i) * calculateNodeDegree(j) / m)) * checkSameCommunity(agents[i], agents[j])

    return Q



"""
Calculates the overlapping modularity of a community structure
Input: One community
Output: The Modularity (double)
"""


def overlappingModularity(communities):

    m = calculateNumberOfEdges() * 2
    adjMatrix = getAdjMatrix()
    agents = getAgents()
    Q = 0

    for comm in communities:
        cmem = len(comm.member)
        for i in range(cmem):
            iID = comm.member[i].id
            degreeI = calculateNodeDegree(iID)
            oi = len(agents[iID].communities)
            for j in range(i+1, cmem):
                jID = comm.member[j].id
                oj = len(agents[jID].communities)
                Q += (1/(oi*oj))*(adjMatrix[iID][jID] - (degreeI * calculateNodeDegree(jID) / m))

    return Q / m

from Common.agent import Agent
from Common.community import Community

agents = []
communities = []

"""
Construct the list of agents based on a number input
"""


def createAgents(num):
    global agents

    agents = []
    for i in range(num):
        agents.append(Agent(i))


"""
Construct the list of communities based on a number input
"""


def createCommunities(num):
    global communities

    communities = []
    for i in range(num):
        communities.append(Community(i))
        # only for static CD or first run


"""
Construct the list of agents and communities based on a number input
"""


def createAgentsAndCommunities(num):
    global agents
    global communities

    for i in range(num):
        agents.append(Agent(i))
        communities.append(Community(i))
        # only for static CD or first run
        agents[i].join(communities[i])


"""
Get list of agents
"""


def getAgents():
    return agents


"""
Get list of communities
"""


def getCommunities():
    return communities

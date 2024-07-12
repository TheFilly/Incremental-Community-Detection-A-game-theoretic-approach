from Common.adjacencyMatrix import get_neighbors
from Common.start_helper import getAgents
from Common.utility import calculateUtility

"""
Determines the best Action for given Agent
Input: Agent, list of all communities, the adjacency matrix and the number of edges
Output: Best Action
"""


def bestAction(agent, communities, adjacencyMatrix, m):
    current_utility = calculateUtility(agent, adjacencyMatrix, m)
    best_utility = current_utility
    best_action = None

    neighbors = get_neighbors(agent.id, getAgents())
    neighbor_communities = set()
    for neighbor in neighbors:
        for c in neighbor.communities:
            neighbor_communities.add(c)

    for community in [c for c in neighbor_communities if c not in agent.communities]:

        agent.join(community)
        new_utility = calculateUtility(agent, adjacencyMatrix, m)
        if new_utility > best_utility:
            best_utility = new_utility
            best_action = ("join", community)
        agent.leave(community)

        for current_community in agent.communities:
            agent.switch(community, current_community)
            new_utility = calculateUtility(agent, adjacencyMatrix, m)
            if new_utility > best_utility:
                best_utility = new_utility
                best_action = ("switch", community, current_community)
            agent.switch(current_community, community)

    for community in agent.communities:
        agent.leave(community)
        new_utility = calculateUtility(agent, adjacencyMatrix, m)
        if new_utility > best_utility:
            best_utility = new_utility
            best_action = ("leave", community)
        agent.join(community)

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


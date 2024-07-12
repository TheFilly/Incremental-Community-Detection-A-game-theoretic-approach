import random
from Common.community import Community

seen_counts = {}

"""
Class to manage agent objects ( nodes ). 
"""


class Agent:

    def __init__(self, id):
        self.id = id
        self.communities = []

    def join(self, c: Community):
        self.communities.append(c)
        c.join(self)

    def leave(self, c: Community):
        self.communities.remove(c)
        c.leave(self)
        if len(c.member) == 0:
            return -1
        return 0

    def switch(self, c_j: Community, c_l: Community):
        self.join(c_j)
        return self.leave(c_l)


"""
Choose an agent randomly with a bias towards less seen agents.
Input: List of agents to choose from, Bias towards less seen agents (default: 0.5).
Output: chosen agent
"""


def chooseAgent(agents, bias=0.5):
    global seen_counts

    for agent in agents:
        seen_counts[agent] = seen_counts.get(agent, 0)

    weights = [1 / (seen_counts.get(agent, 0) + 1) ** bias for agent in agents]
    total_weight = sum(weights)
    weights = [weight / total_weight for weight in weights]
    chosen_agent = random.choices(agents, weights=weights)[0]

    seen_counts[chosen_agent] += 1
    return chosen_agent


"""
Checks if 2 agents are in the same community
Input: agent objects
Output: 1 if yes, 0 if no
"""


def checkSameCommunity(n1, n2):
    common_communities = set(n1.communities) & set(n2.communities)
    if len(common_communities) > 0:
        return 1
    return 0

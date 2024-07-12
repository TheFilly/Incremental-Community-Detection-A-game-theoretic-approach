"""
Class to manage community objects
"""


class Community:

    def __init__(self, id):
        self.id = id
        self.member = []

    def join(self, node):
        self.member.append(node)

    def leave(self, node):
        self.member.remove(node)



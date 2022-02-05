class BaseNode(object):

    def __init__(self, base: chr):

        self.base: chr = base  # The base for this base node. This could be made into an enum if needed.

        self.count: int = 1  # If the base has been instantiated, then there is at least one such base present.

        self.child_base_nodes: {BaseNode} = {}  # Direct descendents of this base node.

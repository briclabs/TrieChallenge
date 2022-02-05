from base_node import BaseNode


class BaseSegmentTrie(object):

    # Instantiate this sample's trie.
    def __init__(self):
        self.base_root_node = BaseNode("")
        self.total_base_node_count: int = 0  # Stores the count of individual base nodes in this trie.

        self.base_root_node.count -= 1  # The base root node should not count toward any base counts.

    # Record this sample's bases into trie form.
    def record(self, segments: [str]):
        for segment in segments:
            this_base_node = self.base_root_node  # Common ancestor for all child base nodes.
            for base in segment:
                this_base = base.upper()  # Standardize bases in record input to uppercase to avoid case sensitivity.

                if this_base == this_base_node.base:
                    this_base_node.count += 1  # If this base node has the same base, increment its count up by 1.
                elif this_base in this_base_node.child_base_nodes:
                    this_base_node = this_base_node.child_base_nodes[this_base]  # Switch to child base node.
                    this_base_node.count += 1  # If the child base has the same base, increment its count up by 1.
                else:
                    # Build a new node in this segment's trie.
                    self.total_base_node_count += 1  # Increment the count of individual nodes in this trie.
                    # No need to increment the new base node's base count since it would naturally start with 1.
                    new_base_node = BaseNode(this_base)
                    this_base_node.child_base_nodes[this_base] = new_base_node
                    this_base_node = new_base_node

    def count_matching_bases(self, search_bases: str) -> int:
        total_count: int = 0
        de_duped_search_bases: str = ""  # Store a representation of the bases being searched without any dupes.
        for search_base in search_bases:
            if search_base not in de_duped_search_bases:
                de_duped_search_bases += search_base

        for search_base in de_duped_search_bases:
            # Loop through the individual bases being searched, gathering the total count for each search.
            total_count += self.__count_matching_base(self.base_root_node, search_base)
        return total_count

    def __count_matching_base(self, this_base_node: BaseNode, search_base: chr) -> int:
        total_count: int = 0  # Default, assuming this base node doesn't have a matching base, don't count it.

        if search_base.upper() == this_base_node.base.upper():
            total_count = this_base_node.count  # Include this node's base occurrence count before moving on.

        # Loop through all children recursively, summing up each according to the logic preceding this loop.
        for child_node in this_base_node.child_base_nodes:
            total_count += self.__count_matching_base(this_base_node.child_base_nodes[child_node], search_base)

        # Return the sum of base occurrences now that there are no more children to explore.
        return total_count

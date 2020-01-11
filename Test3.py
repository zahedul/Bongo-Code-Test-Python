class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    # Get Ancestors Value
    def get_ancestors_value(self, value_list):
        # print(self.value)
        # print(value_list)
        value_list.add(self.value)
        if self.parent is not None:
            value_list.add(self.parent.value)
            return self.parent.get_ancestors_value(value_list)
        return value_list

def lca(nodeA, nodeB):
    ancestorsA = nodeA.get_ancestors_value(set())
    ancestorsB = nodeB.get_ancestors_value(set())
    # print(ancestorsA)
    # print(ancestorsB)

    common_ancestors = ancestorsA.intersection(ancestorsB)
    
    return list(common_ancestors)[-1]



one = Node(1, None)
two = Node(2, one)
three = Node(3, one)
four = Node(4, two)
five = Node(5, two)
six = Node(6, three)
seven = Node(7, three)
eight = Node(8, four)
nine = Node(9, four)

print(lca(nine, seven))
print(lca(six, seven))
print(lca(three, seven))
print(lca(eight, nine))
print(lca(nine, five))
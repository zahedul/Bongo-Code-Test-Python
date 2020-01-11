class Node(object):
    def __init__(self, value, parent):
        self.value = value
        self.parent = parent

    # Get Ancestors Value
    def get_ancestors_value(self, value_list):
        value_list.add(self.value)
        if self.parent is not None:
            value_list.add(self.parent.value)
            return self.parent.get_ancestors_value(value_list)
        return value_list

def lca(nodeA, nodeB):
    ancestorsA = nodeA.get_ancestors_value(set())
    ancestorsB = nodeB.get_ancestors_value(set())

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

print(lca(nine, seven)) # 1
print(lca(six, seven)) # 3
print(lca(three, seven)) # 3
print(lca(eight, nine)) # 4
print(lca(nine, five)) # 2
class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, hfunction, parent=None):
        self.STATE = state
        self.HFUNCTION = hfunction
        self.PARENT_NODE = parent

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)  # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Heuristic function value: ' + str(self.HFUNCTION)


'''
Search the tree for the goal state and return path from initial state to goal state
'''


def TREE_SEARCH():
    #fringe = []
    current_node = Node(INITIAL_STATE[0],INITIAL_HEURISTIC_FUNCTION  )
    #fringe = INSERT(initial_node, fringe)
    #while fringe is not None:
    for x in range(0,21):
    #REMOVE_FIRST(fringe)
        for goal in GOAL_STATES:
            if current_node.STATE == goal:
                return current_node.path()
        children = EXPAND(current_node)
        if not children:
            print("Stuck in loop between " + current_node.STATE + " and " + current_node.PARENT_NODE.STATE)
            current_node = current_node.PARENT_NODE
        else:
            for child in children:
                if child.HFUNCTION < current_node.HFUNCTION:
                    current_node = child

    return current_node.path()


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''


def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(state=child[0],
                 hfunction = child[1],
                 parent=node)
                  # create node for each in state list # e.g. result = 'F' then 'G' from list ['F', 'G']
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''


def INSERT(node, queue):
    return INSERT_ALL([node], queue)


'''
Insert list of nodes into the fringe
'''


def INSERT_ALL(list, queue):
    # queue = list + queue #Depth first
    queue.extend(list) # Breadth first
    return queue


'''
Remove first element from fringe
'''


def REMOVE_FIRST(queue):
    return queue.pop(0)


'''
Successor function, mapping the nodes to its successors
'''


def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]
    #state_properties = STATE_SPACE[state]
    #return state_properties[1:]  # successor_fn( 'C' ) returns ['F', 'G']



INITIAL_STATE = 'A'
INITIAL_HEURISTIC_FUNCTION = 6
GOAL_STATES = ['K', 'L']
STATE_SPACE = {'A': [['B', 5], ['C', 5], ['D', 2]],
               'B': [['F', 5], ['E', 4]],
               'C': [['E', 4]],
               'D': [['H', 2], ['I', 2], ['J', 1]],
               'E': [['G', 4], ['H', 2]],
               'F': [['G', 4]],
               'G': [['K', 0]],
               'H': [['K', 0], ['L', 0]],
               'I': [['L', 0]],
               'J': []
                }

'''
Run tree search and display the nodes in the path to goal node
'''


def run():
    path = TREE_SEARCH()
    print('Solution path:')
    for node in path:
        node.display()


if __name__ == '__main__':
    run()

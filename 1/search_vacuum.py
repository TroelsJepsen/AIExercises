class Node:  # Node has only PARENT_NODE, STATE, DEPTH
    def __init__(self, state, parent=None, depth=0):
        self.STATE = state
        self.PARENT_NODE = parent
        self.DEPTH = depth

    def path(self):  # Create a list of nodes from the root to this node.
        current_node = self
        path = [self]
        while current_node.PARENT_NODE:  # while current node has parent
            current_node = current_node.PARENT_NODE  # make parent the current node
            path.append(current_node)   # add current node to path
        return path

    def display(self):
        print(self)

    def __repr__(self):
        return 'State: ' + str(self.STATE) + ' - Depth: ' + str(self.DEPTH)


'''
Search the tree for the goal state and return path from initial state to goal state
'''
def TREE_SEARCH():
    fringe = []
    initial_node = Node(INITIAL_STATE)
    fringe = INSERT(initial_node, fringe)
    while fringe is not None:
        node = REMOVE_FIRST(fringe)
        if node.STATE == GOAL_STATE:
            return node.path()
        children = EXPAND(node)
        fringe = INSERT_ALL(children, fringe)
        print("fringe: {}".format(fringe))


'''
Expands node and gets the successors (children) of that node.
Return list of the successor nodes.
'''
def EXPAND(node):
    successors = []
    children = successor_fn(node.STATE)
    for child in children:
        s = Node(node)  # create node for each in state list
        s.STATE = child  # e.g. result = 'F' then 'G' from list ['F', 'G']
        s.PARENT_NODE = node
        s.DEPTH = node.DEPTH + 1
        successors = INSERT(s, successors)
    return successors


'''
Insert node in to the queue (fringe).
'''
def INSERT(node, queue):
    #queue.insert(0, node)  # DFS
    queue.append(node)      # BFS
    return queue


'''
Insert list of nodes into the fringe
'''
def INSERT_ALL(list, queue):
    for node in list:
        INSERT(node, queue)
    return queue


'''
Remove first element from fringe
'''
def REMOVE_FIRST(queue):
    if len(queue) != 0:
        return queue.pop(0)
    return []


'''
Successor function, mapping the nodes to its successors
'''
def successor_fn(state):  # Lookup list of successor states
    return STATE_SPACE[state]  # successor_fn( 'C' ) returns ['F', 'G']


def environment_fn(width, height):
    states = []
    environment = {}
    for x in range (1, width):
        for y in range (1, height):
            for z in range (1, (x*y)**2):
                states.append([(x,y)])

    for state in states:
        while len(state) <= width * length + 2 :
            state.append('Dirty')


            environment[state] = []



INITIAL_STATE = ('A', 'Dirty', 'Dirty')
# Note: In this case, goal state is when vacuum goes back to location A and both A and B are clean
# Can also be: GOAL_STATE = ('B', 'Clean', 'Clean')
GOAL_STATE = ('A', 'Clean', 'Clean')

'''
Complete state space including loops back to current state
Note: with loops back to current state, the DFS can be stuck in an infinite loop,
so in that case BFS is used to find the path to the goal state
'''
#                  Current State - Actions:                            ---LEFT---                                  ---SUCK---                             ---RIGHT---                                   ---UP---                                   ---DOWN---
STATE_SPACE = {('A', 'Dirty', 'Dirty', 'Dirty', 'Dirty'): [('A', 'Dirty', 'Dirty', 'Dirty', 'Dirty'), ('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('B','Dirty', 'Dirty', 'Dirty', 'Dirty'), ('A','Dirty', 'Dirty', 'Dirty', 'Dirty'), ('C','Dirty', 'Dirty', 'Dirty', 'Dirty') ],
               ('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'): [('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('B','Clean', 'Dirty', 'Dirty', 'Dirty'), ('A','Clean', 'Dirty', 'Dirty', 'Dirty'), ('C','Clean', 'Dirty', 'Dirty', 'Dirty') ],
               ('A', 'Clean', 'Clean', 'Dirty', 'Dirty'): [('A', 'Clean', 'Clean', 'Dirty', 'Dirty'), ('A', 'Clean', 'Clean', 'Dirty', 'Dirty'), ('B','Clean', 'Clean', 'Dirty', 'Dirty'), ('A','Clean','Clean', 'Dirty', 'Dirty'), ('C', 'Clean', 'Clean', 'Dirty', 'Dirty')],
               ('A', 'Clean', 'Clean', 'Clean', 'Dirty'): [('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('B', 'Clean', 'Clean', 'Clean', 'Dirty'), ('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('C', 'Clean', 'Clean', 'Clean', 'Dirty')],
               ('A', 'Clean', 'Clean', 'Clean', 'Clean'): [('A', 'Clean', 'Clean', 'Clean', 'Clean'), ('A', 'Clean', 'Clean', 'Clean', 'Clean'), ('B', 'Clean', 'Clean', 'Clean', 'Clean'), ('A', 'Clean', 'Clean', 'Clean', 'Clean'),('C', 'Clean', 'Clean', 'Clean', 'Clean')],

               ('A', 'Dirty', 'Clean', 'Clean', 'Clean'): [('A', 'Dirty', 'Dirty', 'Dirty', 'Dirty'), ('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('B','Dirty', 'Dirty', 'Dirty', 'Dirty'), ('A','Dirty', 'Dirty', 'Dirty', 'Dirty'), ('C','Dirty', 'Dirty', 'Dirty', 'Dirty') ],
               ('A', 'Dirty', 'Clean', 'Dirty', 'Dirty'): [('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('B','Clean', 'Dirty', 'Dirty', 'Dirty'), ('A','Clean', 'Dirty', 'Dirty', 'Dirty'), ('C','Clean', 'Dirty', 'Dirty', 'Dirty') ],
               ('A', 'Dirty', 'Clean', 'Clean', 'Dirty'): [('A', 'Clean', 'Clean', 'Dirty', 'Dirty'), ('A', 'Clean', 'Clean', 'Dirty', 'Dirty'), ('B','Clean', 'Clean', 'Dirty', 'Dirty'), ('A','Clean','Clean', 'Dirty', 'Dirty'), ('C', 'Clean', 'Clean', 'Dirty', 'Dirty')],
               ('A', 'Dirty', 'Clean', 'Dirty', 'Clean'): [('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('B', 'Clean', 'Clean', 'Clean', 'Dirty'), ('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('C', 'Clean', 'Clean', 'Clean', 'Dirty')],
               ('A', 'Dirty', 'Dirty', 'Dirty', 'Clean'): [('A', 'Clean', 'Clean', 'Clean', 'Clean'), ('A', 'Clean', 'Clean', 'Clean', 'Clean'), ('B', 'Clean', 'Clean', 'Clean', 'Clean'), ('A', 'Clean', 'Clean', 'Clean', 'Clean'),('C', 'Clean', 'Clean', 'Clean', 'Clean')],
               ('A', 'Dirty', 'Dirty', 'Dirty', 'Dirty'): [('A', 'Dirty', 'Dirty', 'Dirty', 'Dirty'), ('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('B','Dirty', 'Dirty', 'Dirty', 'Dirty'), ('A','Dirty', 'Dirty', 'Dirty', 'Dirty'), ('C','Dirty', 'Dirty', 'Dirty', 'Dirty') ],
               ('A', 'Dirty', 'Dirty', 'Clean', 'Clean'): [('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('A', 'Clean', 'Dirty', 'Dirty', 'Dirty'), ('B','Clean', 'Dirty', 'Dirty', 'Dirty'), ('A','Clean', 'Dirty', 'Dirty', 'Dirty'), ('C','Clean', 'Dirty', 'Dirty', 'Dirty') ],
               ('A', 'Dirty', 'Dirty', 'Clean', 'Dirty'): [('A', 'Clean', 'Clean', 'Dirty', 'Dirty'), ('A', 'Clean', 'Clean', 'Dirty', 'Dirty'), ('B','Clean', 'Clean', 'Dirty', 'Dirty'), ('A','Clean','Clean', 'Dirty', 'Dirty'), ('C', 'Clean', 'Clean', 'Dirty', 'Dirty')],
               ('A', 'Clean', 'Dirty', 'Clean', 'Dirty'): [('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('B', 'Clean', 'Clean', 'Clean', 'Dirty'), ('A', 'Clean', 'Clean', 'Clean', 'Dirty'), ('C', 'Clean', 'Clean', 'Clean', 'Dirty')],
               ('A', 'Clean', 'Dirty', 'Clean', 'Clean'): [('A', 'Clean', 'Clean', 'Clean', 'Clean'), ('A', 'Clean', 'Clean', 'Clean', 'Clean'), ('B', 'Clean', 'Clean', 'Clean', 'Clean'), ('A', 'Clean', 'Clean', 'Clean', 'Clean'),('C', 'Clean', 'Clean', 'Clean', 'Clean')],
               ('A', 'Clean', 'Dirty', 'Dirty', 'Clean'): [('A', 'Clean', 'Clean', 'Clean', 'Clean'), ('A', 'Clean', 'Clean', 'Clean', 'Clean'), ('B', 'Clean', 'Clean', 'Clean', 'Clean'), ('A', 'Clean', 'Clean', 'Clean', 'Clean'),('C', 'Clean', 'Clean', 'Clean', 'Clean')],

               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'):[],
               ('B', 'Dirty', 'Clean', 'Dirty', 'Dirty'):[],
               ('B', 'Dirty', 'Dirty', 'Clean', 'Dirty'):[],
               ('B', 'Dirty', 'Dirty', 'Dirty', 'Clean'):[],
               ('B', 'Dirty', 'Clean', 'Clean', 'Dirty'):[],
               ('B', 'Dirty', 'Dirty', 'Clean', 'Clean'):[],
               ('B', 'Dirty', 'Clean', 'Dirty', 'Clean'):[],
               ('B', 'Clean', 'Dirty', 'Dirty', 'Dirty'):[],
               ('B', 'Clean', 'Clean', 'Dirty', 'Dirty'):[],
               ('B', 'Clean', 'Dirty', 'Clean', 'Dirty'):[],
               ('B', 'Clean', 'Dirty', 'Dirty', 'Clean'):[],
               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'):[],
               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'):[],
               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'):[],
               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'):[],
               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'):[],




               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'): [('A', 'Dirty', 'Dirty', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Clean', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'), ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty'), ('D', 'Dirty', 'Dirty', 'Dirty', 'Dirty')],






               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty')
               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty')
               ('B', 'Dirty', 'Dirty', 'Dirty', 'Dirty')
               ('B', 'Dirty', 'Clean'): [('A', 'Dirty', 'Clean'), ('B', 'Dirty', 'Clean'), ('B', 'Dirty', 'Clean')],
               ('B', 'Clean', 'Dirty'): [('A', 'Clean', 'Dirty'), ('B', 'Clean', 'Clean'), ('B', 'Clean', 'Dirty')],
               ('A', 'Dirty', 'Clean'): [('A', 'Dirty', 'Clean'), ('A', 'Clean', 'Clean'), ('B', 'Dirty', 'Clean')],
               ('A', 'Clean', 'Clean'): [('A', 'Clean', 'Clean'), ('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')],
               ('B', 'Clean', 'Clean'): [('A', 'Clean', 'Clean'), ('B', 'Clean', 'Clean'), ('B', 'Clean', 'Clean')],
               ('C', 'Clean', 'Clean')
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

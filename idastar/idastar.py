
import random
from math import inf
from action import Action

### Iterative Deepening A* -- IDA*

totalcalls = 0
        
def IDAstar(s0,goaltest,h):
    global totalcalls
    bound = h(s0)
    totalcalls = 0
    while True:
        print("Calling doDFS with bound " + str(bound))
        t = doDFS(s0,0,bound,goaltest,h,[s0])
        if t==None:
            print("TIMEOUT")
            return None
        if isinstance(t,list):
            print("SOLVED (" + str(totalcalls) + " recursive calls)")
            return t
        if t == float('inf'):
            print("NOT SOLVABLE")
            return None
        bound = t

# The main subprocedure of IDA*, performing DFS up to a given
# bound.
# doDFS returns
#   None                if spent too much time
#   a list of actions   if a shortest path to goal states was found
#   a number            for the next bound otherwise
#
# The arguments are
#    s        The state to search
#    g        The g-value of 's'
#    bound    The threshold to cut off the DFS search
#    goaltest Function to test if 's' is a goal state
#    h        The function for computing the h-value of 's'
#    path     List of all states encountered in the current
#             branch. Test successors s2 of s with "s2 in path"
#             to see if the path would have a cycle (and then
#             ignore that kind of s2.)

def doDFS(s,g,bound,goaltest,h,path):
    global totalcalls
    totalcalls = totalcalls + 1
    if totalcalls > 10000000:
        return None
    f_score = g + h(s)
    if f_score > bound:
        return f_score
    if goaltest(s):
        return []
    minimum = float('inf')
    for successor in s.successors():
        action, state = successor
        if state not in path:
            path.append(state)
            t = doDFS(state, g + action.cost, bound, goaltest, h, path)
            if isinstance(t, list):
                t.insert(0, action)
                return t
            if t == None:
                return None
            if t < minimum:
                minimum = t
            path.pop()
    return minimum


### Write your code here
### Write your code here
### Write your code here
### Write your code here
### Write your code here
### Write your code here
### Write your code here
### Write your code here
### Write your code here
### Write your code here
### Write your code here
### Write your code here

### NOTE: The grader will call both IDAstar and doDFS, so keep
### the interfaces to these intact. (We need to check doDFS
### separately because otherwise you could plug in your A*
### implementation as an IDA* impersonation. ;-) )

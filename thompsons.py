#01.03.19
#Thompson's construction

# represents a state with 2 arrows, labelled by label.
# use None for a label representing "e" arrows 
class state:
    label, edge1, edge2 = None, None, None
    
# an NFA is represented by its initial and accept states
class nfa:
    initial, accept  = None, None
    
    def __init__(self, initial, accept):
        self.initial = initial
        self.accept = accept

def compile (pofix):
    nfastack = []


    for c in pofix:
        if c == '.':
            # pop 2 NFA's off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # connect first NFA's accept state to the second's initial
            nfa1.accept.edge1 = nfa2.initial 
            # push NFA to the stack
            nfastack.append(nfa(nfa1.initial, nfa2.accept))
        elif c == '|':
            # pop 2 nfas off the stack
            nfa2 = nfastack.pop()
            nfa1 = nfastack.pop()
            # create a new initial state, connect it to initial states
            # of the 2 NFA's popped from the stack
            initial = state()
            initial.edge1 = nfa1.initial
            initial.edge2 = nfa2.initial
            # create a new accept state, connecting the accept states
            # of the 2 NFA's popped from the stack, to the new state
            accept = state()
            nfa1.accept.edge1 = accept
            nfa2.accept.edge2 = accept
            # push new nfa to the stack
            nfastack.append(nfa(initial, accept))
        elif c == '*':
            # pop a single NFA from the stack
            nfa1 = nfastack.pop()
            # create new initial and accept states
            initial = state()
            accept = state()
            #join the new initial state to the NFA's initial state and the new accept state
            initial.edge1 = nfa1.initial
            initial.edge2 = accept# join the old accept state to the new accept state and nfa1's initial state
            nfa1.accept.edge1 = nfa1.initial
            nfa1.accept.edge2 = accept
            #push new NFA to the stack
            nfastack.append(nfa(initial, accept))
        else:
            accept = state() #instance of class state, same as new in java   #first circle
            initial = state()#second circle
            initial.label = c # join 2 circles with a c character: a, b, c, etc 
            initial.edge1 = accept #points to the accept state
            newnfa = nfa(initial, accept)
            nfastack.append(newnfa)
            #nfastack = append(nfa(initial, accept))
            
# nfastack should only have a single nfa on it at a time
    return nfastack.pop()

print(compile("ab.cd|"))
print(compile("aa*"))





















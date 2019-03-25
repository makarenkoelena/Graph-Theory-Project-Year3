#g00341964 
#Elena Makarenko
"""Shunting Yard Algorithm for converting infix regular expressions to postfix"""

def shunt(infix):

    specials = {'+' : 60,'*' : 50, '.' : 40, '|' : 30}

    pofix= ""
    stack= ""

    for c in infix:
        if c == '(':
            stack = stack + c 
            #put ( on the stack
        elif c == ')':
            while stack [-1] !='(':#while the last char on the stack is not (
                #put all the operands from the stack into pofix the whole way back
                #delete everything up to but not including the last char from the stack starting from the top of the stack 
                pofix, stack = pofix+stack[-1], stack[:-1]
            stack = stack[:-1]#delete ) from the stack
        elif c in specials:
            #is there any operator of higher precedence?
            #if not put the next operator at the stack otherwise put into pofix
            #delete it from the stack

            # while stack same as while stack !="", while there is anything on the stack
            #check if there is in the dictionary give it its value otherwise give 0
            while stack and specials.get(c, 0) <= specials.get(stack[-1], 0):
                pofix, stack = pofix+stack[-1], stack[:-1]
            stack = stack + c
        else: pofix = pofix + c

    #if there is anything left on the stack, put it into pofix, clear the stack
    while stack:
        pofix, stack = pofix+stack[-1], stack[:-1]

    return pofix

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
        elif c == '+':
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

#print(compile("ab.cd|"))
#print(compile("aa*"))

def followes(state):
    """Return the set of states that can be reached from state following e arrows."""
    states = set()
    states.add(state)

    #check if state has arrows labelled e from it
    if state.label is None:
        if state.edge1 is not None:
        #if there's an edge1, follow it
         states |= followes(state.edge1)
        if state.edge2 is not None:
        #if there's an edge1, follow it
         states |= followes(state.edge2)
    
    return states

def match(infix, string):
    """Matches string to infix regular expression."""
    postfix  = shunt(infix)
    nfa = compile(postfix)

    current = set()
    next = set()

    # add the initial state to the current set
    current |= followes(nfa.initial)
    
    for s in string:
        for c in current:
            #check if that state is labelled s.
            if c.label == s:
                #add the edge1state to the next set
                next |= followes(c.edge1)
        #set current to next, and clear out next
        current= next
        next = set()

    return (nfa.accept in current)

#print(shunt("(a.b)|(c*.d)"))

infixes=["a.b.c", "a.(b|d).c*", "(a.(b|d))", "a.(b|b)*.c"]
strings=["", "abc", "abbc", "abcc", "abad", "abbbc"]

for i in infixes:
    for s in strings:
        print (match(i, s), i, s)
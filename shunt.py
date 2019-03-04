#g00341964 
#Elena Makarenko
#Shunting Yard Algorithm
#ref

def shunt(infix):

    specials = {'*' : 50, '.' : 40, '|' : 30}

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

print(shunt("(a.b)|(c*.d)"))
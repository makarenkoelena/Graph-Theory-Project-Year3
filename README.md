# Graph-Theory-Project-Year3

Converting regular expression to NFA
The first nondeterministic aspect of an NFA comes from the ability to transit from a current state on the same symbol to different states.
Another property which is possible only in an NFA, is the ability to have epsilon-transitions (aka e-transitions).

Basic NFA-fragments for regular expression
1. Character fragment
The following image illustrates an NFA of an empty string and an NFA of a string containing just 1 character (character a in this particular case)
![DFA](img/NFAempty&singleCharacter.png?raw=true "hoverover")

2. Binary operators (requires 2 operands):
2.1 Union fragment
The union NFA fragment defines the “OR” operation. It is also known as “disjunction” operation.
Regex can look like:  a|b
It has the lowest precedence(they are done the last ones if there are no brackets)
NFA can be represented in 2 ways:
![DFA](img/NFAor.png?raw=true "hoverover")

2.2 Concatenation fragment
The concatenation NFA-fragment defines the “A followed by B” operation 
Regex can look like: ab.
NFA can be represented in 2 ways:
![NFA](img/NFAdot.png?raw=true "hoverover")

3. Unary operators
3.1 Kleene-closure/Kleene-star fragment
The Kleene-closure operator defines the repetition pattern ( “zero or more times”).

Regex can look like: a*. This accepts strings such as: "" (the empty string), "a", "aa", "aaa", etc.

3.2 Plus fragment 
Also defines the repetition pattern (1 or more).
Regex can look like: a+. This accepts strings such as: "a", "aa", "aaa", etc.

3.3 Question mark fragment 
Sort of repetition pattern as well (0 or 1).
Regex can look like: a?. This accepts strings such as: "", "a".

The following image illustrates the unary operators:
![NFA](img/unaryNFA.png?raw=true "hoverover")

Reference: 
http://infolab.stanford.edu/~ullman/ialc/spr10/slides/re1.pdf
https://medium.com/@DmitrySoshnikov/building-a-regexp-machine-part-2-finite-automata-nfa-fragments-5a7c5c005ef0

[this is a comment]

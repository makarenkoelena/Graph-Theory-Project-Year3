# Graph-Theory-Project-Year3

<h4>Description</h4>

This is a python program which takes 2 inputs: a string and a regular expression.
1. Firstly, it converts regular expression from infix to postfix notation,
2. Secondly, builds a non-deterministic finite automaton (NFA) from a regular expression
3. Finally, compares a string and a regular expression ("runs" the given string through the NFA)
As an output it returns a boolean : true if a string matches the regex (by reaching the end of the string one of the states it ends up in is an accept state) 
and false if it doesn't(by reaching the end of the string none of the states it ends up in is an accept state).

<h4>Design Decisions & Issues</h4>

The main algorithms that were used: Shunting Yard algorithm, Thompson's constructor algorithm and Matching algorithm are explained below:

<b>"Shunting Yard algorithm: Converting infix notation regex to postfix notation"</b>

1. If an operand is encountered, add it to postfix.
2. If a left parenthesis is encountered, push it onto Stack.
3. If an operator is encountered ,then:
   Repeatedly pop from Stack and add to postfix each operator (on the top of Stack) which has the same precedence as or higher precedence than operator.
   Add operator to Stack.
4. If a right parenthesis is encountered ,then:
   Repeatedly pop from Stack and add to postfix each operator (on the top of Stack) until a left parenthesis is encountered.
   Remove the left Parenthesis.
   
![DFA](img/shuntingExample.png?raw=true "hoverovertext")

<b>"Thompson's construction : Converting regular expression to NFA"</b>
The first nondeterministic aspect of an NFA comes from the ability to transit from a current state on the same symbol to different states.
Another property which is possible only in an NFA, is the ability to have epsilon-transitions (aka e-transitions).

Basic NFA-fragments for regular expression
1. Character fragment
The following image illustrates an NFA of an empty string and an NFA of a string containing just 1 character (character a in this particular case)
![DFA](img/NFAempty&singleCharacter.png?raw=true "hoverovertext")

2. Binary operators (requires 2 operands):
2.1 Union fragment
The union NFA fragment defines the “OR” operation. It is also known as “disjunction” operation.
Regex can look like:  a|b
It has the lowest precedence(they are done the last ones if there are no brackets)
NFA can be represented in 2 ways:
![NFA](img/NFAor.png?raw=true "hoverovertext")

2.2 Concatenation fragment
The concatenation NFA-fragment defines the “A followed by B” operation 
Regex can look like: ab.
It has the second lowest precedence after union fragment
NFA can be represented in 2 ways:
![NFA](img/NFAdot.png?raw=true "hoverovertext")

3. Unary operators
All unary operators have the highest precedence.
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
![NFA](img/unaryNFA.png?raw=true "hoverovertext")

<br>"Regex Matching algorithm"</br>
The following image is the illustration how to convert a regex to a NFA and check if the string matches the NFA. 
![NFA](img/matching.png?raw=true "hoverovertext")

<h4> How to run the program </h4>
Depending on the number of parameters the user enters:
1 - e.g. python thompsons.py
User will be prompt to enter regex and string.
2 - e.g. python thompsons.py strings.txt
Second parameter is the name of the file, which regex needs to be executed on. If file does not exist or misspelt, the following message is displayed: "File not found"
User will be prompt to enter a regex.
3 - e.g. python thompsons.py a.b.c abc
User enters regex and string as a part of command arguments.

In order to run "hard coded" tests please uncomment lines 186-190.

<h4>Python "features":</h4>

1. 	syntax for a constructor

	def __init__(self, argument1, argument2):
	self.argument1 = argument1
	self.argument2 = argument2
	
2. 	several assignments in one statement
	argument1 = None
	argument2 = None	
	
	can also be written as
	argument1, argument2 = None, None
	
3.  	instance of the class
	classInstance = className()
	same as ClassName classInstance = new ClassName(); in java

4.  	dictionary = {'A' : 1, 'B' : 2,'C' : 3, 'D' : 4, 'E' : 5}
	dictionary.get(item, 0)
	which means if there is such an item in the dictionary give its value otherwise give the value 0 

5. 	sys library (System-specific parameters and functions)
	sys.argv - The list of command line arguments passed to a Python script. argv[0] is the script name. 

6. 	os.path library
	os.path.exists(path)
	Return True if path refers to an existing path. Returns False for broken symbolic links. On some platforms, this function may return False if permission is not granted to execute os.stat() on the requested file, even if the path physically exists.
	
References: 
<p>http://www.oxfordmathcenter.com/drupal7/node/628</p>
<p>http://interactivepython.org/runestone/static/pythonds/BasicDS/InfixPrefixandPostfixExpressions.html</p>
<p>https://www.includehelp.com/c/infix-to-postfix-conversion-using-stack-with-c-program.aspx</p>
<p>http://infolab.stanford.edu/~ullman/ialc/spr10/slides/re1.pdf</p>
<p>https://medium.com/@DmitrySoshnikov/building-a-regexp-machine-part-2-finite-automata-nfa-fragments-5a7c5c005ef0</p>
<p>https://www.youtube.com/watch?v=RYNN-tb9WxI</p>
<p>https://docs.python.org/3/</p>
<p>video and lectures slides provided</p>

P.S. One of the requirements/suggestions in project specification was to remove the concatenation
character, so that 1.0 becomes 10, with the concatenation implicit. In this case it is not clear for me how to distinguish between 1 followed by a zero and a single character 10.
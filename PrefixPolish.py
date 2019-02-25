# PostfixPolish.py
# Eli Oceanak
# Cosc 2150 Lab 03
# Section 10

import operator #defines operators
ops = {
       '+':operator.add,
       '-':operator.sub,
       '*':operator.mul,
       '/':operator.truediv,
       '^':operator.pow
       }

def is_number(s): #checks if the input is a number
    try:
        float(s)
        return True
    except ValueError:
        pass

def calculate(exp): #actually calculates the polish expression
    stack = []
    newstack = []
    result = 0
    for i in exp: #makes a list out of the line, makes it postfix
        stack.insert(0,i)
    print(stack)
    for i in stack: #evaluates as if it was postfix
        if is_number(i):
            newstack.insert(0,i)
        else:
            if len(stack) < 2:
                print ('Error: insufficient values in expression')
                break
            else:
                print ('stack: ', newstack, 'where i = ', i)
                operand1 = float(newstack.pop(1))
                operand2 = float(newstack.pop(0))
                result = ops[i](operand1,operand2)
                newstack.insert(0,str(result))
    return result #returns the answer

print ("Start of Prefix Polish Notation Evaluator")
exp_file = open("Expressions1.1.txt", 'r')
for line in exp_file: #every expression in exp_file gets evaluated
        exp_list = line.rstrip().split(' ')
        answer = calculate(exp_list)
        print ('RESULT: %f' % answer)
print ("End of Reverse Polish Notation Evaluator")

from typing import List

"""*********************************************************************
############################## EXPRESSION ##############################
*********************************************************************"""

class Expression:
    def __init__(self):
        # this should have a type field
        pass

class NumberExpression(Expression):
    def __init__(self, num: float):
        self.value = num

class VariableExpression(Expression):
    def __init__(self, name: str):
        self.name = name

class BinaryExpression(Expression):
    """
    operator: > < + - * / -= += etc...
    left, right: AST_TYPE
    """
    def __init__(self, operator: str, leftAST: Expression, rightAST: Expression):
        self.operator = operator
        self.leftAST = leftAST
        self.rightAST = rightAST

class CallExpression(Expression): # Invoke ()
    def __init__(self, invokee: str, arguments: List[Expression]):
        self.invokee = invokee
        self.arguments = arguments

"""                             EXPRESSION                            """

class Prototype:
    """
    the prototype for a function,
    """
    def __init__(self, name: str, arguments: List[str]):
        self.name = name
        self.arguments = arguments

    def getName(self) -> str:
        return self.name;

class Function:
    def __init__(self, prototype: Prototype, body: Expression):
        self.prototype = prototype
        self.body = body


left = VariableExpression('x')
right = VariableExpression('y')
result = BinaryExpression('+', left, right)


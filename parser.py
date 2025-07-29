
'''
Given a mathematical expression x + y * [a + (b-c)],
[] - 
() * / => Those are the expression
'''

from logging import raiseExceptions
from token import MINUS
from typing import Any
from lexer import Lexer, Token, Token_Type
import lexer


class Node:
    def __init__(self, value, left, right):
        self.value = value
        self.left = left
        self.right = right

#Looks for '+' and '-' operations
class ExpressionNode (Node):
    def __init__(self, value, left, right):
        super().__init__(value,left,right)
    
    def is_sum(self) -> bool:
        return self.value == '+'

#Looks for '*' and '/' operators
class FactorNode (Node):
    def __init__(self, value, left, right):
        super().__init__(value,left,right)
    
    def is_multiplication(self) -> bool:
        return self.value == '*'

class NegativeNode:
    def __init__(self, term):
        self.term = term

class TermNode (Node):
    def __init__(self, value, left, right):
        super().__init__(value,left,right)

class Parser:

    def __init__(self, tk_list):
        self.token_list = tk_list
        self.previous: Any | Token = None
        self.current: Any | Token = None
        self.token_index = 0
        self.advance()
        self.expressionNode =  self.parse()
    
    def parse(self):
        result = self.expression()

        if(self.current != None): raise Exception("Some token was not used")

        return result
    
    def advance(self):
        self.previous = self.current
        if self.token_index >= len(self.token_list):
            self.current = None
        else:
            self.current = self.token_list[self.token_index]
        self.token_index += 1

    def expression(self):
        factorNode = self.factor()

        while self.current != None and self.current.token_type in (Token_Type.MINUS, Token_Type.PLUS):
            self.advance()
            factorNode =  ExpressionNode(self.previous.lexeme, factorNode, self.factor())
        
        return factorNode #In case there is no + or -

    def factor(self):
        termNode = self.term()
        while self.current != None and self.current.token_type in (Token_Type.DIVIDE, Token_Type.MULTIPLY):
            self.advance()
            termNode = FactorNode(self.previous.lexeme,termNode, self.term())
        
        return termNode

    def term(self):
        number: Token | Any = self.current

        if number.token_type == Token_Type.DIGITS:
            self.advance()
            return TermNode(number.lexeme, None, None)
        
        elif number.token_type == Token_Type.MINUS:
            self.advance()
            return NegativeNode(self.term())
        
        elif number.token_type == Token_Type.OPEN_B:
            self.advance()
            result = self.expression()
            if self.current.token_type != Token_Type.CLOSE_B:
                raise Exception("No closing brackets")
            self.advance()
            return result

        elif number.token_type == Token_Type.OPEN_P:
            self.advance()
            result = self.expression()
            if self.current.token_type != Token_Type.CLOSE_P:
                raise Exception("No closing parenthesis")
            self.advance()
            return result
        
        else:
            raise Exception("Invalid term")
    
    def printExpression(self, node: Node | None):
        if(node == None): return ''
        else: 
            return self.printExpression(node.left) + '' + node.value  + '' + self.printExpression(node.right) 

# a = Lexer("10 + [(2 + 1) * [9 / 10]]")
# b = Parser(a.token_list)

#print(b.printExpression(b.expressionNode))
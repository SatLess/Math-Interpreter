from unittest import result
from lexer import Lexer
from parser import ExpressionNode, FactorNode, NegativeNode, Node, Parser, TermNode
from typing import Any


class Interpreter:

    def __init__(self, astTree: ExpressionNode):
        self.tree = astTree
        self.result = 0
        self.current : Node | Any = self.tree
        self.stack : list[Node]
        self.result = self.interpret(self.tree)
    
    def interpret(self, node):

        result = 0
        
        #For Sum and Subtraction
        if isinstance(node, ExpressionNode):

            is_sum = node.is_sum()
            result = self.interpret(node.left) + self.interpret(node.right) if is_sum \
            else self.interpret(node.left) - self.interpret(node.right)
            return result
            
        #For Division and Multiplication
        elif isinstance(node, FactorNode):
            is_multiplying = node.is_multiplication()
            result = self.interpret(node.left) * self.interpret(node.right) if is_multiplying \
            else self.interpret(node.left) / self.interpret(node.right)
            return result   

        #If its just a number, hold on
        elif isinstance(node, TermNode):
            return float(node.value)
        
        elif isinstance(node, NegativeNode):
            result = self.interpret(node.term) * -1
            return result
        
        else:
            raise Exception("Something wrong")
        


    
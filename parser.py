from typing import Any
from lexer import Token, Token_Type


class DigitNode():
    
    value: Any
    def __init__(self, value: Any):
        self.value = value


#Maybe I should remove this class in order to strictly follow the grammar, and have it so express nodes add and factors multiply
class OperatorNode():
    operator_type: Token_Type
    left_side: Any #According to grammar, must be expression Type if parent == expr else Factor
    right_side: Any #According to grammar, must be factor type if parent == expr, else digit

    def __init__(self, type: Token_Type):
        if type != Token_Type.MULTIPLY or type != Token_Type.DIVIDE or type != Token_Type.MINUS or type != Token_Type.PLUS:
            raise Exception("Type is not operation")
        self.operator_type = type

class ExpressionNode():
    operator_node: OperatorNode

    def __init__(self, is_sum: bool):
        if is_sum:
            self.operator_node = OperatorNode(Token_Type.PLUS)
        else:
            self.operator_node = OperatorNode(Token_Type.MINUS)


class FactorNode():
    left_side: Any #According to grammar, must be expression Type if parent == expr else Factor
    right_side: Any #According to grammar, must be factor type if parent == expr, else digit



class Parser():
    
    token_list: list = []

    def consume(self): pass

from interpreter import Interpreter
from lexer import Lexer
from parser import Parser


while True:
    text = input("Input a mathematical expression ")
    if len(text) == 0: break
    lexer = Lexer(text)
    parser = Parser(lexer.token_list)
    interpreter = Interpreter(parser.expressionNode)
    print(interpreter.result)
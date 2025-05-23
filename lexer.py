from calendar import c
from enum import Enum
from pickle import NONE
from token import MINUS, PLUS
from tokenize import String
from unicodedata import digit


WHITESPACE = ' \n\t'
DIGITS = '0123456789.' ##TODO add support for '.' one day
OPERATORS = '+-*/' 
SPECIAL_KEYS = '()[]' 

class Token_Type(Enum):
    DIGITS = 1 # 1,2,...
    #Special Keys
    OPEN_P = 2 # (
    CLOSE_P = 3 # )
    OPEN_B = 4 #[
    CLOSE_B = 5 #[
    PERIOD = 6
    #Operators
    PLUS = 7
    MINUS = 8
    MULTIPLY = 9
    DIVIDE = 10

class Token:
    token_type = -1
    lexeme = "" #the symbol that is typed and tokenized
    
    def __init__(self, type, lexeme):
        self.token_type = type
        self.lexeme = lexeme


#Actualy transforms shit into tokens
class Lexer:
    source_code = ""
    digit_lexeme = "" #For now that'll append digit for us 
    source_size = 0
    cursor_pos = 0
    token_list: list = []

    def __init__(self, p_code):
        self.source_code = p_code
        self.source_size = len(p_code)
        self.__generate_tokens()
        self.print_tokens()
        
    
    def advance(self):
        if self.cursor_pos >= self.source_size: return " "
        c = self.source_code[self.cursor_pos] 
        self.cursor_pos += 1
        return c

    def get_current_char(self):
        if self.cursor_pos >= self.source_size: return " "
        return self.source_code[self.cursor_pos] 

    def __generate_tokens(self):
        while self.cursor_pos < self.source_size:
            c = self.advance()
            type = self.__match_token_type(c)
            token: Token

            if c in WHITESPACE: continue

            if type == Token_Type.DIGITS:
                digits = c
                next_digit = self.get_current_char()
                while self.__match_token_type(next_digit) == Token_Type.DIGITS:
                    digits += next_digit
                    c = self.advance()
                    next_digit = self.get_current_char()
                token = Token(type,digits)
            
            elif type == None:
                raise Exception("Why girls?")

            else: token = Token(type,c)

            self.token_list.append(token)
                

    def __match_token_type(self,c):

        if c in DIGITS: return Token_Type.DIGITS

        match c:
            case '+': return Token_Type.PLUS
            case '-': return Token_Type.MINUS
            case '/': return Token_Type.DIVIDE
            case '*': return Token_Type.MULTIPLY

            case '(': return Token_Type.OPEN_P
            case ')': return Token_Type.CLOSE_P

            case '[': return Token_Type.OPEN_B
            case ']': return Token_Type.CLOSE_B
            
            case _: return None

    def print_tokens(self):
        for i in self.token_list:
            print(i.lexeme)
        
test = Lexer("123 + 789 - (2 * 3)")

        
    
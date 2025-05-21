from calendar import c
from enum import Enum


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
    source_size = 0
    cursor_pos = 0
    token_list = []

    def __init__(self, p_code):
        self.source_code = p_code
        self.source_size = len(p_code)
        self.__generate_tokens()
        self.print_tokens()
        
    
    def advance(self):
        if self.cursor_pos >= self.source_size: return ""
        c = self.source_code[self.cursor_pos] 
        self.cursor_pos += 1
        return c

    def get_previous_lexemme(self):
        return self.source_code[self.cursor_pos - 1] 

    def __generate_tokens(self):
        while self.cursor_pos < self.source_size:
            c = self.advance()

            if c in WHITESPACE: continue
            elif c in DIGITS:
                token = Token(Token_Type.DIGITS, self.__generate_numbers())
                self.token_list.append(token)
            elif c in OPERATORS or c in SPECIAL_KEYS:
                token = Token(self.__match_token_type(c), c)
                self.token_list.append(token)
            else:
                print("Token " + c + " is invalid")
                return

                

    def __match_token_type(self,c):
        match c:
            case '+': return Token_Type.PLUS
            case '-': return Token_Type.MINUS
            case '/': return Token_Type.DIVIDE
            case '*': return Token_Type.MULTIPLY

            case '(': return Token_Type.OPEN_P
            case ')': return Token_Type.CLOSE_P

            case '[': return Token_Type.OPEN_B
            case ']': return Token_Type.CLOSE_B

    def __generate_numbers(self): #TODO need to fix how this works loool like it joins toghether not good tokens toghether ie no token num
        num_digit = self.get_previous_lexemme()
        if (num_digit in DIGITS == False): return ""
        c = self.advance()
        if(c in WHITESPACE): return num_digit
        return num_digit + self.__generate_numbers() #Little bit confusing to understand, since we don't use c directly


    def print_tokens(self):
        for i in self.token_list:
            print(i.lexeme)
        
test = Lexer("123 + 789")

        
    
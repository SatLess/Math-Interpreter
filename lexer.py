from enum import Enum

WHITESPACE = ' \n\t'
DIGITS = '0123456789'

class Token_Type(Enum):
    IDENTIFIER = 1 # 1,2,...
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
    #Whitespace
    WHITESPACE = 11

class Token:
    token_type = -1
    lexeme = "" #the symboy that is typed and tokenized


#Actualy transforms shit into tokens
class Lexer:
    source_code = ""
    cursor_pos = 0
    token_list = []

    def __init__(self, p_code):
        self.source_code = p_code
        self.__generate_tokens()
        print(self.token_list)
        
    
    def advance(self): #returns lexeme grouped toghether
        c = self.source_code[self.cursor_pos] 

        if c in WHITESPACE: return None
        elif c in DIGITS: 
            num = self.generate_numbers(c)
            return num


    def __generate_tokens(self):
        while self.cursor_pos < len(self.source_code):
            token = self.advance()
            if(token != None):
                self.token_list.append(token)
            self.cursor_pos += 1

    def generate_numbers(self, c):
        self.cursor_pos += 1
        if self.cursor_pos >= len(self.source_code): return c
        token = self.advance()
        if token == None: return c
        return c + token
        

        
test = Lexer("123 456 789 1011")

        
    
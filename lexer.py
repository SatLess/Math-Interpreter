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
    token_type: Token_Type
    lexeme = "" #the symbol that is typed and tokenized
    
    def __init__(self, type, lexeme):
        self.token_type = type
        self.lexeme = lexeme
    
    def is_operator(self) -> bool:
        return self.token_type == (Token_Type.PLUS or Token_Type.MINUS or Token_Type. MULTIPLY or Token_Type.DIVIDE)


#Actualy transforms shit into tokens
class Lexer:
    source_code = ""
    source_size = 0
    cursor_pos = 0
    token_list: list[Token] = []

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
            if c in WHITESPACE: continue

            type = self.__match_token_type(c)
            if type == None: raise Exception("Why girls?")

            token: Token

            if type == Token_Type.DIGITS:
                digits = c
                hasDot = False
                next_digit = self.get_current_char()
                while self.__match_token_type(next_digit) == Token_Type.DIGITS:
                    if(next_digit == '.'):
                        if(hasDot): raise Exception("Nao pode mais que um ponto")
                        else: hasDot = True
                    digits += next_digit
                    c = self.advance()
                    next_digit = self.get_current_char()
                if(digits[len(digits) - 1] == '.'): digits += '0'
                token = Token(type,digits)

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


        
    
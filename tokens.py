from enum import Enum
from dataclasses import dataclass
'''
we will define all the different token types and do do that we will create
tokenType enum, each tokenType is going to have an ID
'''

class TokenType(Enum):
    NUMBER = 0
    PLUS = 1
    MINUS = 2
    MULTIPLY = 3
    DIVIDE = 4
    LPAREN = 5
    RPAREN = 6

'''
using dataclass decorator as it can hold different fields and values
'''
@dataclass
class Token:
    type: TokenType
    value: any = None


   #printing token in a nice format, predefined function in dataclass
    def __repr__(self):
        return self.type.name + (f":{self.value}" if self.value!= None else "")


from typing import List, Tuple
from re import compile as createRegex
import src.ast as ast

EOF = -1
FUNCTION = -2
EXTERN = -3 # unused
IDENTIFIER = -4
NUMBER = -5

_alphaRegex = createRegex("[a-zA-z][a-zA-z]*")
_numericalRegex = createRegex("[0-9][.0-9]*")

def _isAlpha(string: str) -> bool:
    return _alphaRegex.match(string) != None

def _isNumber(string: str) -> bool:
    return _numericalRegex.match(string) != None

def tokenize(content: str) -> List[Tuple[str, int]]:
    tokens: List[Tuple[str, int]] = []
    asts = []

    substring: str = ""
    i: int = 0
    line: int = 1
    col: int = 0

    while (i < len(content)):
        col += 1

        # skip whitespace
        if content[i] == " ":
            i += 1
            continue

        if content[i] == "\n":
            line += 1
            col = 0
            i += 1
            continue

        # ignore comments
        if content[i] == "#":
            while True:
                i += 1
                if content[i + 1] == "\n":
                    i += 1
                    line += 1
                    col = 0
                    break

        # handle [a-zA-z][a-zA-Z0-9]*
        elif _isAlpha(content[i]):
            substring += content[i]
            while _isAlpha(content[i + 1]):
                i += 1
                substring += content[i]

            token = None
            if substring == "func":
                token = FUNCTION
            else:
                token = IDENTIFIER

            tokens.append((substring, token))
            substring = ""

        # handle numbers
        elif _isNumber(content[i]):
            substring += content[i]

            while _isNumber(content[i + 1]):
                i += 1
                substring += content[i]

            tokens.append((substring, NUMBER))

            try:
                asts.append(ast.NumberExpression(float(substring)))
            except Exception as e:
                raise Exception(tokenizeError(line, col, str(e)))
            finally:
                substring = ""

        # just append acii value
        else:
            tokens.append((content[i], ord(content[i])))
        # increment while loop
        i = i + 1


    tokens.append(("", EOF))
    print(asts)
    return tokens

def tokenizeError(line: int, col: int, message: str) -> str:
    return "ERROR: line: %d, col: %d\n%s" % (line, col, message)

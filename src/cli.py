from src.evaluator import ZEval
from src.lexer import ZLexer
from src.parser import ZParser 

env = {}

def run(filename: str):
    with open(filename, "r") as file:
        lines = file.readlines()
        for line in lines:
            parser = ZParser()
            lexer = ZLexer()
            tree = parser.parse(lexer.tokenize(line))
            ZEval(tree, env)
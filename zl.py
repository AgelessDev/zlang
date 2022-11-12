import sys
from src.cli import run 

try:
    run(sys.argv[1])
except IndexError:
    print("-" * 40)
    print("Missing Parameter: path to .zl file")
    print("-" * 40)
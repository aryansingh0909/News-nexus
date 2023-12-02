import json
import ast

with open('asd.txt') as f:
    data = ast.literal_eval(f)
print(data)
from lexer import Lexer
from parser import Parser

print("Welcome to UnfinishedLang Pre-Alpha!")

while True:
	print("> ", end='')
	cmd = input('')
	tokens = Lexer(cmd)
	print(Parser(tokens))

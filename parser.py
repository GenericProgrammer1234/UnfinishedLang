import lexer

tokens = lexer.Lexer("2+2")

def Parser(tokens):
    new_tokens = []
    idx = 0
    while idx < len(tokens):
        token = tokens[idx]
        if token.type == "add" or token.type == "sub" or token.type == "div" or token.type == "mul":
            ftoken = new_tokens.pop()
            stoken = tokens[idx + 1].char
            idx += 2
            if token.type == "add":
                new_tokens.append(lexer.Token(ftoken.char + stoken, "int"))
            elif token.type == "sub":
                new_tokens.append(lexer.Token(ftoken.char - stoken, "int"))
            elif token.type == "div":
                new_tokens.append(lexer.Token(ftoken.char / stoken, "int"))
            elif token.type == "mul":
                new_tokens.append(lexer.Token(ftoken.char * stoken, "int"))
        else:
            new_tokens.append(token)
            idx += 1
    return new_tokens[0].char

result = Parser(tokens)
print(result)

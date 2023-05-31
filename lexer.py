line = "3*2+15-(3/2)"

class Token:

    def __init__(self, char, group):

        self.char = char

        self.type = group

    def __str__(self):

        return "{" + f"char={self.char},type={self.type}" + "}"

def throw(cont, err, charn, line):

    print(f"{cont} Error at line 1, char {charn}: {line}")

    print(f"Error: {err}")

def Lexer(line):

    charnum = 0

    tokens = []

    idx = 0

    while idx < len(line):

        char = line[idx]

        charnum += 1

        if char == "+":

            group = "add"

        elif char == "-":

            group = "sub"

        elif char == "/":

            group = "div"

        elif char == "*":

            group = "mul"
        elif char == "(":
            group = "obracket"
        elif char == ")":
            group = "cbracket"

        elif char.isdigit():


            num_chars = 1

            while idx + num_chars < len(line) and line[idx + num_chars].isdigit():

                num_chars += 1

            num_str = line[idx : idx + num_chars]

            idx += num_chars - 1

            group = "int"

            char = int(num_str)

        else:

            throw("Lexer", f"Unrecognized type for token ('{char}')", charnum, line)

            break

        token = Token(char, group)

        tokens.append(token)

        idx += 1

    for token in tokens:

        print(token)

Lexer(line)


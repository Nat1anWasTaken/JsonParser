from core.lexer import Lexer


def main():
    lexer = Lexer('{"a random key with spaces": "a random value with spaces"}')

    for token in lexer.lex():
        print(token)


if __name__ == "__main__":
    main()

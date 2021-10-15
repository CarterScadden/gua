from src.tokenize import tokenize

def main(message: str) -> None:
    try:
        with open("./test.gua") as file:
            content = file.read()

            tokens = tokenize(content)

            print(tokens)

    except Exception as e:
        print(e)

    finally:
        print(message)



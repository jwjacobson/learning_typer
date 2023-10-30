import typer

def main(firstname: str, lastname: str, formal: bool=False):
    if formal:
        print(f'Hello, {firstname.title()} {lastname.title()}')
    else:
        print(f'hey {firstname.lower()}')

if __name__ == "__main__":
    typer.run(main)

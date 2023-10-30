import typer

def main(firstname: str, lastname: str="", formal: bool=False):
    """
    Greet the user based on their input NAME, optionally with --lastname.
    
    Use --formal option for formal greeting.
    """
    if formal:
        print(f'Hello, {firstname.title()} {lastname.title()}')
    else:
        print(f'hey {firstname.lower()}')

if __name__ == "__main__":
    typer.run(main)

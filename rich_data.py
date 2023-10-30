# experimenting with  different rich formatting options

import typer

from rich.console import Console
from rich.table import Table
from rich import print
from rich .pretty import pprint

console = Console()


def table():
    #prints a table
    pprint('A Table:')
    table = Table("Name", "Instrument")
    table.add_row("Trane", "Tenor")
    table.add_row("Wynton", "Piano")
    console.print(table)
    print('\n')

def colors():
    pprint('Colors and other styling:')
    print('[red]red[/red]')
    print('[italic yellow]italic yellow[/italic yellow]')
    print('[bold magenta]bold magenta[/bold magenta]')
    print('[bold magenta on cyan]plus cyan background[/bold magenta on cyan]')
    print('[link=https://www.soundcloud.com/solanaasu]link to my scloud[/link]')
    print("emojis: :face_with_open_mouth-emoji: :person_surfing: (list with python -m rich.emoji)")

def main():
    table()
    colors()

if __name__ == "__main__":
    typer.run(main)
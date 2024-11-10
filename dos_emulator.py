import os

def clear():
    os.system('cls' if os.name == 'nt' else 'clear')

def list_commands():
    commands = [
        "dir - wyświetl zawartość katalogu",
        "cls - wyczyść ekran",
        "cd <ścieżka> - zmień katalog",
        "echo <tekst> - wyświetl tekst",
        "type <plik> - wyświetl zawartość pliku",
        "exit - zakończ program",
        "help - wyświetl listę dostępnych komend"
    ]
    print("\nDostępne komendy:")
    for command in commands:
        print(command)
    print()

def cmd_dir():
    for item in os.listdir():
        print(item)

def cmd_cls():
    clear()

def cmd_cd(path):
    try:
        os.chdir(path)
        print("Zmieniono katalog na:", os.getcwd())
    except FileNotFoundError:
        print("Błąd: Katalog nie istnieje")

def cmd_echo(text):
    print(text)

def cmd_type(file_name):
    try:
        with open(file_name, 'r') as file:
            print(file.read())
    except FileNotFoundError:
        print("Błąd: Plik nie istnieje")

def main():
    clear()
    print("Emulator systemu DOS")
    list_commands()

    while True:
        command = input("> ").strip().split()
        if not command:
            continue
        
        cmd = command[0].lower()
        args = command[1:]

        if cmd == "dir":
            cmd_dir()
        elif cmd == "cls":
            cmd_cls()
        elif cmd == "cd" and args:
            cmd_cd(args[0])
        elif cmd == "echo" and args:
            cmd_echo(" ".join(args))
        elif cmd == "type" and args:
            cmd_type(args[0])
        elif cmd == "exit":
            break
        elif cmd == "help":
            list_commands()
        else:
            print("Nieznana komenda. Wpisz 'help', aby zobaczyć listę dostępnych komend.")
            list_commands()

if __name__ == "__main__":
    main()

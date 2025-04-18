import sys
from app.missing_number import MissingNumber

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("Uso: python main_cli.py <número_a_extraer>")
        sys.exit(1)

    try:
        number = int(sys.argv[1])
        mn = MissingNumber()
        mn.extract(number)
        print(f"El número extraído fue: {mn.find_missing()}")
    except ValueError as e:
        print(f"Error: {e}")

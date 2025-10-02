# learning.py
import argparse


def greet(name: str) -> str:
    return f"Hello, {name}!"


def add(a: float, b: float) -> float:
    return a + b


def multiply(a: float, b: float) -> float:
    return a * b


def main():
    parser = argparse.ArgumentParser(description="Tiny practice CLI")
    sub = parser.add_subparsers(dest="command", required=True)

    g = sub.add_parser("greet", help="Greet someone")
    g.add_argument("--name", required=True)

    a = sub.add_parser("add", help="Add two numbers")
    a.add_argument("--a", type=float, required=True)
    a.add_argument("--b", type=float, required=True)

    m = sub.add_parser("multiply", help="Multiply two numbers")
    m.add_argument("--a", type=float, required=True)
    m.add_argument("--b", type=float, required=True)

    args = parser.parse_args()

    if args.command == "greet":
        print(greet(args.name))
    elif args.command == "add":
        print(add(args.a, args.b))
    elif args.command == "multiply":
        print(multiply(args.a, args.b))


if __name__ == "__main__":
    main()

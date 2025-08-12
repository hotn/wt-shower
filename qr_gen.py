import random
import argparse

def generate_hex_string():
    hex_chars = ''.join(random.choices('0123456789abcdef', k=8))
    return f"wt{hex_chars}!"

def main():
    parser = argparse.ArgumentParser(description="Generate hex-tagged strings.")
    parser.add_argument("count", type=int, help="Number of strings to generate")
    args = parser.parse_args()

    for _ in range(args.count):
        print(generate_hex_string())

if __name__ == "__main__":
    main()

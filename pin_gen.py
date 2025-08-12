import random
import argparse

def generate_8_digit_number():
    return random.randint(10_000_000, 99_999_999)

def main():
    parser = argparse.ArgumentParser(description="Generate random 8-digit numbers.")
    parser.add_argument("count", type=int, help="Number of 8-digit numbers to generate")
    args = parser.parse_args()

    for _ in range(args.count):
        print(generate_8_digit_number())

if __name__ == "__main__":
    main()

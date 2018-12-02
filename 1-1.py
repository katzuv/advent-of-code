"""Solution of day 1 part 1."""

if __name__ == '__main__':
    with open('input.txt') as input_file:
        print(sum(int(line) for line in input_file))

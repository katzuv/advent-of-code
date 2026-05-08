import sys

input_example = """123 328  51 64 
 45 64  387 23 
  6 98  215 314
*   +   *   +  """

Problem = tuple[list[int], Callable[[int, int], int]]


def get_problems(input_text: str) -> list[Problem]:
    lines = input_text.splitlines()
    operators = (
        (m.start(), m.end(), m.group().strip())
        for m in re.finditer(r"[+*]\s*", lines[-1])
    )
    lines = lines[:-1]
    return [
        (
            [int(line[start:end]) for line in lines],
            operator.add if operation == "+" else operator.mul,
        )
        for (start, end, operation) in operators
    ]


def get_answer(input_text: str):
    raise NotImplementedError


if __name__ == "__main__":
    puzzle_input = sys.argv[1] if len(sys.argv) > 1 else input_example
    print(get_answer(puzzle_input))

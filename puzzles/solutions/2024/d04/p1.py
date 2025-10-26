import sys


Matrix = list[str]


def get_diagonals(matrix: Matrix) -> Matrix:
    diagonals = []
    rows_number = len(matrix)
    columns_number = len(matrix[0])
    diagonals.extend(
        get_diagonal_by_start_cell(matrix, 0, i, rows_number, columns_number)
        for i in range(columns_number)
    )
    diagonals.extend(
        get_diagonal_by_start_cell(matrix, i, 0, rows_number, columns_number)
        for i in range(1, rows_number)
    )
    return diagonals


def get_diagonal_by_start_cell(
    matrix: Matrix,
    row: int,
    column: int,
    rows_number: int,
    columns_number: int,
):
    diagonal = ""
    while row < rows_number and column < columns_number:
        diagonal += matrix[row][column]
        row += 1
        column += 1
    return diagonal


def get_all_text_sequences(input_text: str) -> Matrix:
    matrix = input_text.splitlines()
    columns = ["".join(row[i] for row in matrix) for i in range(len(matrix[0]))]

    down_right_diagonals = get_diagonals(matrix)
    up_right_diagonals = get_diagonals(matrix[::-1])

    sequences = matrix + columns + down_right_diagonals + up_right_diagonals
    return sequences + [sequence[::-1] for sequence in sequences]


def get_answer(input_text: str) -> int:
    sequences = get_all_text_sequences(input_text)
    return sum(sequence.count("XMAS") for sequence in sequences)


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.

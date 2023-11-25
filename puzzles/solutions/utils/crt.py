def calculate_extended_euclidean_algorithm(
    first_integer: int, second_integer: int
) -> tuple[int, int]:
    previous_remainder = first_integer
    current_remainder = second_integer
    previous_first_coefficient = 1
    current_first_coefficient = 0
    previous_second_coefficient = 0
    current_second_coefficient = 1

    while True:
        quotient = previous_remainder // current_remainder

        current_remainder, previous_remainder = (
            previous_remainder - quotient * current_remainder,
            current_remainder,
        )
        if current_remainder == 0:
            break
        (
            current_first_coefficient,
            previous_first_coefficient,
        ) = (
            previous_first_coefficient - quotient * current_first_coefficient,
            current_first_coefficient,
        )
        (
            current_second_coefficient,
            previous_second_coefficient,
        ) = (
            previous_second_coefficient - quotient * current_second_coefficient,
            current_second_coefficient,
        )

    return current_first_coefficient, current_second_coefficient

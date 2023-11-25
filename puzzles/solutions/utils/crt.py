import functools
import operator


def calculate_chinese_remainder_theorem(modulo_to_remainder: dict[int, int]) -> int:
    total_product = functools.reduce(operator.mul, modulo_to_remainder)
    modulo_to_partial_product = {
        modulo: total_product // modulo for modulo in modulo_to_remainder
    }
    modulo_to_inverse = {
        modulo: calculate_extended_euclidean_algorithm(
            modulo_to_partial_product[modulo], modulo
        )[0]
        for modulo in modulo_to_remainder
    }

    result = sum(
        modulo_to_remainder[modulo]
        * modulo_to_partial_product[modulo]
        * modulo_to_inverse[modulo]
        for modulo in modulo_to_remainder
    )
    return result % total_product


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

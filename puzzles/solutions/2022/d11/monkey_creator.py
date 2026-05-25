from typing import Sequence, Callable
import re
import operator

from monkey import Monkey


_FIRST_PARAMETER = "first_parameter"
_OPERATOR = "operator"
_SECOND_PARAMETER = "second_parameter"
_OLD = "old"
PLUS_SIGN = "+"


def create_monkey(monkey_attributes: Sequence[str]) -> Monkey:
    """
    :param monkey_attributes: list of lines containing the monkey attributes
    :return: monkey created from the attributes
    """
    starting_items_match = re.findall(r"\b\d+\b", monkey_attributes[0])
    starting_items = list(int(item) for item in starting_items_match)

    worry_function = _get_worry_function(monkey_attributes[1])

    test_divisor_match = re.search(r"\d+", monkey_attributes[2])
    test_divisor = int(test_divisor_match.group())

    true_test_result_monkey_number_match = re.search(r"\d+", monkey_attributes[3])
    true_test_result_monkey_number = int(true_test_result_monkey_number_match.group())

    false_test_result_monkey_number_match = re.search(r"\d+", monkey_attributes[4])
    false_test_result_monkey_number = int(false_test_result_monkey_number_match.group())

    return Monkey(
        starting_items,
        worry_function,
        test_divisor,
        true_test_result_monkey_number,
        false_test_result_monkey_number,
    )


def _get_worry_function(
    line: str,
) -> Callable[[int], int]:
    """
    :param line: line from the input containing the worry level function
    :return: function calculating the new worry level based on the old level
    """
    parameters = re.search(
        rf"(?P<{_FIRST_PARAMETER}>\d+|{_OLD}) (?P<{_OPERATOR}>[*+]) (?P<{_SECOND_PARAMETER}>\d+|{_OLD})",
        line,
    ).groupdict()

    first_parameter = parameters[_FIRST_PARAMETER]
    operator_function = (
        operator.add if parameters[_OPERATOR] == PLUS_SIGN else operator.mul
    )
    second_parameter = parameters[_SECOND_PARAMETER]

    if first_parameter == _OLD:
        if second_parameter == _OLD:
            return lambda old: operator_function(old, old)
        second_parameter = int(second_parameter)
        return lambda old: operator_function(old, second_parameter)
    first_parameter = int(first_parameter)
    if second_parameter == _OLD:
        return lambda old: operator_function(first_parameter, old)

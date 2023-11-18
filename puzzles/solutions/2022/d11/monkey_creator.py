from typing import Callable
import re
import operator


_FIRST_PARAMETER = "first_parameter"
_OPERATOR = "operator"
_SECOND_PARAMETER = "second_parameter"
_OLD = "old"
PLUS_SIGN = "+"


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

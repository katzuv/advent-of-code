def mass_needed_for_mass(mass: int) -> int:
    """
    :param mass: mass to calculate the needed fuel for
    :return: needed amount of fuel to carry the given mass
    """
    return max(0, (mass // 3) - 2)


if __name__ == '__main__':
    with open('../inputs/1.txt') as input_file:
        print(f'Answer for part 1: {sum((mass_needed_for_mass(int(module))) for module in input_file)}')

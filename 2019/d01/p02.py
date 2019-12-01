import p01


def mass_needed_for_mass_recursive(mass: int) -> int:
    """
    :param mass: mass to calculate the needed fuel for
    :return: needed amount of fuel to carry the given mass, taking into account the mass of the added fuel to carry fuel
    """
    if mass < 1:
        return 0
    mass_needed = p01.mass_needed_for_mass(mass)
    return mass_needed + mass_needed_for_mass_recursive(mass_needed)


if __name__ == '__main__':
    with open('../inputs/1.txt') as input_file:
        print(f'Answer for part 2: {sum((mass_needed_for_mass_recursive(int(module))) for module in input_file)}')

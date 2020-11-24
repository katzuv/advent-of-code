from p1 import OrbitCountChecksumCalculator, get_orbits_from_input


def main():
    orbits = get_orbits_from_input()

    calc = OrbitCountChecksumCalculator(orbits)
    you_orbiting = calc.get_node('YOU').parent
    san_orbiting = calc.get_node('SAN').parent

    for ancestor in reversed(you_orbiting.ancestors):
        if ancestor in san_orbiting.ancestors:
            mutual_ancestor = ancestor
            break

    you_mutual_distance = you_orbiting.depth - mutual_ancestor.depth
    san_mutual_distance = san_orbiting.depth - mutual_ancestor.depth
    if you_orbiting in san_orbiting.descendants or san_orbiting in you_orbiting.descendants:
        orbital_transfers = abs(you_mutual_distance - san_mutual_distance)
    else:
        orbital_transfers = you_mutual_distance + san_mutual_distance
    print(f'Orbital transfers needed: {orbital_transfers}')


if __name__ == '__main__':
    main()

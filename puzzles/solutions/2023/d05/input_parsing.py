import re


Mapping = list[tuple[int, int, int]]


def get_map_ranges(lines: list[str]) -> Mapping:
    ranges = []
    for line in lines:
        destination_range_start, source_range_start, range_length = map(
            int, line.split()
        )
        difference = destination_range_start - source_range_start
        source_range_end = source_range_start + range_length
        ranges.append((source_range_start, source_range_end, difference))
    return ranges


def get_category_mapping(mapping: str) -> tuple[str, Mapping]:
    lines = mapping.splitlines()
    source = re.match(r"([a-z]+)", lines[0]).group()
    ranges = get_map_ranges(lines[1:])
    return source, ranges


def get_all_mappings(mapping_lines: str) -> dict[str, Mapping]:
    source_to_destination_categories_ranges = {}
    for mapping in mapping_lines.split("\n\n"):
        source, ranges = get_category_mapping(mapping)
        source_to_destination_categories_ranges[source] = ranges
    return source_to_destination_categories_ranges


def get_initial_data(
    input_text: str,
) -> tuple[list[int], dict[str, Mapping]]:
    first_line, mapping_lines = input_text.split("\n\n", maxsplit=1)
    initial_seeds = [int(number) for number in re.findall(r"\d+", first_line)]
    mappings = get_all_mappings(mapping_lines)
    return initial_seeds, mappings

import sys

import consts
import p1


def get_answer(input_text: str):
    """Return total size of the smallest directory that, if deleted, would free up enough space on the filesystem."""
    filesystem = p1.get_filesystem(input_text)
    root = filesystem[0]
    total_used_space = root.size
    unused_space_needed = consts.REQUIRED_UNUSED_SPACE - (
        consts.TOTAL_DISK_SPACE - total_used_space
    )
    candidate_directories = (
        directory for directory in filesystem if directory.size >= unused_space_needed
    )
    directory_to_delete = min(
        candidate_directories, key=lambda directory: directory.size
    )
    return directory_to_delete.size


if __name__ == "__main__":
    try:
        print(get_answer(sys.argv[1]))
    except IndexError:
        pass  # Don't crash if no input was passed through command line arguments.

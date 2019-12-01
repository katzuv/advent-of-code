import itertools
from typing import List, Dict, Set

from p1 import couples_from_file, steps_to_their_dependencies

NUMBER_OF_WORKERS = 5


class Worker:
    """Class representing a worker."""

    def __init__(self, number: int):
        self.number = number
        self.current_step = '.'
        self.time_remaining = 0

    @property
    def is_available(self):
        """
        :return: whether the worker is available for another step
        """
        return self.time_remaining == 0


def next_available_steps(steps_to_dependencies: Dict[str, List[str]], completed_steps: Set[str],
                         current_steps: Set[str]) -> Set[str]:
    """
    :param steps_to_dependencies: mapping of (step: its dependencies)
    :param completed_steps: the steps which have been already completed
    :param current_steps: the steps which are now being worked on
    :return: all the possible next steps
    """
    return {step for step in steps_to_dependencies if
            set(steps_to_dependencies[step]) <= completed_steps} - current_steps - completed_steps


def step_duration(step: str) -> int:
    """
    :param step: the step to calculate its duration
    :return: the number of seconds needed to complete the given step
    """
    return ord(step) - 4


def main():
    steps_to_dependencies = steps_to_their_dependencies(couples_from_file())
    workers = {Worker(number) for number in range(NUMBER_OF_WORKERS)}
    current_steps = set()
    completed_steps = set()
    completed_steps_list = list()
    print(f'Second    {"   ".join(f"worker {number}" for number in range(NUMBER_OF_WORKERS))}     Done')
    for second in itertools.count():
        for worker in workers:
            if not worker.is_available:
                worker.time_remaining -= 1
            if worker.is_available:
                if worker.current_step.isalpha():
                    completed_steps.add(worker.current_step)
                    completed_steps_list.append(worker.current_step)
                    current_steps.remove(worker.current_step)
                worker.current_step = '.'
        available_steps = next_available_steps(steps_to_dependencies, completed_steps, current_steps)
        for worker in workers:
            if available_steps:
                if worker.is_available:
                    assigned_step = min(available_steps)
                    available_steps.remove(assigned_step)
                    worker.current_step = assigned_step
                    worker.time_remaining = step_duration(assigned_step)
                    current_steps.add(assigned_step)
        print(f'{second}{" " * 12}{(" " * 10).join(worker.current_step for worker in workers)}      {"".join(step for step in completed_steps_list)}')
        if len(completed_steps) == len(steps_to_dependencies):
            print(f'Total time:')
            break


if __name__ == '__main__':
    main()

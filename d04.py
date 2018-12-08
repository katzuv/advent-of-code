import re
import statistics
from collections import Counter
from datetime import datetime
from typing import List, Tuple, Dict


class Guard:
    """Class representing a guard guarding the supply closet."""

    def __init__(self, number: int):
        """
        Instantiate a guard.
        :param number: ID of the guard
        """
        self.number = number
        self.total_sleep_time = 0
        self.minutes_slept = []


def guards_to_sleep_intervals(records: List[Tuple[datetime, str]]) -> Dict[int, Guard]:
    """
    Return mapping from guard IDs to guards' total sleep times and every minute they were asleep in.
    :param records: records of events
    :return: guards' sleeping and shift changing info
    """
    guards_to_time = {}
    for i, (time, event) in enumerate(records):
        if '#' in event:
            guard_id = int(re.match(r'Guard #(\d+) begins shift', event).groups()[0])
            if guard_id not in guards_to_time:
                guards_to_time[guard_id] = Guard(guard_id)
        elif event.startswith('falls asleep'):
            time_falls_asleep = time
            time_wakes_up = records[i + 1][0]
            time_asleep = time_wakes_up - time_falls_asleep
            guards_to_time[guard_id].total_sleep_time += time_asleep.total_seconds() // 60
            guards_to_time[guard_id].minutes_slept.extend(range(time_falls_asleep.minute, time_wakes_up.minute))

    return guards_to_time


def best_guard_minute_combination1(guards_to_sleep: Dict[int, Guard]) -> int:
    """
    Return best guard/minute combination by finding the guard that has the most minutes asleep.
    :param guards_to_sleep: guards' sleeping and shift changing info
    :return: best guard/minute combination by most sleepy guard in total
    """
    most_sleepy_guard = max(guards_to_sleep.items(), key=lambda guard: guard[1].total_sleep_time)[1]
    return most_sleepy_guard.number * statistics.mode(most_sleepy_guard.minutes_slept)


def best_guard_minute_combination2(guards_to_sleep: Dict[int, Guard]) -> int:
    """
    Return best guard/minute combination by finding the guard who is most frequently asleep on the same minute.
    :param guards_to_sleep: guards' sleeping and shift changing info
    :return: best guard/minute combination by most sleepy guard on the same minute
    """
    most_sleepy_guard = max(guards_to_sleep.items(),
                            key=lambda guard: amount_of_most_common_item_only_one(guard[1].minutes_slept))[1]
    return most_sleepy_guard.number * statistics.mode(most_sleepy_guard.minutes_slept)


def amount_of_most_common_item_only_one(numbers: List[int]) -> int:
    """
    Return amount of most common integer in a list, 0 if there is more than one most common item.
    :param numbers: list to check
    :return: most common integer in a list, 0 if there is more than one most common item
    """
    try:
        return Counter(numbers).most_common(1)[0][1]
    except IndexError:
        return 0


def sort_records(records: List[str]) -> List[Tuple[datetime, str]]:
    """
    Sort list of records of guard shifts
    :param records:
    :return:
    """
    dates_to_events = {}
    for record in records:
        date = date_from_record(record)
        dates_to_events[date] = record[19:].strip()
    return sorted(dates_to_events.items(), key=lambda x: x[0])


def date_from_record(record: str) -> datetime:
    """
    Extract date and time from record.
    :param record: record holding date and event
    :return: extracted date and time
    """
    date = record[1:17]
    date = datetime.strptime(date, '%Y-%m-%d %H:%M')
    return date


def main():
    with open('inputs\\4.txt') as file:
        records = sort_records(file.readlines())
        intervals = guards_to_sleep_intervals(records)
        print(best_guard_minute_combination1(intervals))
        print(best_guard_minute_combination2(intervals))


if __name__ == '__main__':
    main()

"""
Advent of Code 2020, Day 2
Password Philosophy
https://adventofcode.com/2020/day/2
"""

from collections.abc import Callable
import re
from os import path
from typing import NamedTuple

INPUT_FILE = "input.txt"
TEST_FILE = "test.txt"


ENTRY_REGEX = re.compile(r"(\d+)-(\d+) (\w): (\w+)")


class Policy(NamedTuple):
    """Represents a policy that a password must adhere to."""

    character: str
    parameter1: int
    parameter2: int


class Entry(NamedTuple):
    """Represents a password entry."""

    password: str
    policy: Policy


def read_password_entries(file_path: str) -> list[Entry]:
    """Read passwords and their respective policies from a file."""

    with open(file_path, encoding="utf-8") as file:
        return [parse_entry(line.strip()) for line in file]


def parse_entry(entry: str) -> Entry:
    """Parse a password entry from a string."""

    pattern_match = ENTRY_REGEX.match(entry)
    if not pattern_match:
        raise ValueError(f"Invalid entry: {entry}")
    
    min_occurrences = int(pattern_match.group(1))
    max_occurrences = int(pattern_match.group(2))
    character = pattern_match.group(3)
    password = pattern_match.group(4)

    policy = Policy(character, min_occurrences, max_occurrences)

    return Entry(password, policy)


def policy_character_count_within_bounds(entry: Entry) -> bool:
    """Check if a password contains the required number of occurrences of a character."""

    password, (character, min_occurrences, max_occurrences) = entry

    character_count = password.count(character)

    return min_occurrences <= character_count <= max_occurrences


def policy_character_at_one_of_two_positions(entry: Entry) -> bool:
    """Check if a password contains the required character at only one of the specified positions."""

    password, (character, position1, position2) = entry

    # NOTE: The positions that the new policies use are 1-based, not 0-based like normal indices.
    character_at_position1 = password[position1 - 1] == character
    character_at_position2 = password[position2 - 1] == character

    character_present = character_at_position1 or character_at_position2
    character_not_at_both = character_at_position1 != character_at_position2

    return character_present and character_not_at_both


def count_valid_entries(entries: list[Entry], validate: Callable[[Entry], bool]) -> int:
    """Count the number of passwords that satisfy their respective policies."""

    return sum(validate(entry) for entry in entries)


def main() -> None:
    """Read policies and passwords from a file and process them."""

    input_file = INPUT_FILE
    file_path = path.join(path.dirname(__file__), input_file)

    entries = read_password_entries(file_path)
    print(entries)

    valid_entries_count_with_old_policy_rules = count_valid_entries(entries, policy_character_count_within_bounds)
    print(f"Number of valid entries using old policy rules: {valid_entries_count_with_old_policy_rules}")

    valid_entries_count_with_new_policy_rules = count_valid_entries(entries, policy_character_at_one_of_two_positions)
    print(f"Number of valid entries using new policy rules: {valid_entries_count_with_new_policy_rules}")


if __name__ == "__main__":
    main()
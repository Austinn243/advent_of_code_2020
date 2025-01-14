"""
Advent of Code 2020, Day 1
Report Repair
https://adventofcode.com/2020/day/1
"""

from os import path
from typing import Optional

INPUT_FILE = "input.txt"
TEST_FILE = "test.txt"

TARGET_SUM = 2020

def read_expenses(file_path: str) -> list[int]:
    """Read expenses from a file."""

    with open(file_path, encoding="utf-8") as file:
        return [int(line.strip()) for line in file]


def find_two_expenses_with_sum(expenses: list[int], target_sum: int) -> Optional[tuple[int, int]]:
    """Find the two expenses that sum to the target sum."""

    index_map = {expense: index for index, expense in enumerate(expenses)}

    for i, expense in enumerate(expenses):
        complement = target_sum - expense
        if complement in index_map and index_map[complement] != i:
            return expense, complement
        
    return None


def find_three_expenses_with_sum(expenses: list[int], target_sum: int) -> Optional[tuple[int, int, int]]:
    """Find the three expenses that sum to the target sum."""

    for i, expense1 in enumerate(expenses):
        remaining_sum = target_sum - expense1
        remaining_expenses = expenses[:i] + expenses[i + 1:]

        two_expenses_with_remaining_sum = find_two_expenses_with_sum(remaining_expenses, remaining_sum)
        if not two_expenses_with_remaining_sum:
            continue

        expense2, expense3 = two_expenses_with_remaining_sum
        return expense1, expense2, expense3
        
    return None


def main() -> None:
    """Read expenses from a file and process them."""

    input_file = INPUT_FILE
    file_path = path.join(path.dirname(__file__), input_file)

    expenses = read_expenses(file_path)
    print(expenses)

    two_expenses_with_target_sum = find_two_expenses_with_sum(expenses, TARGET_SUM)
    if not two_expenses_with_target_sum:
        print("No two expenses found that sum to the target sum.")
        return
    
    expense1, expense2 = two_expenses_with_target_sum
    print(f"Expenses: {expense1}, {expense2}")
    print(f"Product: {expense1 * expense2}")

    three_expenses_with_target_sum = find_three_expenses_with_sum(expenses, TARGET_SUM)
    if not three_expenses_with_target_sum:
        print("No three expenses found that sum to the target sum.")
        return
    
    expense1, expense2, expense3 = three_expenses_with_target_sum
    print(f"Expenses: {expense1}, {expense2}, {expense3}")
    print(f"Product: {expense1 * expense2 * expense3}")


if __name__ == "__main__":
    main()
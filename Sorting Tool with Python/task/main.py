from typing import List

def max_number(lst: List[int]) -> List[int]:
    maximum = max(lst)
    counter = numbers.count(maximum)
    return [maximum, counter]

numbers = []

while True:
    try:
        data = input()
        numbers.extend(map(int, data.split()))
    except EOFError:
        break

print("Total numbers:",len(numbers))
max_num,count_max = max_number(numbers)
print(f"The greatest number: {max_num} ({count_max} time{"s"[:count_max ^ 1]})")
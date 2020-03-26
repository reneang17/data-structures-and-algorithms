"""
Read file into texts and calls.
It's ok if you don't understand how to read files.
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)


"""
TASK 1:
How many different telephone numbers are there in the records?
Print a message:
"There are <count> different telephone numbers in the records."
"""


def numbers(file):
    nums = set()
    for entry in file:
        nums.add(entry[0])
        nums.add(entry[1])
    return nums


if __name__ == '__main__':
    tel_numbers = numbers(texts).union(numbers(calls))
    print("There are {} different telephone numbers in the records.".format(len(tel_numbers)))

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
TASK 4:
The telephone company want to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers:
these are numbers that make outgoing calls but never send texts,
receive texts or receive incoming calls.

Print a message:
"These numbers could be telemarketers: "
<list of numbers>
The list of numbers should be print out one per line in lexicographic order with no duplicates.
"""

def identify_telemarkers(calls, texts):
    """
    calls:list
    texts:list
    Returns:
    numbers: list, possible telemarkers
    """
    dialer = []
    dialed = []
    for call in calls:
        dialer.append(call[0])
        dialed.append(call[1])

    texter = []
    texted = []
    for text in texts:
        texter.append(text[0])
        texted.append(text[1])

    no_telemarketers = set(dialed+texter+texted)
    dialer = set(dialer)

    telemarketers = {n for n in dialer if n not in no_telemarketers}
    return  sorted(list(telemarketers))



if __name__ == '__main__':

    telemarkers = identify_telemarkers(calls, texts)
    print(f"Potential telemarketers:")
    for n in telemarkers:
        print(n)

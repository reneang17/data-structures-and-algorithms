"""
Read file into texts and calls.
It's ok if you don't understand how to read files
"""
import csv
with open('texts.csv', 'r') as f:
    reader = csv.reader(f)
    texts = list(reader)

with open('calls.csv', 'r') as f:
    reader = csv.reader(f)
    calls = list(reader)

"""
TASK 2: Which telephone number spent the longest time on the phone
during the period? Don't forget that time spent answering a call is
also time spent on the phone.
Print a message:
"<telephone number> spent the longest time, <total time> seconds, on the phone during
September 2016.".
"""

def phone_time(calls):
    n_dict = {}
    for call in calls:
        n1, n2 = call[0], call[1]
        time = int(call[-1])


        if n1 in n_dict:
            n_dict[n1] += time
        else:
            n_dict[n1] = time

        if n2 in n_dict:
            n_dict[n2] += time
        else:
            n_dict[n2] = time

    return n_dict


if __name__ == '__main__':
    n_dict = phone_time(calls)
    phone= max(n_dict, key=n_dict.get)
    time = n_dict[phone]
    print(f"{phone} spent the longest time, {time} seconds, on the phone during September 2016.")

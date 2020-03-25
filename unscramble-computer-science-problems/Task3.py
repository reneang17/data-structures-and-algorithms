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
TASK 3:
(080) is the area code for fixed line telephones in Bangalore.
Fixed line numbers include parentheses, so Bangalore numbers
have the form (080)xxxxxxx.)

Part A: Find all of the area codes and mobile prefixes called by people
in Bangalore.
 - Fixed lines start with an area code enclosed in brackets. The area
   codes vary in length but always begin with 0.
 - Mobile numbers have no parentheses, but have a space in the middle
   of the number to help readability. The prefix of a mobile number
   is its first four digits, and they always start with 7, 8 or 9.
 - Telemarketers' numbers have no parentheses or space, but they start
   with the area code 140.

Print the answer as part of a message:
"The numbers called by people in Bangalore have codes:"
 <list of codes>
The list of codes should be print out one per line in lexicographic order with no duplicates.

Part B: What percentage of calls from fixed lines in Bangalore are made
to fixed lines also in Bangalore? In other words, of all the calls made
from a number starting with "(080)", what percentage of these calls
were made to a number also starting with "(080)"?

Print the answer as a part of a message::
"<percentage> percent of calls from fixed lines in Bangalore are calls
to other fixed lines in Bangalore."
The percentage should have 2 decimal digits
"""

def from_bangalore(calls):
    """
    calls: list
    Returns
    codes : list of codes of numbers called from fix lane bangalore
    from_b : number of call found from Bangalore
    to_b: number of calls from bangalore to bangalore
    """
    codes = []
    from_b = 0 # counter of calls from bangalore
    to_b = 0 # counter of call from bangalore to bangalore

    for call in calls:
        dialer =call[0][0:5]
        if dialer == '(080)':
            from_b+=1
            dialed= call[1]
            # Fix land case
            if dialed[:2] == '(0':
                codes.append(dialed.split(sep=')')[0] + ')')
                to_b+=1
            # If Telemarketer
            elif dialed[:3] == '140':
                codes.append(dialed[:3])
            # If Mobile
            elif len(dialed.split())==2 and \
            dialed[0].isdigit()  and int(dialed[0]) in [7,8,9]:
                codes.append(dialed[:4])
            # Rise exception ow
            else:
                assert False, 'Another type of number was found:{}'.format(dialed)
    # get rid fo duplicates and
    codes = list(set(codes))
    #order  lexicographically in line
    codes.sort()
    return codes, from_b, to_b





if __name__ == '__main__':

    codes , calls_from_b, calls_to_b = from_bangalore(calls)
    percentage = (100.0 * calls_to_b) / calls_from_b
    "The numbers called by people in Bangalore have codes:"
    for code in codes:
        print(code)

    print("""{:2.2f} percent of calls from fixed lines in Bangalore are calls
    to other fixed lines in Bangalore.""".format(percentage))

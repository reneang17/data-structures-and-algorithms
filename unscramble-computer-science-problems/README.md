Big O Unscramble Computer Science Problems
================

## Task 0
What is the first record of texts and what is the last record of calls?
Looking at list elements

Big O: \(O(1)\)


## Task 1

How many different telephone numbers are there in the records?
Loop through call/text

Here and below n = number-of-calls plus number-of- text is at worst.

Big O notation: \(O(n  log(n))\)
  - Make a list of phones with repetitions  \(O(n)\)
  - Sorting them to find uniques.\(O(n  log(n))\)

## Task 2

Which telephone number spent the longest time on the phone during the
period?

``` python
def max_phone_time(calls):

    for call in calls:
        n1, n2 = call[0], call[1]
        time = call[3]
        n_dict = {}

        if n1 in n_dict:
            n_dict[n1] += time
        else:
            n_dict[n1] = time

        if n2 in n_dict:
            n_dict[n2] += time
        else:
            n_dict[n2] = time

        key= max(n_dict, key=n_dict.get)
        return key, n_dict[key]
```
Big O notation: \( O(n!)\)

The first loop and hashing is at worst \( O(n!)\), if all numbers
are different. Then the max is at worst O(m), where m is the dictionary length.

## Task 3

```python

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
        if

    # get rid fo duplicates and
    codes = list(set(codes))
    #order  lexicographically in line
    codes.sort()
    return codes, from_b, to_b

```

Big O notation: \(O(n) + O(m * log(m))\)

  - Looping \(O(n)

  - Sorting over bangalore is \(O(m * log(m))\)

## Task 4

The telephone company wants to identify numbers that might be doing
telephone marketing. Create a set of possible telemarketers: these are
numbers that make outgoing calls but never send texts, receive texts or
receive incoming calls.

``` python
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
```

Big O notation: \(n^2\)

  - Looping to form a list \(O(n)\)

  - set(list) is at worst: \(O(n^2)\)

  - Sorting a list : \(O(n* log(n))\)

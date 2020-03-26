Big O Unscramble Computer Science Problems
================

## Task 0
What is the first record of texts and what is the last record of calls?
Looking at list elements


Worst time complexity (Big O) equal to \(O(1)\). Justification:

Because we are not iterating the elements from input lists (calls or texts). We are accessing the first and last value of an array by an index.

## Task 1

How many different telephone numbers are there in the records?
Loop through call/text

Hereafter, n = number-of-calls plus number-of- text at worst.

``` python
def numbers(file):
    nums = set()
    for entry in file:
        nums.add(entry[0])
        nums.add(entry[1])
    return nums


tel_numbers = numbers(texts).union(numbers(calls))
print("There are {} different telephone numbers in the records.".format(len(tel_numbers)))
```

Worst time complexity (Big O) equal to \(O(n^2)\). Justification:

Inside the function:
  - Looping O(n)
  - For each loop iteration, adding an element is at worst \(O(n)\), or
   if adding an element is optimized with a search algorithm.
   
Outside of the function:
  - Union of sets is at worst \(O(n)\).
  - Taking length \(O(1)\).

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

n_dict = phone_time(calls)
phone= max(n_dict, key=n_dict.get)
time = n_dict[phone]
```
Worst time complexity (Big O) equal to  \(O(n^3)\). Justification:

Function Big O:

- The loop is at worst of time complexity \(O(n)\).
- For each loop iteration, ```n in n_dict``` has at worst time worst time complexity  \(O(n)\). To see this notice, that search has to occur at every element. [Reference](https://wiki.python.org/moin/TimeComplexity),
shows ```i in dict```, the most similar case, has indeed big O equal to \(O(n)\).
- For each loop iteration and if,  getting a dictionary value has also big O equal to \(O(n)\).
So the function has big O equal to \(O(n^3)\).

After the function statements:

- Then the max is an operation big O equal to O(n).
- Get dictionary item has big O equal to O(n).


## Task 3

``` python

def from_bangalore(calls):
    """
    calls: list
    Returns
    codes : list of codes of numbers called from fix lane bangalore
    from_b : number of call found from Bangalore
    to_b: number of calls from bangalore to bangalore
    """
    codes = set()
    from_b = 0 # counter of calls from bangalore
    to_b = 0 # counter of call from bangalore to bangalore

    for call in calls:
        dialer =call[0][0:5]
        if dialer == '(080)':
            from_b+=1
            dialed= call[1]
            # Fix land case
            if dialed[:2] == '(0':
                codes.add(dialed.split(sep=')')[0] + ')')
                if dialed[:5] == '(080)':
                    to_b+=1
            # If Telemarketer
            elif dialed[:3] == '140':
                codes.add(dialed[:3])
            # If Mobile
            elif len(dialed.split())==2 and \
            dialed[0].isdigit()  and int(dialed[0]) in [7,8,9]:
                codes.add(dialed[:4])
            # Rise exception ow
            else:
                assert False, 'Another type of number was found:{}'.format(dialed)

    codes = list(codes)
    #order  lexicographically in line
    codes.sort()
    return codes, from_b, to_b

```

Worst time complexity (Big O) equal to \(O(n^2 )\). Justification:

Function has big(O) = O(n log(n)). Justification:
  - Outer loop \(O(n)\)
  - For each loop iteration, adding element to a set, checking each element has worst time complexity \(O(n)\)
  - Sort() list is at worst \(O(n * log(n))\)

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
    dialer = set()
    dialed = set()
    for call in calls:
        dialer.add(call[0])
        dialed.add(call[1])

    texter = set()
    texted = set()
    for text in texts:
        texter.add(text[0])
        texted.add(text[1])

    no_telemarketers = dialed.union(texter).union(texted)

    telemarketers = {n for n in dialer if n not in no_telemarketers}
    return  sorted(list(telemarketers))
```


Worst time complexity (Big O) equal to O\(n^2\). Justification:

Inside the function the Big O is \(O(n  log(n))\):

  - Loop yields \(O(n)\)
  - For each loop iteration, Adding  elements to a set yields \(O(n)\)
  - Union of sets yields \(O(n)\)
  - Making set comprehension with if has Big O equal \(O(log(n))\)
  - Sorting a list : \(O(n* log(n))\)

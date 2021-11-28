import pandas as pd
import numpy as np

# The first 1 million composites. source: http://www.naturalnumbers.org/composites.html

composites = list(pd.read_csv('c-1000000.csv', dtype=int)['composite'])

def get_d(n):
    d = n - 1
    while d % 2 == 0:
        d //= 2
    return d

# Miller-Rabin test
def MR_test(n, d, witness):
    if n==2:
        return False
    x = pow(witness, d, n)
    if(x == 1 or x == n-1 or x == -1):
        return True
    return False

false_witnesses = {} # to keep track of who lied how many times
from_index = 0
range_size = 50000
to_index = from_index + range_size # so to not run over the entire 1 million composites. this would take too long

prev = -1 # for printing the progress
for i, composite in enumerate(composites[from_index:to_index]):
    percent = 100 * round(i / range_size, 2) # for printing the progress
    if(percent % 1 == 0 and percent != prev):
        print('{}% done ({} is being tested now)'.format(percent, composite))
        prev = percent
    
    d = get_d(composite) # the power to be used in the MR test
    for witness in range(2, composite): # investigate each possible witness for the current composite
        test_pass = MR_test(composite, d, witness)
        if(test_pass): # Witness claims that the composie is a prime! False witness!
            if(witness in false_witnesses): # have we registered this false witness before? if so- add one to their charges.
                false_witnesses[witness] += 1
            else: # if this is the first time the witness is caught lying, register it.
                false_witnesses[witness] = 1

import operator
# sort by descending value [i.e. the amount of time each number lied]
sorted_d = dict(sorted(false_witnesses.items(),
                       key=operator.itemgetter(1),reverse=True))

list(sorted_d.items())[:10] # print the 10 most liars

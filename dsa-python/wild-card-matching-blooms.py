"""
Given that "*" can be 0 or 1. Given a binary sring, generate all possible outcomes of the binary string if it conntains a "*"

EXAMPLE

Input: s = "1*1"

Output: ["101","111"]
res = [[101],[111]]

                                                  |
                                    /            10**        \    
                                    |            /   \       |
                                    10*0       100*   101*   10*1-----------
                                 /    \         / \     /\                 |
                               1000   1010  1000  1001 1010  1011        1001 1011


This algorithm runs in O(2n) time where n is equal to the number of wildcards because there are 2n possible sets for all wildcards in the string. The algorithm must perform this many steps to calculate all the sets. [1] If there are no wildcards in the string, 
then the algorithm runs in linear time, O(n), because it will simply append each character to a string.
"""
from copy import deepcopy


def patterns(str):
    output = [[]]
    if not str:
        return output
    for c in str:
        if c == '0' or c == '1':
            for i in range(len(output)):
                output[i] .append(c)
        elif c == '*':
            old_len = len(output)
            output += deepcopy(output)
            for i in range(old_len):
                output[i].append('0')
            for i in range(old_len, len(output)):
                output[i].append('1')
    return ["".join(lst) for lst in output]


s = "100*11**1"
# print(patterns(s))

wild = ['jacob', 'johncena', 'dright', 'low']
wild.sort(key=len)


print(wild)

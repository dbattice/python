# -*- coding: utf-8 -*-
"""
Created on Tue Feb 25 19:32:38 2020

@author: Devin
"""

'Algorithms'
'sorting'
def merge_sort(m):
    ' Base case. A list of zero or one elements is sorted, by definition.'
    if len(m) <= 1:
        return m

    ''' Recursive case. First, divide the list into equal-sized sublists
    consisting of the first half and second half of the list.
    This assumes lists start at index 0.'''
    left=[]
    right=[]
    for x in range(len(m)):
        if x < (len(m))/2:
            left.append(m[x])
        else:
            right.append(m[x])

    'Recursively sort both sublists.'
    left=merge_sort(left)
    right=merge_sort(right)

    'Then merge the now-sorted sublists.'
    return merge(left, right)

def merge(left, right):
    result=[]

    while (left  and right):
        if (left[0] <= right[0]):
            result.append(left[0])
            left =left[1:]
        else:
            result.append(right[0])
            right=right[1:]
            

    ''' Either left or right may have elements left; consume them.
     (Only one of the following loops will actually be entered.)'''
    while left :
        result.append(left[0])
        left=left[1:]
    while right:
        result.append(right[0])
        right=right[1:]
    return result
a=[5,7,4,3,6,10,1,0,8,9]
print(merge_sort(a))
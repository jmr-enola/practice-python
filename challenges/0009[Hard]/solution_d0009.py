'''
Given a list of integers, write a function that returns the largest sum of non-adjacent numbers. Numbers can be 0 or negative.

For example, [2, 4, 6, 2, 5] should return 13, since we pick 2, 6, and 5. [5, 1, 1, 5] should return 10, since we pick 5 and 5.

Follow-up: Can you do this in O(N) time and constant space?
'''

def solution01(arr: list) -> int:
    
    index = 0
    sum = arr[0]

    while index < len(arr) - 2:

        if (index + 3 < len(arr)):
            if (arr[index + 3] > arr[index + 2]):
                sum += arr[index + 3]
                index += 3
                continue

        sum += arr[index + 2]
        index += 2

    index = 1
    sum2 = arr[1]

    while index < len(arr) - 2:

        if (index + 3 < len(arr)):
            if (arr[index + 3] > arr[index + 2]):
                sum2 += arr[index + 3]
                index += 3
                continue

        sum2 += arr[index + 2]
        index += 2
    
    return sum if sum >= sum2 else sum2
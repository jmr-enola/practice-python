'''
Given an array of integers, find the first missing positive integer in linear time and constant space. In other words, find the lowest positive integer that does not exist in the array. The array can contain duplicates and negative numbers as well.

For example, the input [3, 4, -1, 1] should give 2. The input [1, 2, 0] should give 3.

You can modify the input array in-place.
'''

def solution01(arr: list) -> int:
    size = len(arr)

    #Sort from lowest to highest
    for i in range(size):
        while (1 <= arr[i] <= size and arr[arr[i] - 1] != arr[i]):
            arr[arr[i] - 1], arr[i] = arr[i], arr[arr[i] - 1]

    #Check if each element is in their correct position
    for i in range(size):
        if (arr[i] != i + 1):
            return i + 1

    return size + 1
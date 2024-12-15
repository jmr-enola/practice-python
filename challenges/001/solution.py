'''
Given a list of numbers and a number k, return whether any two numbers from the list add up to k.
For example, given [10, 15, 3, 7] and k of 17, return true since 10 + 7 is 17.
'''

def solution01 (k: int, arr: list) -> bool:
    #O(n^2) 
    for i in range(len(arr)):
        for j in range(i, len(arr)):
            if (i != j and arr[i] + arr[j] == k):
                return True

    return False

def solution02 (k: int, arr: list) -> bool:
    #O(nlogn)
    #sort from lowest to highest
    sorted_arr = sorted(arr)
    
    pointer1 = len(sorted_arr)//2
    pointer2 = pointer1//2

    #O(n/2)
    while (pointer2 < pointer1):
        if (sorted_arr[pointer1] > k):
            pointer1 = (pointer1 + pointer2)//2
            pointer2 = (pointer1 + pointer2)//2
            continue

        if (sorted_arr[pointer1] >= k//2):
            if (sorted_arr[pointer1] + sorted_arr[pointer2] == k):
                return True
            
            if (sorted_arr[pointer1] + sorted_arr[pointer2] > k):
                if (pointer2 == 0):
                    return False
                pointer2 = pointer2 // 2
                continue

            if (sorted_arr[pointer1] + sorted_arr[pointer2] < k):
                pointer2 = (pointer1 + pointer2)//2
                continue

        if (sorted_arr[pointer1] < k//2):
            pointer1 = (len(sorted_arr) - pointer1)//2 + pointer1
            pointer2 = (pointer1 + pointer2)//2
            continue

    return False
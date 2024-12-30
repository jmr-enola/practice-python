'''
Given an integer k and a string s, find the length of the longest substring that contains at most k distinct characters.

For example, given s = "abcba" and k = 2, the longest substring with k distinct characters is "bcb".
'''
def solution01(k: int, s: str) -> int:
    p1 = 0
    p2 = 1
    maxLength = 0
    
    while (p2 <= len(s)):
                
        if len({*s[p1:p2]}) > k:
            p1 += 1
            continue
        
        if len({*s[p1:p2]}) == k:
            maxLength = p2 - p1 if p2 - p1 > maxLength else maxLength

        p2 += 1

    return maxLength

    
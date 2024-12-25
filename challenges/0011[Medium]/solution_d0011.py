'''
Implement an autocomplete system. That is, given a query string s and a set of all possible query strings, return all strings in the set that have s as a prefix.

For example, given the query string de and the set of strings [dog, deer, deal], return [deer, deal].

Hint: Try preprocessing the dictionary into a more efficient data structure to speed up queries.
'''

from typing import List

def solution01(prefix: str, arr: List[str]) -> List[str]:
    
    results: List[str] = []

    def isMatched(pre: str, word: str) -> bool:
        for i in range(len(pre)):
            if (pre[i] != word[i]):
                return False
        
        return True

    for word in arr:
        if (isMatched(prefix, word)):
            results.append(word)

    return results
'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def solution01(message: str) -> int:

    if (int(message[0]) <= 0 or int(message[0]) > 9):
        return 0
        
    size = len(message)
    max_pair = size // 2
    
    def helper (message: str, pairs: int) -> int:
        counter = 0
        size = len(message)
        pointer = 0

        if (pairs < 1):
            return 1
        
        if (pairs >= 1):
            while (pointer < size - pairs * 2 + 1):
                if (int(message[pointer:pointer+2]) > 0 and int(message[pointer:pointer+2]) <= 26):
                    counter += helper(message[pointer+2:], pairs - 1)
                pointer += 1
            return counter
            
    count = 0

    for i in range(max_pair, -1, -1):
        count += helper(message, i)

    return count

# print(solution01('111'))
# print(solution01('1112'))
# print(solution01('11123'))
# print(solution01('111213'))
# print(solution01('111234'))
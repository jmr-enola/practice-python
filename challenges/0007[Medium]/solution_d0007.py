'''
Given the mapping a = 1, b = 2, ... z = 26, and an encoded message, count the number of ways it can be decoded.

For example, the message '111' would give 3, since it could be decoded as 'aaa', 'ka', and 'ak'.

You can assume that the messages are decodable. For example, '001' is not allowed.
'''

def solution01(message: str) -> int:

    if (0 >= int(message[0]) > 9):
        return 0
        
    size = len(message)
    max_pair = size // 2
    
    def helper (message: str, pairs: int) -> int:
        counter = 0
        size = len(message)
        pointer = 0

        if (pairs < 1):
            return 1 if(message.find('0') < 0) else 0
        
        if (pairs == 1):       
            while (pointer < size - 1):
                # Check if the two characters form a valid number (10-26)
                if (10 <= int(message[pointer:pointer+2]) <= 26):
                    remaining_digits = message[:pointer] + "" + message[pointer+2:]
                    print(remaining_digits, message[:pointer], message[pointer+2:])
                    # Check if the single character is a valid digit (1-9)
                    if (remaining_digits.find('0') <= -1):
                        counter += helper(message[pointer+2:], pairs - 1)
                pointer += 1
            return counter

        if (pairs > 1):
            while (pointer < size - pairs * 2 + 1):
                # Check if the two characters form a valid number (10-26)
                if (10 <= int(message[pointer:pointer+2]) <= 26):
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


def solution02(message: str, pairs=-1) -> int:

    size = len(message)
    counter = 0

    if (not isinstance(pairs, int)):
        return 0 

    if (pairs < 0):
        if ( 0 >= int(message[0]) > 9):
            return 0
        else:            
            max_pairs = size//2
            for i in range(max_pairs, -1, -1):
                counter += solution02(message, i)
            return counter

    if (pairs == 0):
        return 1 if(message.find('0') < 0) else 0
    
    if (pairs == 1):       
        for pointer in range(size - 1):
            # Check if the two characters form a valid number (10-26)
            if (10 <= int(message[pointer:pointer+2]) <= 26):
                remaining_digits = message[:pointer] + message[pointer+2:]
                print(message, pointer, message[pointer:pointer+2], message[:pointer], message[pointer+2:], remaining_digits)
                # Check if the single character is a valid digit (1-9)
                if (remaining_digits.find('0') < 0):
                    counter += solution02(message[pointer+2:], pairs - 1)
        return counter

    if (pairs > 1):
        for pointer in range(size - pairs * 2 + 1):
            # Check if the two characters form a valid number (10-26)
            if (10 <= int(message[pointer:pointer+2]) <= 26):
                counter += solution02(message[pointer+2:], pairs - 1)
        return counter

def solution03(message):
    size = len(message)
    if (size == 0 or message[0] == '0'):
        return 0

    ways2decode = [0] * (size + 1)
    ways2decode[0] = 1
    ways2decode[1] = 1

    for i in range(2, size + 1):
        # Check if the single character is a valid digit (1-9)
        if (message[i - 1] != '0'):
            ways2decode[i] += ways2decode[i - 1]

        # Check if the two characters form a valid number (10-26)
        two_digit = int(message[i - 2:i])
        if (10 <= two_digit <= 26):
            ways2decode[i] += ways2decode[i - 2]

    return ways2decode[size]
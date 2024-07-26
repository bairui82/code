"""
For a given string that only contains alphabet characters a-z, if 3 or more consecutive 
characters are identical, remove them from the string. Repeat this process until 
there is no more than 3 identical characters sitting besides each other. 
Example: 
Input: aabcccbbad 
Output: 
-> aabbbad 
-> aaad 
-> d
"""
import copy
def remove_consecutive(_string):
    # set switch for jump out the loop
    switch = 1
    while switch != 0:
        i = 0
        # temp save the _string to identify when to jump out the loop
        temp_copy = copy.copy(_string)
        # for each loop finding out the consecutive characters
        while i < len(_string) - 2:
            # find the case to deal with the consecutive characters
            if _string[i] == _string[i+1] == _string[i+2]:
                j = i + 3
                # when characters appear 3 times more
                while j < len(_string) and _string[j] == _string[i]:
                    j += 1
                # when the consecutive case happened at the end of the string
                if j == len(_string):
                    _string = _string[:i]
                # else
                else:
                    _string = _string[:i] + _string[j:]
                break
            i += 1
        # No more consecutive case detected jump out the loop
        if temp_copy == _string:
            switch = 0
        else:
            # show the process
            print(f'temp:"{_string}"')
    # return the result
    return _string
# Example usage 
print("-"*15)
input_string = "aaabbbcccdddeeeefffggg"  
result = remove_consecutive(input_string)
assert result == ""
print("passed test")
print("-"*15)
input_string = "aaabbbcccdddeeeefffggga"  
result = remove_consecutive(input_string)
assert result == "a"
print("passed test")
print("-"*15)
input_string = "aabcccbbad"  
result = remove_consecutive(input_string)
assert result == "d"
print("passed test")
"""#Stage 2 - advanced requirement 
Instead of removing the consecutively identical characters, replace them with a 
single character that comes before it alphabetically.
"""
def remove_consecutive_advanced(_string):
    # set switch for jump out the loop
    switch = 1
    while switch != 0:
        i = 0
        temp_copy = copy.copy(_string)
        # for each loop finding out the consecutive characters
        while i < len(_string) - 2:
            # find the case to deal with the consecutive characters
            if _string[i] == _string[i+1] == _string[i+2]:
                j = i + 3
                # when characters appear 3 times more
                while j < len(_string) and _string[j] == _string[i]:
                    j += 1
                # for the given case if the consecutive case happened with letter "a" the replacement won't be "z" instead it replace with ""
                if _string[i] != "a":
                    # when the consecutive case happened at the end of the string
                    if j == len(_string):
                        _string = _string[:i] + chr(ord(_string[i]) -1)
                    # else
                    else:
                        _string = _string[:i] + chr(ord(_string[i]) -1)+ _string[j:]
                else:
                    if j == len(_string):
                        _string = _string[:i]
                    else:
                        _string = _string[:i] + _string[j:]
                break
            i += 1
        # No more consecutive case detected jump out the loop
        if temp_copy == _string:
            switch = 0
        else:
            print(f'temp:"{_string}"')
    return _string

# Example usage 
print("-"*15)
input_string = "abcccbad"  
result = remove_consecutive_advanced(input_string)
assert result == "d"
print("passed test")
print("-"*15)
input_string = "aaabbbcccdddeeeefffggg"  
result = remove_consecutive_advanced(input_string)
assert result == "abcdef"
print("passed test")
print("-"*15)
input_string = "aaabbbcccdddeeeefffggga"  
result = remove_consecutive_advanced(input_string)
assert result == "abcdefa"
print("passed test")
print("-"*15)
input_string = "affffeeeddccbbaa"  
result = remove_consecutive_advanced(input_string)
assert result == ""
print("passed test")
print("-"*15)
input_string = "gffffeeeddccbbaa"  
result = remove_consecutive_advanced(input_string)
assert result == "g"
print("passed test")
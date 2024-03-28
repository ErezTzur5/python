mixed_list = [1, "hello", 3, "ddddddddddddddddddaaaaa", "boberrrrrrrrrrrr",700000]


def find_longest_string(mixed_list:list):
    """
    This functions takes a list and checks what is the longest string and returns the string.
    this function returns a string
    """
    longest_string = ""
    for item in mixed_list:
        if isinstance(item, str) and len(item) > len(longest_string):
            longest_string = item
    return longest_string




result = find_longest_string(mixed_list)
print(result)
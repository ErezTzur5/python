


def encode_string(string:str):
    """
    This function takes an string and double every character in the string.
    this finction returns a string.

    """
    encoded = ""
    for char in string:
        encoded += char * 2
    return encoded

def decode_string(string:str):
    """
    This function takes the encoded string and and delete's every second character which means back to original
    this function returns a string
    """
    decoded = ""
    for index in range(len(string)):
        if index % 2 == 0:
            decoded += string[index]
    return decoded

# Example usage
original_string = "Shabat Shalom Elik!"
encoded_string = encode_string(original_string)
print("Encoded:", encoded_string)

decoded_string = decode_string(encoded_string)
print("Decoded:", decoded_string)
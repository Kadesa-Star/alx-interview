#!/usr/bin/python3
"""
0-validate_utf8.py
"""

def validUTF8(data):
    """
    Determines if a given data set represents a valid UTF-8 encoding.
    
    Args:
    data (List[int]): A list of integers where each integer represents a byte.
    
    Returns:
    bool: True if data is a valid UTF-8 encoding, else False.
    """
    # Number of bytes remaining to complete a character
    bytes_remaining = 0

    # Iterate through each byte in the data list
    for byte in data:
        # Mask to get only the least 8 bits of each integer (1 byte)
        byte = byte & 0xFF

        if bytes_remaining == 0:
            # Determine the number of bytes in this UTF-8 character
            if (byte >> 5) == 0b110:       # 2-byte character
                bytes_remaining = 1
            elif (byte >> 4) == 0b1110:    # 3-byte character
                bytes_remaining = 2
            elif (byte >> 3) == 0b11110:   # 4-byte character
                bytes_remaining = 3
            elif (byte >> 7):              # Invalid 1-byte character
                return False
        else:
            # Check if it is a valid continuation byte (10xxxxxx)
            if (byte >> 6) != 0b10:
                return False
            bytes_remaining -= 1

    # Return True if all characters are valid and bytes_remaining is 0
    return bytes_remaining == 0

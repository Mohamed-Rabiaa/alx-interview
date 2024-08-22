#!/usr/bin/python3
"""
This module contains the validUTF8 function
"""


def validUTF8(data):
    """
    validUTF8 function
    """
    n_bytes = 0  # Number of bytes in the current UTF-8 character

    # Masks to check the most significant bits (MSBs)
    mask1 = 1 << 7
    mask2 = 1 << 6

    for byte in data:
        mask = 1 << 7
        if n_bytes == 0:
            # Count the number of 1s in the MSB of the first byte
            while mask & byte:
                n_bytes += 1
                mask >>= 1

            # 1-byte characters (ASCII) have no leading 1 bits
            if n_bytes == 0:
                continue

            # Invalid scenarios
            if n_bytes == 1 or n_bytes > 4:
                return False
        else:
            # Check that the byte starts with 10xxxxxx
            if not (byte & mask1 and not (byte & mask2)):
                return False

        n_bytes -= 1

    # If all characters are valid, n_bytes should be 0 at the end
    return n_bytes == 0

#!/usr/bin/python3
'''
This module contains the canUnlockAll function
'''


def canUnlockAll(boxes):
    '''
    Determines if all the boxes can be unlocked.

    You start with the first box (box 0) unlocked.Each box may contain
    keys to other boxes. The function checks if you can unlock all the
    boxes starting from the first box.

    Args:
        boxes (list of list of int): A list of boxes, where each box is
        represented as a list of keys it contains.

    Returns:
        bool: True if all boxes can be unlocked, False otherwise.
    '''
    unlocked = set()
    keys = set(boxes[0])
    unlocked.add(0)

    while keys:
        new_keys = set()
        for key in keys:
            if key not in unlocked and key < len(boxes):
                unlocked.add(key)
                new_keys.update(boxes[key])
        if not new_keys:
            break
        keys = new_keys

    return (len(unlocked) == len(boxes))

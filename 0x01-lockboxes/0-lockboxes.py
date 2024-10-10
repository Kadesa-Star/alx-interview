#!/usr/bin/python3
"""
Module to determine if all lockboxes can be unlocked.
"""


def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    :param boxes: List of lists each sublist contains for keys boxes.
    :return: True if all boxes can be opened, False otherwise.
    """
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True
    keys = set(boxes[0])
    visited = set([0])

    while keys:
        new_key = keys.pop()
        if new_key < n and new_key not in visited:
            visited.add(new_key)
            unlocked[new_key] = True
            keys.update(boxes[new_key])

    return all(unlocked)

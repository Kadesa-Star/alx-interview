#!/usr/bin/python3
def canUnlockAll(boxes):
    """
    Determines if all boxes can be unlocked
    :param boxes: List of lists where each sublist contains keys for other boxes
    :return: True if all boxes can be opened, False otherwise
    """
    n = len(boxes)
    unlocked = [False] * n  # Track whether each box is unlocked
    unlocked[0] = True  # Box 0 is always unlocked
    keys = set(boxes[0])  # Start with keys from Box 0
    visited = set([0])  # Track which boxes have been visited
    
    # While there are keys to check
    while keys:
        new_key = keys.pop()  # Take a key
        if new_key < n and new_key not in visited:  # If the key unlocks a valid box
            visited.add(new_key)  # Mark the box as visited
            unlocked[new_key] = True  # Unlock the box
            keys.update(boxes[new_key])  # Add new keys from the unlocked box

    return all(unlocked)  # Return True if all boxes are unlocked, False otherwise

#!/usr/bin/python3
"""
Lockboxes problem
"""


def canUnlockAll(boxes):
    """Determines if all boxes can be opened."""
    n = len(boxes)
    opened = [False] * n
    opened[0] = True
    stack = [0]

    while stack:
        current_box = stack.pop()
        for key in boxes[current_box]:
            if key < n and not opened[key]:
                opened[key] = True
                stack.append(key)

    return all(opened)

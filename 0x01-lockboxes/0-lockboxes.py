#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    """
    Write a method that determines if all the boxes can be opened.
    """

    list_keys = [0]
    for key in list_keys:
        for box_key in boxes[key]:
            if box_key not in list_keys and box_key < len(boxes):
                list_keys.append(box_key)
    if len(list_keys) == len(boxes):
        return True
    return False

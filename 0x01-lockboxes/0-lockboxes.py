#!/usr/bin/python3
"""Script will unlock list of lists"""


def canUnlockAll(boxes):
    """
    This function will take a list of lists and the content
    of a list will unlock other list
    """
    unlocked = set()

    for box_id, box in enumerate(boxes):
        if len(box) == 0 or box_id == 0:
            unlocked.add(box_id)
        for key in box:
            if key < len(boxes) and key != box_id:
                unlocked.add(key)
        if len(unlocked) == len(boxes):
            return True
    return False

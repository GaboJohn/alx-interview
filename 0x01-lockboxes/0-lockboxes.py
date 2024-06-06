#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determines if all the boxes can be opened or not
    Returns:
        True: all boxes can be opened
        False: not all boxes can be opened
    '''
    n = len(boxes)
    unlocked = [False] * n
    unlocked[0] = True

    keys = set(boxes[0])
    keys.add(0)

    while keys:
        key = keys.pop()
        if not unlocked[key]:
            unlocked[key] = True
            keys.update(k for k in boxes[key] if k < n)

    return all(unlocked)

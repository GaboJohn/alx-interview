#!/usr/bin/python3
'''LockBoxes Challenge'''


def canUnlockAll(boxes):
    '''determine if all the boxes can be unlocked or not
    Returns:
        True: all boxes can be unlocked
        False: all boxes cannot be unlocked
    '''
    x = len(boxes)
    keys = set()
    unlocked = []
    i = 0

    while i < x:
        length = i
        unlocked.append(i)
        keys.update(boxes[i])
        for key in keys:
            if key != 0 and key < x and key not in unlocked:
                i = key
                break
        if length != i:
            continue
        else:
            break

    for i in range(x):
        if i not in unlocked and i != 0:
            return False
    return True

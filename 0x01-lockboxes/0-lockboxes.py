#!/usr/bin/python3
"""Solves the lock boxes puzzle"""

from collections import deque

def canUnlockAll(boxes):
    """Check if all boxes can be opened
    Args:
        boxes (list): List where each element is a list of keys for that box.
    Returns:
        bool: True if all boxes can be opened, otherwise False.
    """
    if not boxes:
        return False

    n = len(boxes)
    opened = [False] * n  # Track which boxes have been opened
    queue = deque([0])    # Start with the first box (index 0)

    while queue:
        current_box = queue.popleft()
        if not opened[current_box]:
            opened[current_box] = True
            for key in boxes[current_box]:
                if key < n and not opened[key]:
                    queue.append(key)

    return all(opened)

def main():
    """Entry point"""
    boxes = [[1], [2], [3], [4], []]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4, 6], [2], [0, 4, 1], [5, 6, 2], [3], [4, 1], [6]]
    print(canUnlockAll(boxes))  # Expected output: True

    boxes = [[1, 4], [2], [0, 4, 1], [3], [], [4, 1], [5, 6]]
    print(canUnlockAll(boxes))  # Expected output: False

if __name__ == '__main__':
    main()


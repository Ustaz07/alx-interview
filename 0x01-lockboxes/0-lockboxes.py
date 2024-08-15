#!/usr/bin/python3

def canUnlockAll(boxes):
    """
    Determine if all the boxes can be opened.
    
    Args:
        boxes (list of lists): A list where each element is a list of keys for that box.
        
    Returns:
        bool: True if all boxes can be opened, False otherwise.
    """
    if not boxes:
        return False
    
    n = len(boxes)
    visited = set()
    queue = [0]
    
    while queue:
        current_box = queue.pop(0)
        if current_box in visited:
            continue
        
        visited.add(current_box)
        
        for key in boxes[current_box]:
            if key < n and key not in visited:
                queue.append(key)
    
    return len(visited) == n


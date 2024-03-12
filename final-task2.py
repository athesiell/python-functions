from typing import List

def split_by_index(s: str, indexes: List[int]) -> List[str]:
    indexes.sort()
    parts = []
    start = 0
    for index in indexes:
        if index <= len(s):
            parts.append(s[start:index])
            start = index
    parts.append(s[start:])
    return parts
        
print(split_by_index("pythoniscool,isn'tit?", [6,8,12,13,18]))
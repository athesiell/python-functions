from typing import Any, List

def linear_seq(sequence: List[Any]) -> List[Any]:
    my_list = []
    for i in sequence:
        if type(i) in [list,tuple]:
        # if isinstance(i, (list,tuple)):
            my_list.extend(linear_seq(i))
        else:
            my_list.append(i)
    return my_list

sequence = [1,2,3, [4,5, (6,7)]]

print(linear_seq(sequence))
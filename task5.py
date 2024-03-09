from typing import List, Tuple, Union

def seq_sum(sequence: Union[List, Tuple]) -> int:
    value = 0
    for i in sequence:
        if isinstance(i, (list,tuple)):
        # if type(i) in [list, tuple]:
            value += seq_sum(i)
        else:
            value += i
    return value

sequence = [1,2,3,[4,5,(6,7)]]

print(seq_sum(sequence))
from typing import Dict

def generate_squares(num: int)-> Dict[int, int]:
    new_dict = {i: i * i for i in range(1, num +1 )}
    return new_dict

print(generate_squares(5))
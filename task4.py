from typing import List, Dict

def combine_dicts(*args:List[Dict[str,int]]) -> Dict[str, int]:
    combined_dict = {}
    for d in args:
        for key, value in d.items():
            combined_dict[key] = combined_dict.get(key, 0) + value
    return combined_dict

dict_1 = {'a': 100, 'b': 200}
dict_2 = {'a': 200, 'c': 300}
dict_3 = {'a': 300, 'd': 100}

print(combine_dicts(dict_1, dict_2))
print(combine_dicts(dict_1, dict_2, dict_3))
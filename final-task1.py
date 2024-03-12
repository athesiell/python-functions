from typing import List

def split(data: str, sep=None, maxsplit=-1):
    splits = []
    temp = ""
    split_count = 0
    for char in data:
        if sep is not None and char == sep:
            splits.append(temp)
            temp = ""
            split_count += 1
            if maxsplit >= 0 and split_count >= maxsplit:
                break
        elif char == " ":
            splits.append(temp)
            temp = ""
        else:
            temp += char
        splits.append(temp)
        return splits
    

if __name__ == '__main__':
    assert split('') == []
    assert split(',123,', sep =',') == ['', '123', '']
    assert split('test') == ['test']
    assert split('Python    2    3', maxsplit=1) == ['Python', '2    3']
    assert split('     test     6    7', maxsplit=1) == ['test', '6    7']
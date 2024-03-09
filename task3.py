def union(*args) -> set:
    result = set()
    for arg in args:
        # if isinstance(arg, (list, tuple)):
        if type(arg) in [list, tuple]:
            result.update(set(arg))
        elif type(arg) in [set]:
            result.update(arg)
    return result


def intersect(*args) -> set:
    result = set()
    for arg in args:
        if isinstance(arg, (list,tuple)):
            arg_set = set(arg)
        elif isinstance(arg, set):
            arg_set = arg
        if result:
            result.intersection_update(arg_set)
        else:
            result.update(arg_set)
    return result


print(union(('S', 'A', 'M'), ['S', 'P', 'A', 'C']))
print(intersect(('S', 'A', 'C'), ('P', 'C', 'S'), ('G', 'H', 'S', 'C')))
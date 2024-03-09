from typing import Dict, Any, Callable, Iterable

DataType = Iterable[Dict[str, Any]]
ModifierFunc = Callable[[DataType], DataType]

def query(data: DataType, selector: ModifierFunc,
          *filters: ModifierFunc) -> DataType:
    result = selector(data)
    for filter_func in filters:
        result = filter_func(result)
    return result



def select(*columns: str) -> ModifierFunc:
    search_fields = columns
    
    def selector(data: DataType) -> DataType:
        selected_list = []
        for i in data:
            selected_dict = {key: value for (key, value) in i.items() if key in search_fields }
            selected_list.append(selected_dict)
            data = selected_list
        return data
    return selector



def field_filter(column: str, *values: Any) -> ModifierFunc:
    flt_key = column
    flt_values = values
    def fltr(data: DataType) -> DataType:
        filtered_list = []
        for i in data:
            if(flt_key in i.keys() and i[flt_key] in flt_values) or not (flt_key in i.keys()):
                filtered_list.append(i)
            data = filtered_list
            return data
    return fltr



def test_query():
    friends = [
        {'name': 'Sam', 'gender': 'male', 'sport': 'Basketball'}
    ]
    value = query(
        friends,
        select(*('name', 'gender', 'sport')),
        field_filter(*('sport', *('Basketball', 'volleyball'))),
        field_filter(*('gender', *('male,'))),
    )
    assert [{'gender': 'male', 'name': 'Sam', 'sport': 'Basketball'}] == value



if __name__ == "__main__":
    test_query()
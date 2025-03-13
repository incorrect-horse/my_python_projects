def foo_bar_list_or_tuple(my_list):
    if isinstance(my_list, str):
        print(my_list)
    else:
        for x in my_list:
            if isinstance(x, dict):
                foo_bar_dict(x)
            elif not isinstance(x, int):
                if len(x) == 1:
                    print(x)
                else:
                    foo_bar_list_or_tuple(x)
            else:
                print(x)

def foo_bar_dict(my_dict):
    if isinstance(my_dict, str):
        print(my_dict)
    else:
        for key, val in my_dict.items():
            if isinstance(val, list) or isinstance(val, tuple):
                print(key)
                foo_bar_list_or_tuple(val)
            elif isinstance(val, dict):
                print(key)
                foo_bar_dict(val)
            else:
                print(key)
                print(val)

def run(my_list):
    for i in my_list:
        if isinstance(i, list) or isinstance(i, tuple):
            foo_bar_list_or_tuple(i)
        elif isinstance(i, dict):
            foo_bar_dict(i)
        else:
            print(i)

# my_list = 123, "abc", [['a','b','c'], 2, {"key1": "val1", "key2": "val2"}], {"key3": "val3", "KEY0": ["def", 456], "KEY1": {"key4": "val4"}}, 789,
my_list = 123, "abc", [['a','b','c', {'test': 'dict', 'nested_list': ['list','in','dict',{'dict':'in_list'}]}], 2, {"key1": "val1", "key2": "val2"}], \
{"key3": "val3", "KEY0": ["def", 456, ['12','ab',['34','cd',['56','ef',['78','gh',{'super_nested':'dict', 109871234: 'int_type_dict_key_test', \
'int_type_dict_value_test': 109871234, 'TUPLE_TUPLE_TUPLE': ('tuple', 'tuuple', 'tuuuple')}]], ("oops", 123, 'did i forget', 345, 'tuples??')]]], \
"KEY1": {"key4": "val4"}}, (1, 'A', 2, 'B', ['list', 1010101, '- - - - - -'], (987, (876, (765, {'dict': "ina tuuuple"}, 234, 123, [44, 'f0', '1x0']), \
345), 234), 123), 789,

print(type(my_list))
print(my_list)
print('Number of elements:', len(my_list))
print()
run(my_list)

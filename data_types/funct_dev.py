def foo_bar(my_list):
    for x in my_list:
        # print(type(x))
        # print(x)
        if not isinstance(x, list) and not isinstance(x, dict):
            print(x)
            pass
        elif isinstance(x, list):
            for y in x:
                if isinstance(y, int):
                    print(y)
                    pass
                else:
                    foo_bar(y)
        elif isinstance(x, dict):
            for key, val in x.items():
                print(key)
                print(val)
                # print('KEY:', key, 'VAL:', val)
                # foo_bar(x.items())
                for item in val:
                    if isinstance(item, int):
                        print(item)
                        pass
                    else:
                        # print('ITEM:', item)
                        # foo_bar((key, val))
                        foo_bar(item)
                        print(val)
                # foo_bar(x.items())
                # foo_bar((key, val))
    print("- # -\n")

my_list = 123, "abc", [['a','b','c'], 2, {"key1": "val1", "key2": "val2"}], {"key3": "val3", "KEY0": ["def", 456], "KEY1": {"key4": "val4"}}, 789,

print(my_list)
print()

foo_bar(my_list)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def foo_bar_list(my_list):
    if isinstance(my_list, str):
        print(my_list)
    else:
        for x in my_list:
            if not isinstance(x, int):
                if len(x) == 1:
                    print(x)
                else:
                    foo_bar_list(x)
            else:
                print(x)

my_list = [123, "abc", [['a','b','c'], 2, ["key1", "val1", "key2", "val2"]], ["key3", "val3", "KEY0", ["def", 456], "KEY1", ["key4", "val4"]], 789,]

print(my_list)
print()

foo_bar_list(my_list)

# - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - - -

def foo_bar_dict(my_dict):
    if isinstance(my_dict, str):
        print(my_dict)
    else:
        for key, val in my_dict.items():
            if isinstance(val, dict):
                foo_bar_dict(val)
            else:
                print(key)
                print(val)

my_list = {123: 'abc', 'tyuit': {2: {'a': 'b','c': '-'}, 'asd': {"key1": "val1", "key2": "val2"}}, 'lkj':{"key3": "val3", "KEY0": {"def": 456}, "KEY1": {"key4": "val4"}}, 789:'ZXC'}

print(my_list)
print()

foo_bar_dict(my_list)

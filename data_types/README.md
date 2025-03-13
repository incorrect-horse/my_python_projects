Project to work through iterating recursively nested unrelated data types and sets, accessing each element individually.

E.g. a list within a dictionary of different data types within a list within a tuple etc.

Inspired by a task to access employee data within nested dictionaries and lists / JSON data structures.

    {
        "Engineering": {
            "team1": {
                "members": [
                    {"name": "Alice", "role": "Engineer", "age": 30},
                    {"name": "Bob", "role": "Senior Engineer", "age": 35}
                ],
                "projects": ["Project A", "Project B"]
            },
            "team2": {
                "members": [
                    {"name": "Charlie", "role": "Engineer", "age": 28},
                    {"name": "David", "role": "Lead Engineer", "age": 40}
                ],
                "projects": ["Project C"]
            }
        },
        "HR": {
            "team1": {
                "members": [
                    {"name": "Grace", "role": "HR Specialist", "age": 27},
                    {"name": "Hank", "role": "HR Manager", "age": 38}
                ]
            }
        }
    }


Initial data sets used to develop individual functions:

my_list = 123, "abc", [['a','b','c'], 2, {"key1": "val1", "key2": "val2"}], {"key3": "val3", "KEY0": ["def", 456], "KEY1": {"key4": "val4"}}, 789,

my_list = {123: 'abc', 'tyuit': {2: {'a': 'b','c': '-'}, 'asd': {"key1": "val1", "key2": "val2"}}, 'lkj':{"key3": "val3", "KEY0": {"def": 456}, "KEY1": {"key4": "val4"}}, 789:'ZXC'}


Final data set to demonstrate completed script:

my_list = 123, "abc", [['a','b','c', {'test': 'dict', 'nested_list': ['list','in','dict',{'dict':'in_list'}]}], 2, {"key1": "val1", "key2": "val2"}], {"key3": "val3", "KEY0": ["def", 456, ['12','ab',['34','cd',['56','ef',['78','gh',{'super_nested':'dict', 109871234: 'int_type_dict_key_test', 'int_type_dict_value_test': 109871234, 'TUPLE_TUPLE_TUPLE': ('tuple', 'tuuple', 'tuuuple')}]], ("oops", 123, 'did i forget', 345, 'tuples??')]]], "KEY1": {"key4": "val4"}}, (1, 'A', 2, 'B', ['list', 1010101, '- - - - - -'], (987, (876, (765, {'dict': "ina tuuuple"}, 234, 123, [44, 'f0', '1x0']), 345), 234), 123), 789,

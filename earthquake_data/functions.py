def foo_bar_list_or_tuple(my_list):
    if isinstance(my_list, str):
        print(my_list)
    else:
        for x in my_list:
            if isinstance(x, dict):
                foo_bar_dict(x)
            elif isinstance(x, float):
                print(x)
            elif not isinstance(x, int):
                if len(x) == 1:
                    print(x)
                else:
                    foo_bar_list_or_tuple(x)
            else:
                print(x)


def foo_bar_dict(my_dict):
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
    if isinstance(my_list, dict):
        foo_bar_dict(my_list)
    else:
        for i in my_list:
            if isinstance(i, list) or isinstance(i, tuple):
                foo_bar_list_or_tuple(i)
            elif isinstance(i, dict):
                foo_bar_dict(i)
            else:
                print(i)
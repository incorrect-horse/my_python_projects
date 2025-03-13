import json


def read_file(input):
    global content
    with open (input, 'r') as file:
        content = json.load(file)
    return content


def get_employees(content):
    employee_list = []
    #contents = content['Engineering']['team1']['members']
    for key1, val1 in content.items():
        for key2, val2 in val1.items():
            for key3, val3 in val2.items():
                for i, val4 in enumerate(val3):
                    if isinstance(val4, dict):
                        employee_list.append(val4['name'])
    print("Employee List: ", employee_list)
    return


def get_data(content, employee):
    global result
    no_match = []
    for key1, val1 in content.items():
        for key2, val2 in val1.items():
            for key3, val3 in val2.items():
                for i, val4 in enumerate(val3):
                    if isinstance(val4, dict):
                        for key5, val5 in val4.items():
                            if val5 == employee:
                                print("\nName: ", val4['name'])
                                print("Role: ", val4['role'])
                                print("Age:  ", val4['age'])
                                print("Dept: ", key1)
                                print("Team: ", key2)
                                no_match.append(False)
                            else:
                                no_match.append(True)
    if all(no_match):
        result = "\nEmployee not found."
    else:
        result = "\nBye."
    return result


read_file("coding_13.json")
get_employees(content)
result = True

employee = input("Employee name: ")
print(get_data(content, employee))
#get_data(content, employee)

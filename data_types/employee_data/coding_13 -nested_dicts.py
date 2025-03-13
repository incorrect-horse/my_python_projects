import json


def read_file(input):
    global content
    with open (input, 'r') as file:
        content = json.load(file)
    return content


input_file = "coding_13.json"
read_file(input_file)

for key1, val1 in content.items():
#    print(key1)
#    print()
    for key2, val2 in val1.items():
#        print(key2)
        for key3, val3 in val2.items():
#            print(key3)
            #print(val3)
            for i, val4 in enumerate(val3):
#                print(f"{i}: {val4}")
#                print(type(val4))
                if isinstance(val4, dict):
#                    print(f"{i}: {val4}")
                    for key5, val5 in val4.items():
                        #print(type(key5))
#                        print("Key5 ", key5)
                        #print(type(val5))
#                        print("Val5 ", val5)
                        if val5 == "Charlie":
                            print()
                            print("* * * * * MATCH * * * * *")
                            print(type(val4))
                            print(f"{i}: {val4}")
                            print("Name: ", val4['name'])
                            print("Age: ", val4['age'])
                            print()
#            print("*********************")
#            print()


#content = content.values()

#print("\n", content)
#print("\n", type(content))

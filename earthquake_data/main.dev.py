import requests
import json
from functions import run
from pprint import pprint

URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

response = requests.get(URL)
raw_data = response.json()

def get_data(raw_data):
    count = 1
    count_down = 10
    tmp_number = 0.0
    max = 0.0
    top_ten = []
    main_dict_output = {}
    # output_list_2 = {}
    # print(raw_data.keys())
    print("Total records: ", len(raw_data["features"]))
    # print(len(raw_data["features"][0]["properties"]))
    # print(raw_data["features"][0]["properties"]["mag"])

    ## Dump raw data from URL to file
    with open('source_data.txt', 'w') as file:
        file.write(str(raw_data) + "\n")

    ## Print top 10 earthquakes to screen
    # for i in raw_data["features"]:
    #     tmp_number = float(i["properties"]["mag"])
    #     if tmp_number > max:
    #         max = float(tmp_number)
    #         top_ten.append(max)
    # print(max)
    # print(top_ten)

    # while count_down > 0:
    #     for i in raw_data["features"]:
    #         count += 1
    #         # print(i["properties"]["mag"])
    #         tmp_number = float(i["properties"]["mag"])
    #         # while count_down > 0:
    #         if tmp_number > max:
    #             print(count_down)
    #             # print(tmp_number)
    #             count_down -= 1
    #             # print(count_down)
    #             max = float(tmp_number)
    #             top_ten.append(max)
    #             # print(count)
    #             # print([i["properties"]["place"]])
    #             # print([i["properties"]["url"]])
    # print(max)
    # print(top_ten)

    ## Print first three entries to screen
    # for i in raw_data["features"]:
    #     if count <= 3:
    #         print(count)
    #         val_1 = [i["properties"]["mag"]]
    #         print(val_1[0])
    #         val_2 = [i["properties"]["place"]]
    #         print(val_2[0])
    #         # val_3 = [i["properties"]["url"]]
    #         # print(val_3[0])
    #         print("")

    ## Write all magnitues to output file
    # for i in raw_data["features"]:
    #     tmp_number = float(i["properties"]["mag"])
    #     with open('output.txt', 'a') as file:
    #         file.write(str(tmp_number) + "\n")

    ## Construct dictionary with numerical index and event
    ## event is sub-dictionary with Magnitude, Location, and URL
    for i in raw_data["features"]:
        individual_event = {}
        magnitude = [i["properties"]["mag"]]
        individual_event["Magnitude"] = magnitude[0]
        location = [i["properties"]["place"]]
        individual_event["Location"] = location[0]
        website_url = [i["properties"]["url"]]
        individual_event["URL"] = website_url[0]

        main_dict_output[count] = individual_event

        count += 1

    with open('output.txt', 'w') as file:
        file.write(str(main_dict_output) + "\n")

    find_max_mag_event(main_dict_output, printout=True)
    pprint(build_top_10_list(main_dict_output))


def find_max_mag_event(input_data, printout=False):
    max_mag = 0.0
    for index, event in input_data.items():
        if event['Magnitude'] > max_mag:
            max_mag = event['Magnitude']
            max_index = index

    if printout:
        print("\nLargest earthquake magnitude:", max_mag)
        print("Index number:", max_index)
        print("\ndict entry:", input_data[max_index])
    return max_index


def build_top_10_list(input_data):
    # take dict as working input
    # identify largest magnitude and associated index number (dict key)

    # append previous to new output dict

    # delete previous from working input
    # - dictionary.pop(keyname, defaultvalue)
    # - - output_dict[len(output_dict)] = input_dict.pop('index')
    # loop until new output dict.keys() == 10
    print("\nTop 10 earthquake events by magnitude:\n")

    sorted_dict = dict(sorted(input_data.items(), reverse=True, key=lambda item: item[1]['Magnitude']))

    counter = 0
    new_output_dict = {}
    for key, value in sorted_dict.items():
        if counter < 10:
            # print(counter)
            # print(value)
            # print(" ")
            new_output_dict[counter + 1] = value
            counter += 1
        else:
            break

    # new_output_dict = {}
    # max_index = find_max_mag_event(input_data)
    # # print(max_index)
    # # print(input_data[max_index])
    # new_output_dict[max_index] = input_data[max_index]
    # print(len(new_output_dict) + "\n")
    return new_output_dict
    # return sorted_dict
    # return


if __name__ == '__main__':
    # print("main")
    print(type(raw_data))
    # print(raw_data)
    print('Number of elements:', len(raw_data))
    print()
    # run(raw_data)
    get_data(raw_data)

print("\nGoodbye.\n")

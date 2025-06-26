import requests
from functions import run
from pprint import pprint


def run():
    raw_data = fetch_data()
    new_data = index_and_curate_data(raw_data)

    find_max_magnitude_event(new_data, printout=True)

    print("\nTop 10 earthquake events by magnitude:\n")
    pprint(build_top_10_list(new_data))
    return


def fetch_data():
    URL = "https://earthquake.usgs.gov/earthquakes/feed/v1.0/summary/all_week.geojson"

    response = requests.get(URL)
    raw_data = response.json()
    output_to_file(raw_data, file_name='source_data.txt')
    return raw_data


def index_and_curate_data(raw_data):
    count = 1
    main_dict_output = {}
    print("Total records: ", len(raw_data["features"]))

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

    output_to_file(main_dict_output, file_name='output.txt')
    return main_dict_output


def output_to_file(output_data, file_name):
    with open(file_name, 'w') as file:
        file.write(str(output_data) + "\n")
    return


def find_max_magnitude_event(input_data, printout=False):
    max_mag = 0.0
    for index, event in input_data.items():
        if event['Magnitude'] > max_mag:
            max_mag = event['Magnitude']
            max_index = index

    if printout:
        print("\nLargest earthquake magnitude:", max_mag)
        print("Index number:", max_index)
        print("Event:", input_data[max_index])
    return max_index


def build_top_10_list(input_data):
    sorted_dict = dict(sorted(input_data.items(), reverse=True, key=lambda item: item[1]['Magnitude']))

    counter = 0
    new_output_dict = {}
    for key, value in sorted_dict.items():
        if counter < 10:
            new_output_dict[counter + 1] = value
            counter += 1
        else:
            break
    return new_output_dict


if __name__ == '__main__':
    run()

print("\nGoodbye.\n")

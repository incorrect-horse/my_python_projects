import requests
from pprint import pprint

URL = "https://ip-ranges.amazonaws.com/ip-ranges.json"

"""# JSON DATA STRUCTURE
# {
#   "syncToken": "nnnnnnnnnn",
#   "createDate": "YYYY-MM-DD-HH-MM-SS",
#   "prefixes": [
#     {
#       "ip_prefix": "IPv4 CIDR IP address range",
#       "region": "region name",
#       "service": "service name",
#       "network_border_group": "network border group"
#     },
#   ]
#   "ipv6_prefixes": [
#     {
#       "ipv6_ip_prefix": "IPv6 CIDR IP address",
#       "region": "region name",
#       "service": "service name",
#       "network_border_group": "network border group"
#     },
#   ]
# }

# {'ip_prefix': '51.0.28.0/24', 'region': 'eusc-de-east-1',
#  'service': 'DYNAMODB', 'network_border_group': 'eusc-de-east-1'}"""

response = requests.get(URL)
raw_data = response.json()


def date_time():
    date_time = raw_data['createDate'][:]
    date = date_time[:10]
    hh = date_time[11:13]
    mm = date_time[14:16]
    ss = date_time[17:19]
    time = (f"{hh}:{mm}:{ss}")
    return (f"{date} {time}")


def ip_range_lookup_menu():
    lookup_options = "\nChoose a dataset to lookup:\n\
    \n  r | AWS Regions\
    \n  s | AWS Services\
    \n  n | AWS Network Border Groups\
    \n  p | Previous section\
    \n\nEnter selection: "

    while True:
        lookup_actn = input(lookup_options).strip().lower()
        if lookup_actn.startswith("region") or lookup_actn.startswith("r"):
            build_ip_range_lookup('prefixes', "region")
        elif lookup_actn.startswith("service") or lookup_actn.startswith("s"):
            build_ip_range_lookup('prefixes', "service")
        elif lookup_actn.startswith("network") or lookup_actn.startswith("n"):
            build_ip_range_lookup('prefixes', "network_border_group")
        elif lookup_actn.startswith("previous") or lookup_actn.startswith("p"):
            break
        else:
            print("\nOops! Command not recognized... Try again.")
    return


def build_ip_range_query():
    USE_TEST_VALUES = False
    if USE_TEST_VALUES:
        # BYPASS ENTERING INPUTS WHILE TESTING/DEVELOPING
        region = "north"
        service = "ALL"
        network = "north"
        prnt_nr = 1
    else:
        region_msg = \
"\nEnter a region to query. E.g. 'north' or 'ALL': "
        service_msg = \
"\nEnter a service to query. E.g. 'AMAZON' or 'ALL': "
        network_msg = \
"\nEnter a network border group to query. E.g. 'north' or 'ALL': "
        prnt_nr_msg = \
"\nSelect number of query matches to return from top and\
 bottom of list.\n\nE.g. Entering '5' will return the top five\
 and bottom five results. Alternatively, entering 'ALL' will\
 return all query results. Note, full queries can return\
 hundreds or thousands of results.\n\nEnter a number: "
        region = input(region_msg)
        service = input(service_msg).upper()
        network = input(network_msg)
        if region == "":
            region = "ALL"
        if service == "":
            service = "ALL"
        if network == "":
            network = "ALL"
        if region == "ALL" or service == "ALL" or network == "ALL":
            prnt_nr = 0
            output = "ALL"
        else:
            prnt_nr = input(prnt_nr_msg)
            output = int(prnt_nr) * 2
    print(f"\nRegion: {region}\nService: {service}\
          \nNetwork: {network}\nOutput: {output}")
    input("\nPress enter to continue.")
    query_data(region, service, network, prnt_nr)
    return


def get_total(region, service, network):
    total = 0
    MATCH = []
    for key0, val0 in raw_data.items():
        if key0.endswith('prefixes'):
            for index, item in enumerate(raw_data[key0]):
                for key, val in item.items():
                    if key == "region" and (region in val or region == "ALL"):
                        MATCH.append(True)
                    elif key == "service" and (service in val or service == "ALL"):
                        MATCH.append(True)
                    elif key == "network_border_group" and (network in val or network == "ALL"):
                        MATCH.append(True)
                    if len(MATCH) == 3:
                        total += 1
                MATCH = []
    print(f"\nTotal matches: {total}")
    return total


def build_ip_range_lookup(input_key, type_value):
    output = []
    for key, val in raw_data.items():
        if key.endswith(input_key):
            for index, item in enumerate(raw_data[key]):
                for key, val in item.items():
                    if key == type_value:
                        if val not in output:
                            output.append(val)
    output.sort()
    print(f"\n{type_value.upper()}S: {output}")
    refined_output = []
    while True:
        refine = input("\nRefine lookup results, 'yes'|'no': ").strip().lower()
        if refine.startswith("yes") or refine.startswith("y"):
            match_term = input("\nwhat do now?? e.g. west: ") # iasip
            if type_value == "service":
                match_term = match_term.upper()
            for index, item in enumerate(output):
                if match_term in item:
                    refined_output.append(item)
            if len(refined_output) != 0:
                print(f"\n{type_value.upper()}S: {refined_output}")
            else:
                input("\nNo results found. Press enter to continue.")
                break
            input("\nBam! Press enter to continue.")
            output = []
            for i in refined_output:
                output.append(i)
            refined_output = []
            if len(output) == 1:
                break
        else:
            break
    return


def query_data(region, service, network, prnt_nr):
    count = 0
    total = get_total(region, service, network)
    MATCH = []
    prnt_nr = int(prnt_nr)
    print_screens = 0
    pause = "no"
    if (prnt_nr == 0 or prnt_nr > 500) and total > 500:
        pause = input(f"\nUh oh! Output will be greater than 500\
 results. Consider making inputs more specific next time. Pause\
 prining every N lines, 'yes'|'no': ").strip().lower()
    if prnt_nr == 0: #in the case of region:ALL, service:ALL, network:ALL
        prnt_nr = total
    try:
        if pause.startswith("yes") or pause.startswith("y"):
            pause = "yes"
            pause_interval = int(input("\nEnter # of lines to print: "))
        elif pause.startswith("no") or pause.startswith("n"):
            pass
    except ValueError:
        pause_interval = 0
        input("\nInput not valid. Press enter to continue.")
    print("\n_query_data start_")
    for key0, val0 in raw_data.items():
        if key0.endswith('prefixes'):
            for index, item in enumerate(raw_data[key0]):
                for key, val in item.items():
                    if key == "region" and (region in val or region == "ALL"):
                        MATCH.append(True)
                    elif key == "service" and (service in val or service == "ALL"):
                        MATCH.append(True)
                    elif key == "network_border_group" and (network in val or network == "ALL"):
                        MATCH.append(True)
                    if len(MATCH) == 3:
                        count += 1
                        if count <= prnt_nr or count > total - prnt_nr:
                            pprint(item)
                            print_screens += 1
                        elif count == int(total/2):
                            print("...")
                MATCH = []
                if pause == "yes" and print_screens == pause_interval:
                    input("\nOutput paused, press enter to continue...")
                    print_screens = 0
                elif pause == "no":
                    continue
    print("\n_query_data complete_")
    input("\nPress ENTER to continue.")
    return


def format_paragraph(text, max_width):
    words = text.split()
    line = ""
    for word in words:
        if len(line) + len(word) <= max_width:
            line += word + " "
        else:
            print(line)
            line = word + " "
    print(line.strip())
    return


welcome_msg = "A utility to search AWS IP ranges. Search by\
 AWS Region, AWS Service, or AWS Network Border Group.\
 Additionally, this utility can print lists of current\
 regions, services, or network border groups."

print(f"JSON DATA CURRENT AS OF: {date_time()}\n")
format_paragraph(welcome_msg, 65)

options = "\nAWS IP RANGES -- Choose an option below:\n\
\n  l | Lookup values needed for IP Range queries\
\n  q | Query IP Ranges\
\n  x | Exit application\n\
\nEnter: "

while True:
    usr_actn = input(options).strip().lower()

    if usr_actn.startswith("lookup") or usr_actn.startswith("l"):
        ip_range_lookup_menu()
    elif usr_actn.startswith("query") or usr_actn.startswith("q"):
        build_ip_range_query()
    elif usr_actn.startswith("exit") or usr_actn.startswith("x"):
        break
    else:
        print("\nOops! Command not recognized... Try again.")

print("\nGoodbye.\n")

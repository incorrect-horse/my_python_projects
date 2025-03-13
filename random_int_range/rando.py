import random


def run():
    # range_max = 35 # max range of random number / total number of controls for review
    # list_min = 8 # min length of number list / min number of controls per row
    # list_max = 20 # max length of number list / max number of controls per row
    # loop_max = 37 # number of loops = length of output file / total number of rows

    range_max = 100 # max range of random number / total number of controls for review
    list_min = 3 # min length of number list / min number of controls per row
    list_max = 12 # max length of number list / max number of controls per row
    loop_max = 7 # number of loops = length of output file / total number of rows

    output = []
    counter = 0

    while counter < loop_max:
        rando = random.randint(1,range_max)
        gen_ran_num_lst(rando, output, range_max)
        if len(output) >= list_min and len(output) < list_max:
            write_output(output)
            # print(counter, output)
            counter += 1
        output = []
    return

def gen_ran_num_lst(rando, output, range_max):
    while len(output) < rando:
        new_rando = random.randint(1,range_max)
        if new_rando not in output:
            output.append(new_rando)

    output.sort()
    return output

def write_output(output):
    with open("output_lists.txt", 'a') as out_put:
        out_put.write(str(output) + "\n")
    return


if __name__ == '__main__':
    run()

print('\nGoodbye!')

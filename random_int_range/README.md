Random Integer Range

A simple script written to generate lists of random numbers to be used for a sampling task. Output is configurable by setting four variables shown below:

    # range_max = 35 # max range of random number / total number of items for review
    # list_min = 8 # min length of number list / min number of items per row
    # list_max = 20 # max length of number list / max number of items per row
    # loop_max = 37 # number of loops = length of output file / total number of rows

range_max - generates a range of randomly selected integers up to the number specified
list_min - determines range minimum length
list_max - determines range maximum length
loop_max - total number of rows needed for output

For example, the configuration shown below...

range_max = 100
list_min = 3
list_max = 12
loop_max = 7

... will output the following:

[5, 54, 61, 62, 64, 73, 79, 97]
[36, 67, 85, 89, 95, 99]
[7, 12, 29, 43, 44, 45, 47, 65, 89]
[2, 31, 48, 53, 59, 83, 98]
[5, 10, 26, 43, 50, 58, 59, 61, 64, 73, 80]
[10, 30, 69]
[17, 22, 25, 27, 28, 32, 54, 63, 74, 84, 89]

- Largest number in the entire output is 97 / range_max = n

    Each list consists of a range of random numbers, from 1 up to range max

- Shortest list has a length of 3 / list_min = n
- Longest list has a length of 11 / list_max = n

    Each list length is a random number, between min and max

- Output consists of 7 lists

    Not a random number, script will always loop n times / loop_max = n

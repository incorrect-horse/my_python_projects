import random

def generate_password(test=False):
    password = ''
    validate_pw_params = ()
    if test:
        pw_params = 20, True, True, True, True
        length, lower, upper, number, spec_char = pw_params
    else:
        while True not in validate_pw_params:
            pw_params = validate_length(), validate_lower(), validate_upper(), \
                        validate_number(), validate_spec_char()
            length, lower, upper, number, spec_char = pw_params
            validate_pw_params = lower, upper, number, spec_char
            if True not in validate_pw_params:
                print('\nYou need to select at least one character set.')

    while len(password) < length:
        lower_list = chr(random.randrange(int(ord('a')), int(ord('z'))))
        upper_list = chr(random.randrange(int(ord('A')), int(ord('Z'))))
        number_list = str(random.randint(0, 9))
        spec_char_list = '!@#$%^&*()_+|'
        if len(password) < length and lower and random.randint(0,1):
            password += random.choice(lower_list)
        if len(password) < length and upper and random.randint(0,1):
            password += random.choice(upper_list)
        if len(password) < length and number and random.randint(0,1):
            password += random.choice(number_list)
        if len(password) < length and spec_char and random.randint(0,1):
            password += random.choice(spec_char_list)
    return f'Generated password: {password}'


def validate_length():
    while True:
        try:
            length = int(input('\nPassword length: '))
            if length >= 8 and length <= 25:
                return length
            else:
                print('Enter a number between 8 and 25.')
        except ValueError:
            print('Input not valid, please try again.')


def validate_lower():
    while True:
        lower = input('Use lowercase letters? (y/n): ').strip().lower() or 'y'
        if lower == 'y':
            return True
        elif lower == 'n':
            return False
        else:
            print('\nInput not valid, please try again.')


def validate_upper():
    while True:
        upper = input('Use uppercase letters? (y/n): ').strip().lower() or 'y'
        if upper == 'y':
            return True
        elif upper == 'n':
            return False
        else:
            print('\nInput not valid, please try again.')


def validate_number():
    while True:
        number = input('Use numbers? (y/n): ').strip().lower() or 'y'
        if number == 'y':
            return True
        elif number == 'n':
            return False
        else:
            print('\nInput not valid, please try again.')


def validate_spec_char():
    while True:
        spec_char = input('Use special characters? (y/n): ').strip().lower() or 'y'
        if spec_char == 'y':
            return True
        elif spec_char == 'n':
            return False
        else:
            print('\nInput not valid, please try again.')


def test_run():
    for i in range(20):
        print(generate_password(test=True))


msg = '\n-- Password Generator --\n\
Choose an option:\n\
1: generate password\n\
2: exit the program\n\
Your choice: '

try:
    while True:
        usr_input = input(msg) or '1'
        if usr_input == '1':
            print('\n' + generate_password())
            pass
        elif usr_input == '2':
            print('\nProgram closed. Goodbye!')
            break
        elif usr_input == 'test':
            print()
            test_run()
            break
        else:
            print('\nOops! Input not valid, please try again.')
except KeyboardInterrupt:
    print('\nProgram terminated. Goodbye!')

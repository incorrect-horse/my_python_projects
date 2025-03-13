"""
Individual Function Version

A study in string manipulation and duplicating the
output of common python string methods: .upper(),
.lower(), .title(), .capitalize(), .split(), and
.join()
"""

def upper(text):
    new_upper = ''
    for ltr in text:
        if ord(ltr) >= 97 and ord(ltr) <= 122:
            new_upper += chr(ord(ltr) - 32)
        else:
            new_upper += chr(ord(ltr))
    return new_upper

def lower(text):
    new_lower = ''
    for ltr in text:
        if ord(ltr) >= 65 and ord(ltr) <= 90:
            new_lower += chr(ord(ltr) + 32)
        else:
            new_lower += chr(ord(ltr))
    return new_lower

def title(text):
    lower_text = lower(text)
    words = splitify(lower_text)
    new_word = ''
    new_words = []
    for word in words:
        for ltr in word[0]:
            new_word = upper(ltr) + word[1:]
        new_words.append(new_word)
    return stringify(new_words)

def capitalize(text):
    lower_text = lower(text)
    words = splitify(lower_text)
    new_word = ''
    new_words = []
    for word in words:
        if word is words[0]:
            for ltr in word[0]:
                new_word = upper(ltr) + word[1:]
            new_words.append(new_word)
        else:
            new_words.append(word)
    return stringify(new_words)

def stringify(text):
    new_string = ''
    for word in text:
        if word is not text[-1]:
            new_string += word + ' '
        else:
            new_string += word
    return new_string

def splitify(text):
    space_list = []
    counter = 0
    new_index = 0
    word = ''
    word_list = []
    for char in text:
        counter += 1
        if char == ' ':
            space_list.append(counter)
    for space_char in space_list:
        word = text[new_index:space_char - 1]
        new_index = space_char
        word_list.append(word)
    last_word = text[new_index:len(text)]
    word_list.append(last_word)
    return word_list

def test_run(test_text='test'):
    test_input = []
    if test_text == 'test':
        test_input = ['test test test']
    elif test_text == 'demo':
        test_input = ['abcdefghijklmnopqrstuvwxyz','abc123ABC456',
                    'ABCDEFGHIJKLMNOPQRSTUVWXYZ',
                    'test test Check 123, TEST! TEST!',
                    'THE quick brown FOX jumped over the lazy DOG.',
                    'Lorem ipsum dolor sit amet, consectetur adipiscing elit,']
    else:
        test_input.append(test_text)

    print('\nINPUT:', test_input)

    for i in test_input:
        print('\nUPPER:', upper(i))
        print('LOWER:', lower(i))
        print('TITLE:', title(i))
        print('CAPS :', capitalize(i))

if __name__ == '__main__':
    msg = "Test Mode Entered:\n\n\
'test' - A short test - 'test test test'\n\
'demo' - A demonstration with various text\n\n\
Enter a choice above or enter any text you choose: "
    usr_input = input(msg).strip().lower() or 'sample'
    test_run(usr_input)

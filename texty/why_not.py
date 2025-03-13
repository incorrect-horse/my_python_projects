"""
OOP Version

A study in string manipulation and duplicating the
output of common python string methods: .upper(),
.lower(), .title(), .capitalize(), .split(), and
.join()
"""

class Texty:
    def __init__(self):
        return

    def upper(self, text):
        new_upper = ''
        for ltr in text:
            if ord(ltr) >= 97 and ord(ltr) <= 122:
                new_upper += chr(ord(ltr) - 32)
            else:
                new_upper += chr(ord(ltr))
        return new_upper

    def lower(self, text):
        new_lower = ''
        for ltr in text:
            if ord(ltr) >= 65 and ord(ltr) <= 90:
                new_lower += chr(ord(ltr) + 32)
            else:
                new_lower += chr(ord(ltr))
        return new_lower

    def title(self, text):
        lower_text = self.lower(text)
        words = self.splitify(lower_text)
        new_word = ''
        new_words = []
        for word in words:
            for ltr in word[0]:
                new_word = self.upper(ltr) + word[1:]
            new_words.append(new_word)
        return self.stringify(new_words)

    def capitalize(self, text):
        lower_text = self.lower(text)
        words = self.splitify(lower_text)
        new_word = ''
        new_words = []
        for word in words:
            if word is words[0]:
                for ltr in word[0]:
                    new_word = self.upper(ltr) + word[1:]
                new_words.append(new_word)
            else:
                new_words.append(word)
        return self.stringify(new_words)

    def stringify(self, text):
        new_string = ''
        for word in text:
            if word is not text[-1]:
                new_string += word + ' '
            else:
                new_string += word
        return new_string

    def splitify(self, text):
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

    def test_run(self, test_text='test'):
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
            print('\nUPPER:', self.upper(i))
            print('LOWER:', self.lower(i))
            print('TITLE:', self.title(i))
            print('CAPS :', self.capitalize(i))

if __name__ == '__main__':
    msg = "Test Mode Entered:\n\n\
'test' - A short test - 'test test test'\n\
'demo' - A demonstration with various text\n\n\
Enter a choice above or enter any text you choose: "
    usr_input = input(msg).strip().lower() or 'sample'
    Texty().test_run(usr_input)

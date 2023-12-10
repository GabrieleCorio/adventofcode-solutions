import regex as re

f = open('input_2.txt', 'r')
f_content = f.read()

def search_characters(string):
    return re.findall(r'(\d|one|two|three|four|five|six|seven|eight|nine)', string, overlapped=True)

def replace_number_in_digit(list_number):

    replaces = {
        "one": '1',
        "two": '2',
        "three": '3',
        "four": '4',
        "five": '5',
        "six": '6',
        "seven": '7',
        "eight": '8',
        "nine": '9',
    }

    for i, number in enumerate(list_number):
        if number in replaces.keys():
            list_number[i] = replaces[number]
    
    return list_number

def unify_fist_and_last(list_digit):

    return list_digit[0] + list_digit[-1]

numbers = []
for line in f_content.split("\n"):
    numbers.append(int(unify_fist_and_last(replace_number_in_digit(search_characters(line)))))

print(sum(numbers))
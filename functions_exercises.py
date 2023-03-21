
def is_two(input):
    return input == 2 or input == '2'

def is_vowel(input):
    return input == ('a','e','i','o','u')

def is_consonant(input):
    return input != ('a','e','i','o','u')

def cap_con(word):
    vowels = ['a','e','i','o','u']
    if word[0].lower() not in vowels:
        return word.cap()
    else:
        return word
    
def cal_tip(percent,total):
    tip_amount = total * percent
    return tip_amount

def app_dis(price,percent):
    after_dis = percent * price
    return after_dis

def handle_commas(input_str):
    output_str = input_str.replace(',','')
    return int(output_str)

def get_letter_grade(number):
    if number > 88:
        return 'A'
    elif number > 78:
        return 'B'
    elif number > 68:
        return 'C'
    elif number > 58:
        return 'D'
    else:
        return 'F'
    
def remove_vowels(input_str):
    vowels = 'aeiouAEIOU'
    output_str = ''
    for char in input_str:
        if char not in vowels:
            output_str += char
        return output_str
    
def normalize_name(input_str):
    input_str = ''.join(char for char in input_str if char.isalnum() or char == '_')
    input_str = input_str.replace('','_')
    input_str = input_str.lower()
    if input_str[0].isdigit():
        input_str = '_'+ input_str
    return input_str

def cumulative_sum(numbers):
    running_sum = 0
    cumulative = []
    running_sum += numbers
    cumulative.append(running_sum)
    return cumulative

def is_two(input):
    # This function checks if the input is equal to eithe the integer '2' or the string 2.
    return input == 2 or input == '2'

def is_vowel(input):
    #This function checks if there is a vowel in the input.
    return input == ('a','e','i','o','u')

def is_consonant(input):
    #This function checks if the input is not = to a vowel.
    return input != ('a','e','i','o','u')

def cap_con(word):
    #This function defines vowels first, then makes the first letter of the word lowercase and is not a defined
    # vowel then it returns the word as a capitlized. 
    vowels = ['a','e','i','o','u']
    if word[0].lower() not in vowels:
        return word.cap()
    else:
        return word
    
def cal_tip(percent,total):
    # This function takes the % and total and multiplies them to return the tip amount.
    tip_amount = total * percent
    return tip_amount

def app_dis(price,percent):
    # This function takes the original price multiplied by the discount % and returns the amount after the discount.
    after_dis = percent * price
    return after_dis

def handle_commas(input_str):
    # This function returns an inputed string with the commas replaced with a no space using .replace.
    output_str = input_str.replace(',','')
    return int(output_str)

def get_letter_grade(number):
    # This function takes in a number between 0 - 100 and runs it thru the loop to define what the return should be.
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
    # This function checks the input to see if it has defined 'vowel(s)' and ignores them, then for not vowels
    # it adds the chars to a new string called output_str and returns the output_str with no space where a vowel used to be.
    vowels = 'aeiouAEIOU'
    output_str = ''
    for char in input_str:
        if char not in vowels:
            output_str += char
        return output_str
    
def normalize_name(input_str):
    # Replace spaces with underscores
    input_str = ''.join(char for char in input_str if char.isalnum() or char == '_')
    # Remove/replace non_alphanumeric chars
    input_str = input_str.replace('','_')
    # Convert to lowercase
    input_str = input_str.lower()
    # Remove leading underscores
    if input_str[0].isdigit():
        input_str = '_'+ input_str
    return input_str

def cumulative_sum(numbers):
    # Initialize a variable to store the running sum
    running_sum = 0
    # Create a empty list to store the cumulative sum
    cumulative = []
    # Iterate thru the list of numbs
    for number in numbers:
        # Add the current numver to the running sum
        running_sum += number
        # Append the running sum to the cumulative list
    cumulative.append(running_sum)
    #return the cumulative list
    return cumulative
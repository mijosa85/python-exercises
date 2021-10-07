def is_two(num):
    if num == 2 or num == "2":
        return True
    return False

def is_vowel(char):
    if char in "aeiou":
        return True
    return False

def is_consonant(char2):
    if is_vowel(char2) == True:
        return False
    elif is_vowel(char2) == False and char2.isalpha():
        return True
    pass

def capitalize(string):
    if is_consonant(string[0]):
        if len(string.split()) > 1:
            return string.split(" ", 1)[0].capitalize() + " " + string.split(" ", 1)[1]
        else:
            return string.split(" ", 1)[0].capitalize()
    else:
        return string

def calculate_tip(pct, invoice):
    return pct * invoice

def apply_discount(price, discount):
    return price - (price * discount)

def handle_commas(num1):
    num2 = ""
    if "," in num1:
        for num in num1:
            if num != ',':
                num2 += num
    return num2

def get_letter_grade(score):
    grade = ""
    if 100 >= score >= 90:
        grade = "A"
    elif 90 > score >= 80:
        grade = "B"
    elif 80 > score>= 70:
        grade = "C"
    elif 70 > score >= 60:
        grade = "D"
    elif score < 60:
        grade = "F"
    return(grade)

def remove_vowels(string):
    string2 = ""
    for char in string:
        if char not in 'aeiou':
            string2 += char
    return string2

def normalize_name(string):
    string2 = ''
    string = string.strip()
    for char in string:
        if char.isnumeric():
            string2 += char
        elif char.isalpha():
            string2 += char.lower()
        elif char == " ":
            string2 += "_"
    return string2

def cumulative_sum(lst1):
    lst2 = []
    total = 0
    for num in lst1:
        total += num
        lst2.append(total)
    return lst2




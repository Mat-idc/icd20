#homework 1

'''l = float(input("Please enter length"))
w = float(input("Please enter width"))

def area_of_rectangle(length, width):
    if isinstance(length, (int, float)) and isinstance(width, (int, float)):
        return length * width
    else:
        return "Invalid input. Please provide numeric values for length and width."
print(f"{area_of_rectangle(l,w)}")

#homework 2

str = input("Please Enter string:")
substr = input("Please Enter a substring:")

def contains_substring(string, substring):
    if isinstance(string, str) and isinstance(substring, str):
        return substring in string
    else:
        return "Invalid input. Please provide two strings."
print(contains_substring(h,e))

#homework 3

num1 = float(input("Please Enter #1:"))
num2 = float(input("Please Enter #2:"))
num3 = float(input("Please Enter #3:"))

def average_of_three_floats(num1, num2, num3):
    if all(isinstance(x, float) for x in [num1, num2, num3]):
        return (num1 + num2 + num3) / 3.0
    else:
        return "Invalid input. Please provide three floating-point numbers."

print(average_of_three_floats(num1, num2, num3))

#homework 4

str1 = input("Please Enter String 1:")
str2 = input("Please Enter String 2:")

def concatenate_strings(str1, str2):
    if isinstance(str1, str) and isinstance(str2, str):
        return str1 + str2
print(concatenate_strings(str1, str2))

#homework 5 *won't round

sl = float(input("Please Enter the side length of a cube:"))
def volume_of_cube(side_length):
    if isinstance(side_length, (int, float)):
        return side_length ** 3
print(volume_of_cube(round(sl,2)))

# homework 6

num = float(input("Please enter a number:"))
def check_number_status(number):
    if isinstance(number, (int, float)):
        if number > 0:
            return "Positive"
        elif number < 0:
            return "Negative"
        else:
            return "Zero"
print(check_number_status(num))

# homework 7 *won't round

r = float(input("Please Enter Radius:"))
def circumference_of_circle(radius):
    if isinstance(radius, (int, float)):
        return 2 * 3.141592653589793 * radius
print(circumference_of_circle(round(r,2)))

#homework 8 *won't print

str = str(input("Please Enter a String:"))
char = str(input("Please Enter a Character:"))

def count_char_occurrences(string, char):
    if isinstance(string, str) and isinstance(char, str) and len(char) == 1:
        return string.count(char)
print(count_char_occurrences(char, str))'''

#homework 9 *don't know how to round

n = float(input("Please Enter a Number:"))
p = float(input("Plesase Enter a Percentage %:"))

def calculate_percentage(number, percentage):
    if isinstance(number, (int, float)) and isinstance(percentage, (int, float)):
        return (percentage / 100) * number
print(calculate_percentage(n,p))

#homework 10

n1 = float(input("Enter Number 1:"))
n2 = float(input("Enter Number 2"))

def absolute_difference(num1, num2):
    if all(isinstance(x, (int, float)) for x in [num1, num2]):
        return abs(num1 - num2)
print(absolute_difference(n1,n2))

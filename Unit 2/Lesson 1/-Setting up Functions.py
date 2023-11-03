#function to calculate area of rectangle
def area_of_rectangle(l,w):

    if isinstance(l, (int,float)) and isinstance(w, (int, float)):
         return (l*w)
    else:
         print("invalid input: please provide numeric values")

#function to get a substring
def contains_substring(s, ss):
     s = str(s)
     ss = str(ss)
     return ss in s

#function to calculate average of 3 numbers
def average_of_numbers (n1, n2, n3):
     if all(isinstance(n1, (int, float)) for x in [n1, n2, n3]):
          return (n1+n2+n3)/3
     else:
          print(f"Invalid input. Please proide numeric values")

 
#function to calculate concatenate strigns
def concatenate_strings(str1, str2):
     if isinstance(str1, str) and isinstance(str2, str):
          return str1+str2

#function to calculate volume of cube
def volume_of_cube(side_length):
     if isinstance(side_legnth):
          return side_length**3
     
#function to check if a number is positive or negative or zero
def check_number_status(number):
     if isinstance(number, (int, float)):
          if number>0:
               return "Positive"
          elif number < 0:
               return "Negative"
          else:
              return "Zero"
          
#function to calculate the circumfrence of a circle
def circumfrence_of_circle(radius):
     if isinstance(radius, (int, float)):
          return 2 * 3.141592653589793 * radius
     
#function to count the number of occurences of a chracter in a string
def count_char_occurences(string, char):
     if isinstance(string, str) and isinstance(char, str) and len(char) ==1:
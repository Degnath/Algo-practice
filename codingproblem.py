# 1 Write a program to check wheather a string contain all the alphabets(take input from a user)

# alphabet = set(string.ascii_lowercase)
# input_string = 'The quick brown fox jumps over the lazy dog'
# print(set(input_string.lower()) >= alphabet)
# input_string = 'The quick brown fox jumps over the lazy cat'
# print(set(input_string.lower()) >= alphabet)
string = input("enter the any input: ")
condition = True
for x in string:
    if not x.isalpha():
        condition = False
        break
if not condition:
    print("give string does not have all alphabet")
else:
    print("given string has all alphabet.")


# 2 Writer a program to count number of vowels in a string
sentence = 'i have been doing this for a years one'
string = sentence.lower()
count = 0
list = ['a', 'e', 'i', 'o', 'u']
for char in string:
    if char in list:
        count = count + 1
print('number of vowels in given string is: ', count)

# 3. Writer a program to check if it is a vowel or not

ch = input("enter a character: ")

if(ch == 'a' or ch == 'e' or ch == 'i' or ch == 'o' or ch == 'u' or ch == 'A' or ch == 'E' or ch == 'I' or ch == 'O' or ch == 'U'):
    print("The Given Character ", ch, "is a Vowel")
else:
    print("The Given Character ", ch, "is a Consonant")

# 4. Write a program if a year is a leap or not
Year = 2000
if(Year % 400 == 0):
    print(Year, "is a leap year")
elif(Year % 4 == 0 and Year % 100 != 0):
    print(Year, " is leap year")
else:
    print(Year, 'is not a leap year')

# 5. WAP to swap two number without using temporary variable

x = 20
y = 10
# befor swaping
print("Value of x: ", x, "and y: ", y)
x, y = y, x
# after swaping
print("Value of x: ", x, "and y: ", y)

# 6. WAP to print the product of two variables
a = 10
b = 15
product = a * b
print(product)

# 7. Writer a program to print wheather a number is divisible by 9 and multiple of 6

# def multiple(m, n):
#     return True if m % n == 0 else False


# print(multiple(18, 12))

def divisible(m, n):
    if(m % 9 == 0 and n % 6 == 0):
        return True
    else:
        return False


print(divisible(90, 24))

# 8. Write a pseudocode to take 5 values from users and print their average using while loop(take input from the user)
# list = [4, 5, 6, 8, 9]
# num_of_list = sum(list)
# print(num_of_list)
# len_of_list = len(list)
# average = num_of_list/len_of_list
# print(average)

# list = [3, 5, 6, 9, 9]
# sum = 0
# index = 0
# while index < len(list):
#     sum = sum + list[index]-list[0]
#     index += 1
# print(sum/len(list))

sum = 0
for num in range(5):
    number = int(input("Enter a number: "))
    sum = sum + number
average = sum/5
print("Average of the number is: ", average)
# 9. Writer a program to print Armstrong number in the interval from 100 to 2000
for number in range(100, 2000):
    sum = 0
    temp = number
    while temp > 0:
        digit = temp % 10
        sum += digit ** 3
        temp //= 10
    if sum == number:
        print(number)


# 10. Write a program to remove punctuations from a string (take a string containing punctuations as an input from user)
punctuations = '''!()-[]{};:'"\,<>./?@#$%^&*_~'''

str = "Hello!, he said, --and went to $$$."

# To take input from the user
# str = input("Enter a string: ")

# remove punctuation from the string
no_punct = ""
for char in str:
    if char not in punctuations:
        no_punct = no_punct + char

# display the unpunctuated string
print(no_punct)

# 11. Write a program to remove punctuations from a string (take a string containing punctuations as an input from user)</b>
number = int(input("Enter a number: "))
if(number % 2 == 0):
    print("even number")
else:
    print("odd number")

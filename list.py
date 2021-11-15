# List and Dictionary Comprehension
# using list comprehensiin to create RGB colors
import random  # random is one of the inbuilt module, randon is imported to get randon RGB number
R, G, B = [random.randint(0, 255) for value in range(0, 3)]
print(R)
print(G)
print(B)

sent = 'This is a randow sentence'
sent_words = sent.split()
sent_words_upper = [word.upper() for word in sent_words]
print(sent_words_upper)

# Dictionary Comprehension
# create dict from the user input number is key and square of number is value

square_dict = {}  # it can be square_dict = dict()
for num in range(1, 11):
    square_dict[num] = num*num

# print(square_dict)

# using Dict comprehension
dict_sqares = {num: num*num for num in range(1, 11)}
# print(dict_sqares)

# conditional
d_square = {n: n * n for n in range(1, 11) if n % 2 == 0}
print(d_square)

# word occurance
sent1 = 'Flask is a web framework that provides libraries to build lightweight web applications in python is that i.'
word_count = {word: sent1.lower().split().count(word)
              for word in sent1.lower().split() if word in set(sent1.lower().split())}
# print(word_count)

# conversion
price_in_dollar = {'milk': 3, 'sugar': 2, 'bread': 2, 'coke': 3}
dollor_to_pound = 0.75
price_in_pounds = {product: value*0.75 for (product, value) in price_in_dollar}
# print(price_in_pounds)

#Copy: Shallow and Deepcopy

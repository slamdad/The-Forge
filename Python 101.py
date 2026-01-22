# #   # x = 1    # int
# #   # y = 2.8  # float
# #   # z = 1j   # complex

# #   # #convert from int to float:
# #   # a = float(x)

# #   # #convert from float to int:
# #   # b = int(y)

# #   # #convert from int to complex:
# #   # c = complex(x)

# #   # print(a)
# #   # print(b)
# #   # print(c)

# #   # print(type(a))
# #   # print(type(b))
# #   # print(type(c))

# # # import random

# # # print(random.randrange(1, 10))


# # # import random
# # # random.seed(42)
# # # print([random.randrange(1,10) for _ in range(5)]

# # print("It's alright")
# # print("He is called 'Johnny'")
# # print('He is called "Johnny"')

# # a = """Lorem ipsum dolor sit amet,
# # consectetur adipiscing elit,
# # sed do eiusmod tempor incididunt
# # ut labore et dolore magna aliqua."""
# # print(a)

# a = "Hello, World!"
# print(a[0])

# for x in "banana":
#   print(x)

# for d in "Slamdad":
#   print(d)
  
# a = "Hello, World!"
# print(len(a))
# txt = "The best things in life are free!"
# print("free" in txt)




# txt = "The best things in life are free!"
# if "free" in txt:
#   print("Yes, 'free' is present.")

 
# txt = "The best things in life are free!"
# print("expensive" not in txt)


# txt = "The best things in life are free!"
# if "expensive" not in txt:
#   print("No, 'expensive' is NOT present.")

# b = "Hello, World!"
# print(b[2:5])

# b = "Hello, World!"
# print(b[-5:-2])

# b = "Hello, World!"
# print(b[-5:-2])

# a = "Hello, World!"
# print(a.upper())

# a = "Hello, World!"
# print(a.lower())

# a = "   Hello, World! "
# print(a.strip())

# a = "Hello, World!"
# print(a.replace("H", "J"))

# a = "Hello, World!"
# print(a.split(",")) 

# a = "Hello"
# b = "World"
# c = a + b
# print(c)

# a = "Hello"
# b = "World"
# c = a + " " + b
# print(c)


# age = 36
# #This will produce an error:
# txt = f"My name is John, I am {age}"
# print(txt)

# price = 59
# txt = f"The price is {price} dollars"
# print(txt)

# price = 59
# txt = f"The price is {price:.2f} dollars"
# print(txt)

# txt = f"The price is {20 * 59} dollars"
# print(txt)

# txt = "We are the so-called \"Vikings\" from the north."
# print(txt)

# txt = "hello, and welcome to my world."
# x = txt.capitalize()
# print (x)

# txt = "python is FUN!"
# x = txt.capitalize()
# print (x)

# txt = "banana"
# x = txt.center(20)
# print(x)

# txt = "My name is Ståle"
# x = txt.encode()
# print(x)

#!/bin/python3

import math
import os
import random
import re
import sys



if __name__ == '__main__':
    n = int(input().strip())

if n % 2 == 1:
    print("weird")
else:
    if 2 <= n <= 5:
        print("Not Weird")
    elif 6 <= n <= 20:
        print("Weird")
    else:
        print("Not Weird")
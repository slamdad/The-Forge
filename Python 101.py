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

# import math
# import os
# import random
# import re
# import sys



# if __name__ == '__main__':
#     n = int(input().strip())

# if n % 2 == 1:
#     print("weird")
# else:
#     if 2 <= n <= 5:
#         print("Not Weird")
#     elif 6 <= n <= 20:
#         print("Weird")
#     else:
#         print("Not Weird")


# print(10 > 9)
# print(10 == 9)
# print(10 < 9)


# a = 200
# b = 33

# if b > a:
#   print("b is greater than a")
# else:
#   print("b is not greater than a")

# print(bool("Hello"))
# print(bool(15))
# x = "Hello"
# y = 15

# print(bool(x))
# print(bool(y))

# bool("abc")
# bool(123)
# bool(["apple", "cherry", "banana"])

# class myclass():
#   def __len__(self):
#     return 0

# myobj = myclass()
# print(bool(myobj))



# def myFunction():
#     return True
# print(myFunction())


# def myFunction() :
#   return True

# if myFunction():
#   print("YES!")
# else:
#   print("NO!")

# x = 15
# y = 4

# print(x + y)
# print(x - y)
# print(x * y)
# print(x / y)
# print(x % y)
# print(x ** y)
# print(x // y)

# numbers = [1, 2, 3, 4, 5]
# count = len(numbers)
# if count > 3:
#     print(f"List has {count} elements")

# if (count := len(numbers)) > 3:
#     print(f"List has {count} elements")

# x = 5

# print(1 < x < 10)

# print(1 < x and x < 10)
# x = 5

# # print(x > 0 and x < 10
# x = ["apple", "banana"]
# y = ["apple", "banana"]
# z = x

# print(x is z)
# print(x is y)
# print(x == y)

# x = ["apple", "banana"]
# y = ["apple", "banana"]

# print(x is not y)


# fruits = ["apple", "banana", "cherry"]

# print("banana" not in fruits)


# def is_leap(year):
    
#     if year % 400 == 0:
#         return True
#     elif year % 100 == 0:
#         return False
#     elif year % 4 == 0:
#         return True

#     else:
#         return False

# year = int(input())
# print(is_leap(year))


# thislist = ["apple", "banana", "cherry", "apple", "cherry"]
# print(thislist)
# thislist = ["apple", "banana", "cherry"]
# print(len(thislist))

# list1 = ["apple", "banana", "cherry"]
# list2 = [1, 5, 7, 9, 3]
# list3 = [True, False, False]

# thislist = list(("apple", "banana", "cherry")) # note the double round-brackets
# print(thislist)

# thislist = ["apple", "banana", "cherry"]
# print(thislist[-1])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:5])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[:4])

# thislist = ["apple", "banana", "cherry", "orange", "kiwi", "melon", "mango"]
# print(thislist[2:])

# thislist = ["apple", "banana", "cherry"]
# if "apple" in thislist:
#   print("Yes, 'apple' is in the fruits list")



# thislist = ["apple", "banana", "cherry"]
# thislist[1:2] = ["blackcurrant", "watermelon"]
# print(thislist) 

# thislist = ["apple", "banana", "cherry"]
# thislist[1:3] = ["watermelon"]
# print(thislist)

# i = 1
# while i < 6:
#   print(i)
#   i += 1

#   i = 1
# while i < 6:
#   print(i)
#   if i == 3:
#     break
#   i += 1


# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   print(x)
#   if x == "banana":
#     break
  
# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     break
# #   print(x)

# fruits = ["apple", "banana", "cherry"]
# for x in fruits:
#   if x == "banana":
#     continue
#   print(x)

# for x in range(2, 30, 3):
# #   print(x)

# for x in range(6):
#   print(x)
# else:
#   print("Finally finished!")

# mytuple = ("apple", "banana", "cherry")
# myit = iter(mytuple)

# print(next(myit))
# print(next(myit))
# print(next(myit))

# mystr = "banana"
# myit = iter(mystr)

# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# print(next(myit))
# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     x = self.a
#     self.a += 1
#     return x

# myclass = MyNumbers()
# myiter = iter(myclass)

# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))
# print(next(myiter))

# class MyNumbers:
#   def __iter__(self):
#     self.a = 1
#     return self

#   def __next__(self):
#     if self.a <= 20:
#       x = self.a
#       self.a += 1
#       return x
#     else:
#       raise StopIteration

# myclass = MyNumbers()
# myiter = iter(myclass)

# for x in myiter:
#   print(x)
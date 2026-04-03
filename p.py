# python3 p.py

# printing statement print(f"hello")

# name = int(input("enter no.of elements: ", name))

# Even Odd
# x = int(input("Enter number: "))
# if x%2==0:
#     print("Even")
# elif x==0:
#     print("Zero")
# else:
#     print("Odd")


# def is_prime(num):
#     if num <= 1:
#         return False
#     for i in range(2, int(num ** 0.5) + 1):
#         if num % i == 0:
#             return False
#     return True
# num = int(input("Enter number: "))
# result = is_prime(num)
# if result:
#     print("prime")
# else:
#     print("not prime")


# num = int(input("Enter number: "))
# count = 0
# rem = 0

# if num == 0:
#     print(1)
# else:
#     n = num
#     while n > 0:
#         rem = n % 10
#         count += 1
#         n = n // 10
#     print(count)


# num = int(input("Enter a number: "))
# def rev(num):
#     rev=0
#     while(num!=0):
#         rem = num%10
#         rev = rev * 10 + rem
#         num //= 10
#     return rev
# result = rev(num)
# print(result)


# num = int(input("Enter a number: "))
# def digit_sum(n):
#     if n == 0:
#         return 0
#     elif n < 0:
#         print("Negative numbers not supported!")
#         return None
#     else:
#         summation = 0
#         while n != 0:
#             rem = n % 10
#             summation += rem
#             n //= 10
#         return summation

# result = digit_sum(num)
# if result is not None:
#     print(result)

# def add(a, b):
#     return a+b
# result = add(3, 5)
# print(result)

# def add():
#     x,y = int(input("Enter x and y: "))
#     print(f"x={x} y={y}")
# add()

# def square(n):
#     return n*n
# result = square(8)
# print(result)
# a = square(9)
# print(a)

# keyword arguments
# display(age=20, name="ravi")

# default arguments
# def greet(name="guest"):
#     print("hello", name)
# greet()
# greet("anil")

# variable length arguments
# non keyword argumnets
# def total(*numbers):
#     return sum(numbers)
# print(total(1,3,4,5,6,7,3,8,9))

# y= lambda x: x*x*x*x
# print(y(2))

# def process(data):
#     match data:
#     case[x,y]:
#         print(f"two-elements list: {x} {y}")
#     case[x,y,z]:
#         print(f"three-elements list: {x} {y}")
#     case_:
#         print("unknown data format")
# process([1,2])
# process([1,2,3])
# process([1,2,3,4])

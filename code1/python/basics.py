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


num = int(input("Enter a number: "))

def digit_sum(n):
    if n == 0:
        return 0
    elif n < 0:
        print("Negative numbers not supported!")
        return None
    else:
        summation = 0
        while n != 0:
            rem = n % 10
            summation += rem
            n //= 10
        return summation

result = digit_sum(num)
if result is not None:
    print(result)
import random
import time

list1 = [random.randint(1, 100) for i in range(10)]
list2 = [random.randint(1, 100) for i in range(10)]

# find the common numbers
COMMON_NUMBERS = [num for num in list1 if num in list2]
if not COMMON_NUMBERS:
    COMMON_NUMBERS = []

# find the odd and even numbers
ODD_NUMBERS1 = [num for num in list1 if num % 2 == 1]
if not ODD_NUMBERS1:
    ODD_NUMBERS1 = []

ODD_NUMBERS2 = [num for num in list2 if num % 2 == 1]
if not ODD_NUMBERS2:
    ODD_NUMBERS2 = []

EVEN_NUMBERS1 = [num for num in list1 if num % 2 == 0]
if not EVEN_NUMBERS1:
    EVEN_NUMBERS1 = []

EVEN_NUMBERS2 = [num for num in list2 if num % 2 == 0]
if not EVEN_NUMBERS2:
    EVEN_NUMBERS2 = []

# find the prime numbers
PRIME_NUMBERS1 = []
for num in list1:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            PRIME_NUMBERS1.append(num)

if not PRIME_NUMBERS1:
    PRIME_NUMBERS1 = []

PRIME_NUMBERS2 = []
for num in list2:
    if num > 1:
        for i in range(2, num):
            if num % i == 0:
                break
        else:
            PRIME_NUMBERS2.append(num)

if not PRIME_NUMBERS2:
    PRIME_NUMBERS2 = []

full_check = int(0)

print("This program will generate two random lists and give you information about them.")
time.sleep(2)
# establish a while loop so I can give the option for more steps
while True:
    print(f"List one contains:\n{list1}\n\nand list two contains:\n{list2}\n\n")
    time.sleep(2)
    print("The common numbers in these lists are:")
    time.sleep(1)
    print(COMMON_NUMBERS)
    odd_and_even = input("Would you like to know the odd and even numbers in list 1 and 2? (y/n): ")
    if odd_and_even == 'y':
        print("The even numbers in list one were:")
        time.sleep(1)
        print(EVEN_NUMBERS1)
        time.sleep(2)
        print("The even numbers in list two were:")
        time.sleep(1)
        print(EVEN_NUMBERS2)
        time.sleep(2)
        print("The odd numbers in list one were:")
        time.sleep(1)
        print(ODD_NUMBERS1)
        time.sleep(2)
        print("The odd numbers in list two were:")
        time.sleep(1)
        print(ODD_NUMBERS2)
        time.sleep(2)
        prime_numbers = input("Would you like to know if there are any prime numbers in list one and two?(y/n): ")
        if prime_numbers == 'y':
            print("The prime numbers in list one are:")
            time.sleep(1)
            print(PRIME_NUMBERS1)
            time.sleep(2)
            print("\nThe prime numbers in list two are: ")
            time.sleep(1)
            print(PRIME_NUMBERS2)
            time.sleep(2)
            full_check += 1
            print(full_check)
            break
        else:
            break
    else:
        break

if full_check == 1:
    print("Thank you for using this program! You've used everything I can offer.")
else:
    print("Thank's for using me!")

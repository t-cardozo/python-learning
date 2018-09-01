numbers = ['one', 'two', 'three', 'four', 'five']

#FOR LOOPS:

# for number in numbers:
#     print(number)

# for number in numbers[1:3]:
#     print(number)

# for number in numbers:
#     if number == numbers[3]:
#         print(f'{number} - selected')
#     else:
#         print(number)

#WHILE LOOPS:

age = 25
num = 0

while num < age:
    if num % 2 == 0:
        print(num)
    if num > 10:
        break
    num += 1
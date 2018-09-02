ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name:')
    ninja_belt = input('enter belt color')
    ninja_belt[ninja_name] = ninja_belt

    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break
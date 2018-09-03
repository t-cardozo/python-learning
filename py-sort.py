# def ninja_intro(dictionary):
#     for key, val in dictionary.items():
#           print(f'I am {key} and i am a {val} belt')

def ninja_belt_count(dictionary):
    belts = list(dictionary.values())
    for belt in set(belts):
        num = belts.count(belt)
        print(f'There are {num} {belt}')


ninja_belts = {}

while True:
    ninja_name = input('enter a ninja name:')
    ninja_belt = input('enter belt color')
    ninja_belts[ninja_name] = ninja_belt

    another = input('add another? (y/n)')
    if another == 'y':
        continue
    else:
        break
    
ninja_belt_count(ninja_belts)
    

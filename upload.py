from random import choice
Map = {
    'hot': [hot for hot in range(76, 91)],
    'warm': [warm for warm in range(41, 76)],
    'cold': [cold for cold in range(0, 41)],
}
while True:
    temperature = input('temperature range ')
    if temperature not in Map:
        print(f'error, type in {Map.keys()}')
    else:
        print(f'The temperature for {temperature} is {choice(Map[temperature])}F')
        break


        

    
    
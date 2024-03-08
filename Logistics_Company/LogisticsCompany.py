print('Welcome to Logistics Company')

def object_dimensions():
    while True:
        try:
            length = float(input('\nEnter length of object (in cm): '))
            width = float(input('Enter width of object (in cm): '))
            height = float(input('Enter height of object (in cm): '))
            volume = length * width * height
            print('The volume of object is (in cm³): {}' .format(volume))
            
            if volume >= 100000:
                print('\nWe do not accept objects with volume that exceed 100000.\n'
                        'Enter dimensions again.')
                continue
            break
        except ValueError:
            print('\nYou enter some dimension of object with a non-numeric value.\n'
                    'Please, enter dimensions again.')

    if volume < 1000:
        value = 10
    elif volume >= 1000  and volume < 10000:
        value = 20
    elif volume >= 10000 and volume < 30000:
        value = 30
    elif volume >= 30000 and volume < 100000:
        value = 50
    return value

def object_weight():
    while True:
        try:
            weight = float(input('\nEnter weight of object (in kg): '))
            if weight >= 30:
                print('\nWe do not accept such heavy objects.\n'
                        'Enter weight again.')
                continue
            break
        except ValueError:
            print('\nYou enter weight of the object with non-numeric value.\n'
                    'Please, enter weight again.')

    if weight < 0.1:
        multiplier = 1
    elif weight >= 0.1 and weight < 1:
        multiplier = 1.5
    elif weight >= 1 and weight < 10:
        multiplier = 2
    elif weight >= 10 and weight < 30:
        multiplier = 3
    return multiplier

def object_route():
    acronyms = ['RS', 'SR', 'BS', 'SB', 'BR', 'RB']
    while True:
        print('\nSelect the route:')
        print('RS - Rio de Janeiro to São Paulo \n'
              'SR - São Paulo to Rio de Janeiro \n'
              'BS - Brasília to São Paulo \n'
              'SB - São Paulo to Brasília \n'
              'BR - Brasília to Rio de Janeiro \n'
              'RB - Rio de Janeiro to Brasília')
        route = input('>> ').upper()
        if route not in acronyms:
            print('You enter non-existing route. \n'
                    'Please, enter route again.')
        else:
            break

    if route == 'RS' or route == 'SR':
        multiplier = 1
    elif route == 'BS' or route == 'SB':
        multiplier = 1.2
    elif route == 'BR' or route == 'RB':
        multiplier = 1.5
    return multiplier


if __name__ == '__main__':
    dimension = object_dimensions()
    weight = object_weight()
    route = object_route()
    total = dimension * weight * route
    print('Final price: R${:.2f} (dimension: {} * weight: {} * route: {})' .format(total, dimension, weight, route))
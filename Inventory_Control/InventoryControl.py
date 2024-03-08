print('Welcome to Inventory Control')
register = []
register_count = 0

def piece_register():
    global register_count
    piece = {} 
    piece['cod'] = register_count + 1
    register_count = piece['cod']
    print('Code of piece {}' .format(piece['cod']))
    piece['name'] = input('Enter name of piece: ')
    piece['manufacturer'] = input('Enter manufacturer of piece: ')
    piece['price'] = float(input('Enter price(R$) of piece: '))
    register.append(piece)

def piece_query():
    while True:
        try:
            print('Select the option:\n'
                  '1 - Query all pieces\n'
                  '2 - Query pieces by code\n'
                  '3 - Query pieces by manufacturer\n'
                  '4 - Return')
            op = int(input('>> '))
            if op >= 5: 
                print('Invalid option!')
                continue
        except ValueError:
            print('You entered non-numeric value\n'
                    'Try again!')
        if op == 1:
            for item in register:
                print('Code: {}' .format(item['cod']))
                print('Name: {}' .format(item['name']))
                print('Manufacturer: {}'.format(item['manufacturer']))
                print('Price: R${:.2f}'.format(item['price']))
                print('-' * 10)
        if op == 2:
            code = int(input('Enter code of piece: '))
            for item in register:
                if code == item['cod']:
                    print('Code: {}'.format(item['cod']))
                    print('Name: {}'.format(item['name']))
                    print('Manufacturer: {}'.format(item['manufacturer']))
                    print('Price: R${:.2f}'.format(item['price']))
                    print('-' * 10)
                    break
        elif op == 3:
            manufacturer = input('Enter manufacturer of piece: ')
            for item in register:
                if manufacturer == item['manufacturer']:
                    print('Code: {}'.format(item['cod']))
                    print('Name: {}'.format(item['name']))
                    print('Manufacturer: {}'.format(item['manufacturer']))
                    print('Price: R${:.2f}'.format(item['price']))
                    print('-' * 10)
        elif op == 4:
            break

def piece_remove():
    print('You selected remove piece option')
    cod = int(input('Enter code of piece for remove: '))
    find = False
    for item in register:
        if cod == item['cod']:
            register.remove(item)
            find = True 
    if not find:
        print('Code non-exist')

while True:
    try: 
        print('Select a option:')
        print('1 - Register piece\n'
              '2 - Query piece\n'
              '3 - Remove piece\n'
              '4 - Exit')
        option = int(input('>> '))
        if option >= 5:
            print('Invalid option!')
            continue
    except ValueError:
        print('You enter a non-numeric value.\nTry again!')
    if option == 1:
        piece_register()
    elif option == 2:
        piece_query()
    elif option == 3:
        piece_remove()
    elif option == 4:
        break
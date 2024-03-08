print('Restaurant')

def entry(s1):
    print('*' * 15, s1, '*' * 15)

def cardapio(itens):
    max_size = 0
    for item in itens:
        size = len(item['desc'])
        if size > max_size:
            max_size = size
    for item in itens:
        padding = len(str(item['cod'])) + 4
        print('|', item['cod'], '|', item['desc'].center(max_size + padding), '|', str(item['value']).rjust(4), '|')

itens_list = [
    {'cod': 100, 'desc': 'HotDog', 'value': 9.00},
    {'cod': 101, 'desc': 'Cheeseburger', 'value': 11.00},
    {'cod': 102, 'desc': 'Sandwich', 'value': 12.00},
    {'cod': 103, 'desc': 'Cake', 'value': 13.00},
    {'cod': 104, 'desc': 'Ice Cream', 'value': 14.00},
    {'cod': 105, 'desc': 'Orange Juice', 'value': 17.00},
    {'cod': 200, 'desc': 'Soda', 'value': 5.00},
    {'cod': 201, 'desc': 'Iced Tea', 'value': 4.00}
]
order = [] 
total = 0.0

entry('Menu')
cardapio(itens_list)

while True:
    product = int(input('\nEnter the code: '))
    find = False

    for item in itens_list:
        if item['cod'] == product:
            order.append(item)
            print('You ordered a {} worth R${:.2f}' .format(item['desc'], item['value']))
            find = True
            break

    if not find:
        print('Invalid option!')
        continue

    while True:
        order_final = int(input('Do you want anything else? \n 1 - Yes \n 0 - No \n >> '))
        if order_final == 0:
            break
        elif order_final == 1:
            break
        else:
            print('Invalid option!')
    if order_final == 0:
        break

for item in order:
    total += item['value']
print('Final price: R${:.2f}' .format(total))




print('Welcome to the Store')

try:
    price = float(input('Enter the price of the product: '))
    amount = int(input('Enter the amount desired: '))
except ValueError:
    print('You entered non-numeric value\n')
    exit()

if(amount <= 9):
    total = price * amount
    print('Total price is: R${:.2f}' .format(total))

elif((amount >= 10) and (amount <= 99)):
    total = price * amount
    discount = total * 0.95
    print('Price without discount is: R${:.2f}'.format(total))
    print('Price with discount is: R${:.2f}  (5% off)'.format(discount))

elif((amount >= 100) and (amount <= 999)):
    total = price * amount
    discount = total * 0.90
    print('Price without discount is: R${:.2f}'.format(total))
    print('Price with discount is: R${:.2f}  (10% off)'.format(discount))
    
else:
    total = price * amount
    discount = total * 0.85
    print('Price without discount is: R${:.2f}'.format(total))
    print('Price with discount is: R${:.2f}  (15% off)'.format(discount))

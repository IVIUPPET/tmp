purchase_price = 135e3

inflation_rate = 2

num_years = 6

def financialPrint(numerical_string):
	print('$ ' +  '{:0.2f}'.format(numerical_string))

## Print report:
print('Initial value:')
financialPrint(purchase_price)
print('\n')

for i in range(num_years):
	purchase_price = (purchase_price*(inflation_rate/100+1))
	financialPrint(purchase_price)

# TODO: add interest rate calculation from current and future value

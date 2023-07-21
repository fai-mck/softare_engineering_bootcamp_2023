# This program uses lists and dictionaries to calculate the 
# total value of each item of stock available in store and then the total value of stock available in the store.

menu = ['coffee', 'tea', 'sandwich', 'bagel', 'smoothie']
stock = {'coffee':5, 'tea':10, 'sandwich':25, 'bagel':20, 'smoothie':10}
price = {'coffee':3.50, 'tea':2, 'sandwich':3.50, 'bagel':4, 'smoothie':4}
total_stock = 0

# Iterate the dictionaries over the menu list to calculate the item_value of each item in the menu list.
# ' : .2f ' is used to round off the item_value answers to two decimal places.
for item in menu:
    item_stock = stock[item]
    item_price = price[item]
    item_value = stock[item] * price[item]
    total_stock += item_value
    print(f'{item.capitalize()}: {item_stock} x {item_price: .2f} = {item_value: .2f}')

print(f'The total stock value in the cafe is: {total_stock: .2f} GBP')














mug = 75
coffee_bag = 150

amount_mugs = int(input('How many mugs? '))
amount_coffee_bag = int(input('How many coffee bags? '))

total_mugs_weight = amount_mugs * amount_mugs
total_coffee_bag_weight = amount_coffee_bag * coffee_bag

total_weight = total_mugs_weight + total_coffee_bag_weight

print(f'''
The total weight of the products are...
Mug {total_mugs_weight} gr
Coffee {total_coffee_bag_weight} gr
All {total_weight} gr
''')
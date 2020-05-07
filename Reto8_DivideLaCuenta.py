if __name__ == "__main__":
    bill = round(float(input('How much did you consume? ')), 2)
    tip = float(input('What percentage of tip will you give? '))
    tax = float(input('What is the taxt percentage in your city? '))
    persons = int(input('How much people are paying? '))

    tip_percentage = tip / 100
    tax_percentage = tax / 100

    net_total = bill + (bill * tip_percentage)
    net_total = net_total + (net_total * tax_percentage)
    total_by_person = net_total / persons

    print(f'\nThe total to pay is ${net_total}') 
    print(f'Each person will have to pay ${total_by_person}')

savings = float(input('How much are your savings? '))
interest_rate = int(input('What is your interest rate? ')) / 100
years_saved = int(input('How many years have passed? '))
print(interest_rate)

for years in range(years_saved):
    end_of_year = savings * (interest_rate)
    savings += end_of_year

print(f'Your balance with an interest rate of {interest_rate * 100}% is {end_of_year}')
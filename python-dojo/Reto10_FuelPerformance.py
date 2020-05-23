if __name__ == "__main__":
    us_gallon = 3.79 #lt
    uk_gallon = 4.55 #lt
    mile = 1.6034 #km

    distance = float(input('What is the distance traveled? '))

    lts_to_us_gallon = 1/us_gallon
    lts_to_uk_gallon = 1/uk_gallon
    us_gallon_performance = lts_to_us_gallon/distance
    uk_gallon_performance = lts_to_uk_gallon/distance

    print(f'The performance for US Gallons is: {us_gallon_performance} km/lt)')
    print(f'The performance for UK Gallons is: {uk_gallon_performance} km/lt)')
    
    
    #galones imperiales
    #lts/100Km = 282.48 / millas por galón
    #lts/100Km = 282.48 / 24 = 11.77

    #galones estadounidenses
    #lts/100Km = 235.21 / millas por galón
    #lts/100Km = 235.21 / 24 = 9.8 

    #millas / 1 galón = 1.60934 Km / 1 milla
    #24 millas / 1 galón = 1.60934 Km / 1 milla = 38.616Km / galón

    #UK Gallon
    #38.616 Km / 1 galón = 1 / 4.55 lt = 38.616 km / 4.55 lt
    #4.55 lt / 38.616 km

    #US Gallon
    #38.616 km / 1 gallon = 1 gallon / 3.79 lt = 38.616 km / 3.79 lt
    #3.79 lt / 38.616 km
    #0.098 lt/km

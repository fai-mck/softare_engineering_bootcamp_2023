# This program makes use of defining functions to calculate a users holiday cost including
# plane cost, hotel cost and car rental cost.

print("Welcome to the holiday calculator page. Here you will be able to calculate the total cost of your intended holiday.")

print('''Our flights depart from four major cities only, namely Cape Town, 
         Durban, Johannesburg and Port Elizabeth. When inputting your departure
         and arrival cities, please use the following abbreviations.
         Cape Town      = CPT
         Johannesburg   = JHB
         Durban         = DBN
         Port Elizabeth = PE
         N.B. All costs are for a one way flight only.''')

city_flight = ""

while True:
    city_flight_departure = input('Please input your departure airport: ').upper()
    city_flight_arrival = input('Please input your arrival airport: ').upper()

    if city_flight_departure not in ['CPT','JHB','DBN','PE'] or city_flight_arrival not in ['CPT','JHB','DBN','PE']:
        print('This route is not offered. Please select a different route.')
        continue
    elif city_flight_departure == city_flight_arrival:
        print('You have made a mistake. Please try again')
        continue
    else:
        break

pax = int(input('How many passengers will be flying? '))

num_nights = int(input('How many nights will you be staying in the city? '))

rental = input('Do you require car rental? (y/n) ').lower()

if rental == 'y':
    rental_days = int(input('How many days do you need to rent the car for? '))
else:
    print()
    print('You have opted to not hire a car.')
    rental_days = 0

def hotel_cost(num_nights):
    return num_nights * 1200

def plane_cost(city_flight):
        
        if city_flight_departure == 'JHB' and city_flight_arrival == 'CPT' or city_flight_departure == 'CPT' and city_flight_arrival == 'JHB':
            city_flight = 800
        elif city_flight_departure == 'JHB' and city_flight_arrival == 'DBN' or city_flight_departure == 'DBN' and city_flight_arrival =='JHB':
            city_flight = 500
        elif city_flight_departure == 'JHB' and city_flight_arrival == 'PE' or city_flight_departure == 'PE' and city_flight_arrival == 'JHB':
            city_flight = 750
        elif city_flight_departure == 'CPT' and city_flight_arrival == 'DBN' or city_flight_departure == 'DBN' and city_flight_arrival == 'CPT':
            city_flight = 1200
        elif city_flight_departure == 'CPT' and city_flight_arrival == 'PE' or city_flight_departure == 'PE' and city_flight_arrival == 'CPT':
            city_flight = 400
        elif city_flight_departure == 'DBN' and city_flight_arrival == 'PE' or city_flight_departure == 'PE' and city_flight_arrival == 'DBN':
            city_flight = 500
        else:
            print('This input is invalid. Please restart your selections.')
        return city_flight * pax
        

def car_rental(rental_days):
    return rental_days * 500
    
def holiday_cost():
    return hotel_cost(num_nights) + plane_cost(city_flight) + car_rental(rental_days)

print()
print(f'''We have the following information:
        Passengers flying:    {pax}
        Departure city:       {city_flight_departure}
        Arrival city:         {city_flight_arrival}
        Hotel stay in nights: {num_nights}
        Car rental in days:   {rental_days}
        
        The cost of the plane tickets for a one way journey: R {plane_cost(city_flight)}
        The cost of the hotel stay for {num_nights} nights:  R {hotel_cost(num_nights)}
        The cost of the car rental for {rental_days} days:   R {car_rental(rental_days)}
        
        The total cost of your vacation i.e. cost of flight, accomodation and car rental, is:
        R {holiday_cost()}''')
            

















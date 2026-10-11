# # Example of dict using multiple objects(types):
# favorite_vehicles = [
#     {
#         'make': 'Toyota', # String
#         'model': 'Corolla Hybrid', # String
#         'year': 2023, # Number (int)
#         'price':  26999.99, # Number (float)
#         'features': ['Toyota Safety Sense 3.0', 'Hybrid', 'All-Wheel Drive'], # List
#         'is_hybrid': True, # Boolean
#         'owner': None # None
#     },
#     {
#         'make': 'Ford', # String
#         'model': 'Maverick Lariat Hybrd', # String
#         'year': 2026, # Number (int)
#         'price': 38999.99, # Number (float)
#         'features': ['All-Wheel Drive', 'Hybrid', '360-Degree Camera System', 'Adaptive Cruise Control'], # List
#         'is_hybrid': True, # Boolean
#         'owner': None # None
#     },
#     { 
#         "make": "Honda",
#         "model": "CR-V Hybrid Sport",
#         "year": "2025",
#         "price": 37245.50,
#         "features": ["All-Wheel Drive", "Hybrid", "Blind Spot Information", "Heated Seats"],
#         "is_hybrid": True,
#         "owner": None
#     },
#     {
    
#         "make": "Hyundai",
#         "model": "Tucson Limited Hybrid",
#         "year": "2026",
#         "price": 41210.00,
#         "features": ["All-Wheel Drive", "Hybrid", "Panoramic Sunroof", "Smart Park Assist"],
#         "is_hybrid": True,
#         "owner": None    
#     },
#     {
#         "make": "Lexus",
#         "model": "NX 350h Luxury",
#         "year": "2027",
#         "price": 52140.20,
#         "features": ["All-Wheel Drive", "Hybrid", "Head-Up Display", "Thematic Ambient Lighting"],
#         "is_hybrid": True,
#         "owner": None
#     }
# ]

# Example of printing without for loop.
# print(favorite_vehicles[0])
# print('Next item:')
# print(favorite_vehicles[1])
# print('Next item:')
# print(favorite_vehicles[2])
# print('Next item:')
# print(favorite_vehicles[3])
# print('Next item:')
# print(favorite_vehicles[4])

# Not expected to write print commands for a lot of items in a list.
# Example of for loop that does the same as above.
# for vehicle in favorite_vehicles:
#     print(vehicle)
#     print('Next vehicle:')

# Example of for loop combined with an if-else statement:
# for vehicle in favorite_vehicles:
#     if vehicle['make'] == 'Toyota':
#         print('The first vehicle is a Toyota.')
#         print(vehicle['make'] + ' ' + vehicle['model'])
#     else:
#         print('The current vehicle is not a Toyota.')
#         print(vehicle['make'] + ' ' + vehicle['model'])

# Using break and continue with try and except so the code doesn't break + fixing the error:
# favorite_vehicles[0] = None # This will give you a TypeError.
# for vehicle in favorite_vehicles:  
#     try:
#         if vehicle['make'] == 'Toyota':
#             print('The first vehicle is a Toyota.')
#             print(vehicle['make'] + ' ' + vehicle['model'])
#             break
#         else:
#             print('Not a Toyota.')
#     except TypeError as e:
#         print('Encountered a type error.')
#         print(f'Error: {e}')
        
#         vehicle = {
#                 'make': 'Toyota', # String
#                 'model': 'Corolla Hybrid', # String
#                 'year': 2023, # Number (int)
#                 'price':  26999.99, # Number (float)
#                 'features': ['Toyota Safety Sense 3.0', 'Hybrid', 'All-Wheel Drive'], # List
#                 'is_hybrid': True, # Boolean
#                 'owner': None # None
#             }
#         if vehicle['make'] == 'Toyota':
#             print('The first vehicle is a Toyota.')
#             print(vehicle['make'] + ' ' + vehicle['model'])
#         else:
#             print('Not a Toyota.')
#             continue
#     else:
#         print('No exceptions were encountered')
#     finally:
#         print('This code will always run.')
     
# Using the any function:
# The any() function returns True if at least one element in an iterable is truthy; otherwise, it returns False.
# if any(vehicle['make'] == 'Ford' for vehicle in favorite_vehicles):
#     print('Ford found!')
# else:
#     print('Ford not found.')


# # Example if, elif, else:
# if favorite_vehicles == []:
#     print('This list is empty.')
#     print('Please add some items to the list.')
#     print('Thank you.')
# elif favorite_vehicles[0]['make'] == 'Toyota':
#     print('The first item is a Toyota.')
# else:
#     print('This list is not empty.')
#     print(favorite_vehicles[0]['make'] + ' ' + favorite_vehicles[0]['model'])



# n = 100 
# if n < 50:
#     print('The number is less than 50.')
# elif n == 50:
#     print('The number is equal to 50.')
# else:
#     print('the number is greater than 50.')

# Example of match using HTTP Status Codes:
# code = 200
# match code:
#     case 404:
#         print('Not found')
#     case 401:
#         print('Unauthorized - please authenticate')
#     case 403:
#         print('Forbidden - you don\'t have permission to access this resource')
#     case 301:
#         print('Moved permanently')
#     case 200:
#         print('Success')

# Lab challenge 5:

'''
Create a loop to iterate over the list of cars so that you can
try to see if the price is over $100,000. Print to the terminal
which cars are over $100,000.
'''
# favorite_cars = [
#     {
#         "make": "Tesla",
#         "model": "Model S",
#         "year": 2022,
#         "price": 79999.99,
#         "features": ["Autopilot", "Electric", "All-Wheel Drive"],
#         "is_electric": True,
#         "owner": None
#     },
#     {
#         "make": "Porsche",
#         "model": "911 Carrera",
#         "year": 2023,
#         "price": 106500.00,
#         "features": ["Sport Mode", "Rear-Wheel Drive", "Turbocharged"],
#         "is_electric": False,
#         "owner": None
#     },
#     {
#         "make": "Ford",
#         "model": "Mustang",
#         "year": 2022,
#         "price": 27995.00,
#         "features": ["Rear-Wheel Drive", "V8 Engine", "Fastback"],
#         "is_electric": False,
#         "owner": None
#     },
#     {
#         "make": "Chevrolet",
#         "model": "Corvette",
#         "year": 2023,
#         "price": 62995.00,
#         "features": ["Supercharged", "V8 Engine", "Fastback"],
#         "is_electric": False,
#         "owner": None
#     },
#     {
#         "make": "Audi",
#         "model": "R8",
#         "year": 2023,
#         "price": 144195.00,
#         "features": ["All-Wheel Drive", "V10 Engine", "Convertible"],
#         "is_electric": False,
#         "owner": None
#     }
# ]

# for car in favorite_cars:
#     if car["price"] > 100000: 
#         print(f'The {car["make"]} {car["model"]} is over $100,000 at ${car["price"]:,.2f}.') # Using f-strings.

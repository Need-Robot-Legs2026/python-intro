# Example of dict using multiple objects(types):
favorite_vehicles = [
    {
        'make': 'Toyota', # String
        'model': 'Corolla Hybrid', # String
        'year': 2023, # Number (int)
        'price':  26999.99, # Number (float)
        'features': ['Toyota Safety Sense 3.0', 'Hybrid', 'All-Wheel Drive'], # List
        'is_hybrid': True, # Boolean
        'owner': None # None
    },
    {
        'make': 'Ford', # String
        'model': 'Maverick Lariat Hybrd', # String
        'year': 2026, # Number (int)
        'price': 38999.99, # Number (float)
        'features': ['All-Wheel Drive', 'Hybrid', '360-Degree Camera System', 'Adaptive Cruise Control'], # List
        'is_hybrid': True, # Boolean
        'owner': None # None
    },
    { 
        "make": "Honda",
        "model": "CR-V Hybrid Sport",
        "year": "2025",
        "price": 37245.50,
        "features": ["All-Wheel Drive", "Hybrid", "Blind Spot Information", "Heated Seats"],
        "is_hybrid": True,
        "owner": None
    },
    {
    
        "make": "Hyundai",
        "model": "Tucson Limited Hybrid",
        "year": "2026",
        "price": 41210.00,
        "features": ["All-Wheel Drive", "Hybrid", "Panoramic Sunroof", "Smart Park Assist"],
        "is_hybrid": True,
        "owner": None    
    },
    {
        "make": "Lexus",
        "model": "NX 350h Luxury",
        "year": "2027",
        "price": 52140.20,
        "features": ["All-Wheel Drive", "Hybrid", "Head-Up Display", "Thematic Ambient Lighting"],
        "is_hybrid": True,
        "owner": None
    }
]

print(favorite_vehicles[0])
print('Next item:')
print(favorite_vehicles[1])

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

print('Hello world')

sum = 1 + 2
print(sum) # 3

planets_in_solar_system = 8 # int, pluto used to be the 9th planet, but is too small
distance_to_alpha_centauri = 4.367 # float, lightyears
can_liftoff = True
shuttle_landed_on_the_moon = "Apollo 11" #string

print(type(distance_to_alpha_centauri)) ## <class 'float'>

from datetime import date

print("Today's date is: " + str(date.today())) # Date of today

parsecs = 11
lightyears = parsecs * 3.26
print(str(parsecs) + " parsecs is " + str(lightyears) + " lightyears")

import sys

print(sys.argv)
print(sys.argv[0]) # program name
print(sys.argv[1]) # first arg
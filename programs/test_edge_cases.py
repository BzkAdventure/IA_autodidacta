#This file is used to test the edge cases of the ledger program.
from ast import Assert
from converter import kilometers_to_miles, celsius_to_fahrenheit, fahrenheit_to_celsius, miles_to_kilometers
from ledger import add



#This is what should happen in each case of both functions:

#converter: 
assert fahrenheit_to_celsius(50) == (50 - 32) * 5 / 9
assert celsius_to_fahrenheit(20) == 20 * 9 / 5 + 32
assert kilometers_to_miles(30) == 30 * 0.621371
assert miles_to_kilometers(10) == 10 / 0.621371

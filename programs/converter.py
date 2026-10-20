"""Unit conversions. Each conversion is one function."""


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32 #this is the formula to convert celsius to fahrenheit

#fahrenheit = (celsius * 9/5) + 32

def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9 #this is the formula to convert fahrenheit to celsius
    #celsius = (fahrenheit - 32) * 5/9 -> simple ecuation


def kilometers_to_miles(kilometers: float) -> float:
    return kilometers * 0.621371 #km to miles conversion


def miles_to_kilometers(miles: float) -> float:
    return miles / 0.621371 #miles to km conversion


_BY_NAME = {
    "c_to_f": celsius_to_fahrenheit,
    "f_to_c": fahrenheit_to_celsius,
    "km_to_mi": kilometers_to_miles,
    "mi_to_km": miles_to_kilometers,
} #we use a dictionary to store the conversion functions by name


def convert(name: str, amount: str) -> float:
    if name is None or str(name).strip() == "" or amount is None or str(amount).strip() == "":
        #we could just do name instead of str(name) because it is already a string
        raise ValueError("empty input")
    if name not in _BY_NAME:
        raise ValueError(f"unknown conversion: {name}")
    #if we arrive to a raise, the program will stop and print the error message
    return _BY_NAME[name](float(amount))
#we can return the function with the arg float because all of the functions are expecting a float
#_BY_NAME[name]-> it returns the function that we want to call
#what would happen if one of the functions is not expecting a float?
#we would get a TypeError: 'function' object is not callable
#so we need to make sure that all of the functions are expecting a float
#we can do this by adding a type hint to the functions

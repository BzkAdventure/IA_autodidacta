"""Unit conversions. Each conversion is one function."""


def celsius_to_fahrenheit(celsius: float) -> float:
    return celsius * 9 / 5 + 32


def fahrenheit_to_celsius(fahrenheit: float) -> float:
    return (fahrenheit - 32) * 5 / 9


def kilometers_to_miles(kilometers: float) -> float:
    return kilometers * 0.621371


def miles_to_kilometers(miles: float) -> float:
    return miles / 0.621371


_BY_NAME = {
    "c_to_f": celsius_to_fahrenheit,
    "f_to_c": fahrenheit_to_celsius,
    "km_to_mi": kilometers_to_miles,
    "mi_to_km": miles_to_kilometers,
}


def convert(name: str, amount: str) -> float:
    if name is None or str(name).strip() == "" or amount is None or str(amount).strip() == "":
        raise ValueError("empty input")
    if name not in _BY_NAME:
        raise ValueError(f"unknown conversion: {name}")
    return _BY_NAME[name](float(amount))

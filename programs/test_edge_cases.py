#This file is used to test the edge cases of the ledger program.

from converter import convert, kilometers_to_miles, celsius_to_fahrenheit, fahrenheit_to_celsius, miles_to_kilometers
from ledger import add, report
from datetime import date
from pathlib import Path




#This is what should happen in each case of both functions:

#converter: 
assert fahrenheit_to_celsius(50) == (50 - 32) * 5 / 9
assert celsius_to_fahrenheit(20) == 20 * 9 / 5 + 32
assert kilometers_to_miles(30) == 30 * 0.621371
assert miles_to_kilometers(10) == 10 / 0.621371

#empty value
try: 
    convert("f_to_c", "")
    assert False
except ValueError as e:
    assert str(e) == "empty input"

#unknown function
name_function:str = "unknown"
try: 
    convert(name_function, "100.00")
    assert False
except ValueError as e: 
    assert str(e) == f"unknown conversion: {name_function}"


#ledger:

try: 
    add("ledger.txt", None, "Salary")
    assert False #this line always fails when executed. 
except ValueError as e:
    assert str(e) == "empty input"

try: 
    add("ledger.txt", "hello", "Salary")
    assert False
except ValueError as e: 
    assert str(e) == "bad amount"

#check if the file exists
try: 
    report("none.txt")
    assert False #this line shouldn't run
except FileNotFoundError:
    pass


#we have to check wether:
#with a bad amount -> the file is not changed
before = report("test.txt")

try:
    add("test.txt", "bad", "Salary")
    assert False

except ValueError as e:
    pass

assert report("test.txt") == before





#read the file before and after:
try: 
    lines_b, amount_b = report("test.txt")
except FileNotFoundError as e: 
    assert False
add("test.txt", "100.0", "Salary")

lines_a, amount_a = report("test.txt")
assert len(lines_a) == len(lines_b ) + 1
assert amount_a == amount_b + 100.0

#delete the file before
Path("new.txt").unlink(missing_ok=True)
#add a line to the file
add("new.txt", "200.00", "Salary")
lines, total = report("new.txt")
assert lines[0] == (date.today().isoformat(), 200.00, "Salary")
assert total == 200.00







#For each function, write down: what is a normal input, what is an empty input,
# what is an invalid input? What should happen in each case?
#converter:
#normal input: a number
#empty input: None
#invalid: String, Float, Boolean, List, Dictionary, etc. -> ValueError
#what should happen: the function should raise a ValueError

#ledger:
#normal input: str, int, str
#empty input: None
#invalid: Float, Boolean, List, Dictionary, etc. -> ValueError
#what should happen: the function should raise a ValueError

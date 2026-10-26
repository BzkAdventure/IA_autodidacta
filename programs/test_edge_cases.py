#This file is used to test the edge cases of the ledger program.
from ast import Assert
from converter import kilometers_to_miles, celsius_to_fahrenheit, fahrenheit_to_celsius, miles_to_kilometers
from ledger import add, report
import FileNotFoundError



#This is what should happen in each case of both functions:

#converter: 
assert fahrenheit_to_celsius(50) == (50 - 32) * 5 / 9
assert celsius_to_fahrenheit(20) == 20 * 9 / 5 + 32
assert kilometers_to_miles(30) == 30 * 0.621371
assert miles_to_kilometers(10) == 10 / 0.621371

#ledger:
assert add("ledger.txt", 100, "Salary") == "2026-10-20\t100.00\tSalary\n"

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

try: 
    report("None.txt")
    assert False
except FileNotFoundError as e:
    assert str(e) == "file not found"


assert add("ledger.txt", "100.00", "Salary") == "2026-10-20\t100.00\tSalary\n"
assert add("ledger.txt", "100.00", "Salary") == "2026-10-20\t100.00\tSalary\n"  




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

#example of error: 
assert add("ledger.txt", "100", "Salary") == ValueError("bad amount")

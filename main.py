print('Hello World')
print('Hello World')
print('Hello World')
## Boolean
is_student = True
is_teacher = False
Result_And = is_student and is_teacher
Result_or = is_student or is_teacher
Result_not = not is_teacher
print(Result_And)
print(Result_or)
print(Result_not)
## Variables
message = "And now for something completely different"
n = 17
pi = 3.1415926535897931
print(n)
print(pi)
# Type of Variables
type(message)
type(n)
type(pi)
print("Done")

# Formatting of string
formatter = "{} {} {} {}"
print(formatter.format(1, 2, 3, 4))
print(formatter.format("one", "two", "three", "four"))
print(formatter.format(True, False, False, True))
print(formatter.format(formatter, formatter, formatter, formatter))
print(formatter.format(
    "Try your",
    "Own text here",
    "Maybe a poem",
    "Or a song about fear"
))
days = "Mon\nTue\nWed\nThu\nFri\nSat\nSun"
months = "Jan\nFeb\nMar\nApr\nMay\nJun\nJul\nAug"
print("Here are the days: ", days)
print("Here are the months: ", months)
print("""
There's something going on here.
With the three double-quotes.
We'll be able to type as much as we like.
Even 4 lines if we want, or 5, or 6.
""")



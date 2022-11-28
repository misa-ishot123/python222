# ZeroDivisionError
# number = 5/0

# TypeError
# x = "A" + 15

# index error
# lst = ["A","B" ,"C"]

# Syntax error
# x = "uwu bbg

# Value error (when u write a letter and not a number)
# number = int("A")

# Name error
# space = 200
# space

try:
    number = int(input("Digit: "))
    x = 5 / number
except ValueError:
    print("I asked for a digit not a letter")
except ZeroDivisionError:
    print("You can't divide by 0")

try:
        number = int(input("Digit: "))
        x = 5 / number
except Exception:
    print("Oof, you got it wrong, don't turn emo pls")

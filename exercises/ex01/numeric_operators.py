"""Demonstrates numerical values being used with four different numerical operators."""

__author__ = "730443394"

left: int = int(input("Left-hand side: "))
right: int = int(input("Right-hand side: "))

print(str(left) + " ** " + str(right) + " is " + str(left ** right))
print(str(left) + " / " + str(right) + " is " + str(left / right))
print(str(left) + " // " + str(right) + " is " + str(left // right))
print(str(left) + " % " + str(right) + " is " + str(left % right))
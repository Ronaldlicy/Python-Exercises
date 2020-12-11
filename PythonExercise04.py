# Given the number of people in the room, calculate the probability that any two people in that room have the same birthday, assuming we have 365 days in a year. (no leap years) Return the probability rounded off to two decimal points.

from math import factorial as bom

def calculate_probability(n):
    return round(1 -(bom(365) / (bom(365-n) * 365**n)),2)

print(calculate_probability(20))
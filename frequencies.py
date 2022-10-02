"""Frequencies function."""
"""ENTER YOUR SOLUTION HERE!"""

def frequencies(items):
    frequencies = {}
    for z in items:
        z = str(z)
        if z not in frequencies.keys():
            frequencies[z] = 1
        else:
            frequencies[z] += 1
    return frequencies
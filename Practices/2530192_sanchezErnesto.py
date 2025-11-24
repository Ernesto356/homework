"""
 PORTADA
 nombre: Jesus Ernesto Sanchez Luevano
 matricula = 2530192
 grupo : 1-1 IM
"""
"""
 EXECUTIVE SUMMARY
 The Fibonacci series is a sequence where each term is the sum of the previous two,
 starting from 0 and 1. Computing the series up to n terms means generating the first
 n values following this rule. This program reads an integer n, validates it, and then
 generates the series using a loop structure.
"""
"""
 PROBLEM DOCUMENTATION
 Problem: Fibonacci series generator
Description: Program that reads an integer n and prints the first n Fibonacci terms.
 Inputs:
 - n (int; number of terms to generate)
 Outputs:
 - "Fibonacci series:" followed by n terms
 Validations:
 - n must be an integer
 - n >= 1
 - Optional: n <= 50
 Test cases:
 1) Normal: n = 7 -> 0 1 1 2 3 5 8
 2) Border: n = 1 -> 0
 3) Error: n = 0 -> Error: invalid input
"""

n = int(input("Insert a number: "))

try:

    if n < 1 or n > 50:
        print("insert a number inside the specified range")
    else: 
        a = 0
        b = 1

        for i in range(n):
            c  = a
            print (c)
            a = b
            b  = a + c
except:
    print("Error: Invalid Input")

"""
 
 CONCLUSIONS
 Using a loop allows generating the Fibonacci sequence efficiently. Handling special
 cases like n = 1 or n = 2 ensures correct output for small inputs. The logic used here
 can be reused in more advanced programs involving numerical sequences or recursive
 patterns.
"""

"""
 REFERENCES
 1) Python documentation – while and for loops
 2) Python tutorials on Fibonacci calculations
 3) Course notes on sequence generation and iteration

"""
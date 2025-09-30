import os, sys
import sympy as sp

def  bad_function ( ) :
    a=1
    b=2
    print(a+b)
    return

unused_var = 10

def long_line():
    print("This is a very long line that definitely exceeds the typical character limit for most linters and should trigger warnings")
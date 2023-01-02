#mprinter.py
#Sameer Komoravolu
#5.13.2020

from sympy import latex

# Formats output to include math symbols
def mprint(rv):
    print("\[" +latex(rv) + "\]")

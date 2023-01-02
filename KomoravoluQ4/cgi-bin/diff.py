#diff.py
#Sameer Komoravolu
#5.13.2020

#Imports the Sympy library and cgi, creates x, y, z
import cgi
from sympy import *
from mprinter import *
from sympy.parsing.sympy_parser import parse_expr
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

#Takes a function and variable to differentiate with. If a number is provided,
#the slope of the function at the point is returned. Else, it differentiates the function.
def calculate(func):

    function = func.split(", ")

    if len(function) == 2:
        var_diff = function[1]
        rv = diff(function[0], var_diff)

    elif len(function) == 3:
        var_diff = function[1]
        derivative = diff(function[0], var_diff)
        rv = derivative.subs(x, function[2])
    
    return (rv)

# process input from form
form = cgi.FieldStorage()
func = form["func"].value

# HTML response
print("Content-Type: text/html")    # HTML is following

htmlHdr = """
<head>
   <script id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>

"""
print(htmlHdr)                             # blank line, end of headers

#Prints the answer
rv = calculate(func)
mprint (rv)



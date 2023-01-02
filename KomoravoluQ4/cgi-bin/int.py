#int.py
#Sameer Komoravolu
#5.13.2020

#Imports the Sympy library and cgi, creates x, y, z
import cgi
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
from mprinter import *

x = Symbol('x')
y = Symbol('y')
z = Symbol('z')

#Takes a function and variable to integrate with. If numbers are provided,
#the area of the function is returned. Else, it integrates the function.
def calculate(func):

    function = func.split(", ")
    function[1] = Symbol(function[1])

    if len(function) == 2:
        var_int = function[1]
        rv = integrate(function[0], var_int)

    elif len(function) == 4:
        var_int = function[1]
        integral = integrate(function[0], var_int)
        lower = integral.subs(x, function[2])
        upper = integral.subs(x, function[3])
        rv = (upper - lower)

    values = [rv, len(function)]
    
    return values

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
values = calculate(func)
if values[1] == 4:
    print ("<b>Area = </b>")
mprint (values[0])
if values[1] == 2:
    print ("<b> + c</b>")

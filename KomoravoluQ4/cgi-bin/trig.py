#trig.py
#Sameer Komoravolu
#5.13.2020

#Imports the Sympy library and cgi, creates x, y
import cgi
from sympy import *
from mprinter import *
from sympy.parsing.sympy_parser import parse_expr
x = Symbol('x')
y = Symbol('y')

#Takes in two parameters, function and mode. If exp, expands the expression.
#Otherwise, simplifies.
def calculate(trigfunc):

    function = trigfunc.split(", ")
    function[0] = parse_expr(function[0])
    if function[1] == "exp":
        function[0] = expand_trig(function[0])

    elif function[1] == "simp":
        function[0] = simplify(function[0])

    rv = function[0]
    return rv


# process input from form
form = cgi.FieldStorage()
trigfunc = form["trigfunc"].value

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
print()

#Prints answer
rv = calculate(trigfunc)
mprint(rv)

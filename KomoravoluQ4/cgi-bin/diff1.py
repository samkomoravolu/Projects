#diff1.py
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

#Solves the differential equation given by the constants. xval1 y'' + xval2 y' +
#xval3 y = xval4.
def calculate(xval1, xval2, xval3, xval4):
    f = Function('f')(x)
    diffeq = Eq(xval1*f.diff(x, 2) + xval2*f.diff(x) + xval3*f, xval4)
    rv = dsolve(diffeq, f)
    
    return rv

# process input from form
form = cgi.FieldStorage()
xval1 = parse_expr(form["xval1"].value)
xval2 = parse_expr(form["xval2"].value)
xval3 = parse_expr(form["xval3"].value)
xval4 = parse_expr(form["xval4"].value)

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

#Prints the answer.
rv = expand(calculate(xval1, xval2, xval3, xval4))
mprint (rv)





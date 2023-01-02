#KomoravoluInt.py
#Sameer Komoravolu
#5.9.2020
#! python3

import cgi
from mprinter import *
from sympy import *
from sympy.parsing.sympy_parser import parse_expr
x = Symbol('x')
y = Symbol('y')
z = Symbol('z')
t = Symbol('t')

def calculate(xval1, xval2, xval3, yval1, yval2, yval3, zval1, zval2, zval3):
    x = Function('x')(t)
    y = Function('y')(t)
    z = Function('z')(t)
    diffx = Eq(x.diff(t), xval1*x + xval2*y + xval3*z)
    diffy = Eq(y.diff(t), yval1*x + yval2*y + yval3*z)
    diffz = Eq(z.diff(t), zval1*x + zval2*y + zval3*z)
    system = [diffx, diffy, diffz]
    rv = dsolve(system, [x, y, z])
    
    return rv

# process input from form
form = cgi.FieldStorage()

xval1 = parse_expr(form["xval1"].value)
xval2 = parse_expr(form["xval2"].value)
xval3 = parse_expr(form["xval3"].value)

yval1 = parse_expr(form["yval1"].value)
yval2 = parse_expr(form["yval2"].value)
yval3 = parse_expr(form["yval3"].value)

zval1 = parse_expr(form["zval1"].value)
zval2 = parse_expr(form["zval2"].value)
zval3 = parse_expr(form["zval3"].value)


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


rv = calculate(xval1, xval2, xval3, yval1, yval2, yval3, zval1, zval2, zval3)
mprint (rv)






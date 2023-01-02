#eq.py
#Sameer Komoravolu
#5.13.2020

#Imports the Sympy library and cgi, creates x, y
import cgi
from sympy import *
from mprinter import *

x = Symbol('x')
y = Symbol('y')

# process input from form
form = cgi.FieldStorage()
systems = [form["system1"].value, form["system2"].value]

# HTML response
print("Content-Type: text/html")    # HTML is following
print()                             # blank line

htmlHdr = """
<head>
   <script id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>
"""

#Prints answer
def solve():
    return (solve_poly_system(systems, x, y))

rv = solve()
print(rv)

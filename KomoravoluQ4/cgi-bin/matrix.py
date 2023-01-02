#matrix.py
#Sameer Komoravolu
#5.13.2020

#Imports the Sympy library and cgi, creates x
import cgi
from sympy import *
from mprinter import *

x = Symbol('x')

#Calculates properties of matrix, depending on mode:
#If the user enters det, the determinant is calculated
#for eigen, the eigenvalues, eigenvectors and algebraic multiplicity are given
#for rref, returns reduced row-echelon form
def calculate(M, mode):
    if mode == "det":
        rv = M.det()

    elif mode == "eigen":
        rv = M.eigenvects()

    elif mode == "rref":
        rv = M.rref()

    return rv

# process input from form
form = cgi.FieldStorage()
nums = form["values"].value
size = form["size"].value
mode = form["mode"].value

#creates a list for the size of the matrix, determines the rows and columns
values = nums.split(",")
sizeList = size.split("x")
rows = int(sizeList[0])
columns = int(sizeList[1])

#creates a sympy-based matrix using a double for-loop
mat = []
for i in range(columns):
    row = []
    for j in range(rows):
        row.append(values[i*columns+j])
    mat.append(row)
        
M = Matrix(mat)

print(M)

# HTML response
print("Content-Type: text/html")    # HTML is following

#For special chars
htmlHdr = """
<head>
   <script id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>

"""

#Returns rv to html
print(htmlHdr)# blank line, end of headers

rv = calculate(M, mode)
mprint(rv)
#print ("<b>"+rv+"</b><p>")

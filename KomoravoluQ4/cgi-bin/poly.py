#Poly.py
#Sameer Komoravolu
#5.13.2020

#Imports the Sympy library and cgi
import cgi
from sympy import *
from mprinter import *


#Creates a symbol x
x = Symbol('x')

#Takes an input from the html page and either finds the zeroes, or with two arguments,
#finds the value of the function.
def calculate(userfunc):

    function = userfunc.split(",")

    #If the length is 1, finds zeroes
    if len(function) == 1:
        rv = solve(function[0], x)
        length = len(rv)
        
        #Converts the type to float
        #for i in range(length):
            #rv[i] = N(rv[i])

    #If the length is 2, substitutes a value for x
    elif len(function) == 2:
        rv = function[0].subs(x, function[1])
    
    return (rv)



# process input from form
form = cgi.FieldStorage()
userfunc = form["userinput"].value

# HTML response
print("Content-Type: text/html")    # HTML is following
print()

#For special chars
htmlHdr = """
<head>
   <script id="MathJax-script" async
          src="https://cdn.jsdelivr.net/npm/mathjax@3/es5/tex-mml-chtml.js">
  </script>
</head>

"""
#Returns rv to html
print(htmlHdr)#blank line, headers

rv = calculate(userfunc)
mprint (rv)


### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?
Python is used for back-end development, which is the area of web development in charge of creating the elements that users don't see, such as the server side of an application. While Python can be used to develop the back-end part of a web application, JavaScript can be used to develop both the bacl-end and the front-end of the application
(Source: https://www.freecodecamp.org/news/python-vs-javascript-what-are-the-key-differences-between-the-two-popular-programming-languages/)

JS provides support for arrays as inbuilt data types. Python uses lists, the closest thing to arrays that Python has to offer. Python lists are similar to another data type available in the programming language - tuples

JS makes use of curly brakcets for defining code blocks. Python uses indentation

Python cares when a function is called wtih incorrect parameters. JS doesn't care whether a function is called with correct parameters

Python features inbuilt hash tables called dictionaries, sets, etc. JS has no inbuilt hash tables

In JS, you have only floating-point variables. Python features several varieties of numeric data types, such as int, float, and complex

(Source: https://hackr.io/blog/python-vs-javascript)

Python variable name style is lower-snake-case
There is no keyword for declaring variables; ie no let or var
No specific way to make unrebindable like const


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

get(key, def_val) method is useful when we have to check for the key
setdefault(key, def_value) works in a similar way as get(), but the difference is that each time a key is absent, a new key is created with the def_value associated to the key passed in the arguments


- What is a unit test?
It is testing code in isolated small pieces. We question if this individual component works

- What is an integration test?
It is program units that are combined and tested as groups in multiple ways. We question if the parts work together


- What is the role of web application framework, like Flask?
Flask provides you with tools, libraries, and mechanics that allow you to build a web application. It reduces development time and allows programmers to build faster and smarter. It means that it provides more minimalistic functionality than an enterprise framework

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?
A URL parameter is better for the subject of the page
Query param is better to obtain more information within that subject of the page
It's better to use quesry params for applications

- How do you collect data from a URL placeholder parameter using Flask?
@app.route("/")
def hello():
  return request args.get("page_number")

- How do you collect data from the query string using Flask?
return request args.get("page_number")


- How do you collect data from the body of the request using Flask?
request get data

- What is a cookie and what kinds of things are they commonly used for?
Cookies are stored on the client's computer as text files
The goal is to remember and track data relevant to the customer's usage

- What is the session object in Flask?
It's used to track the session data which is a dictionary object that contains a key-value pair of the session varibales and their asscoiated values

- What does Flask's `jsonify()` do?
Returns a response object with the app/json mimetype set

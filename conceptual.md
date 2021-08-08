### Conceptual Exercise

Answer the following questions below:

- What are important differences between Python and JavaScript?

Python is mostly used for server-side programming, while JavaScript runs on both browser and server.

Python relies on indentation to define code blocks. JavaScript uses curly braces ({}) to group statements that belong to the same code

Python has many libraries for scientific computing, data analytics, and machine learning, whereas Javascript doesn't

Python has support for many numeral data types like int, float, fixed-point decimal, whereas JS mainly works on floating-point variables

In Python, we rely on naming conventions to define constants because there are no strict rules in the language to prevent changes to their values

Sources: https://www.educba.com/python-vs-javascript/
https://www.freecodecamp.org/news/python-vs-javascript-what-are-the-key-differences-between-the-two-popular-programming-languages/


- Given a dictionary like ``{"a": 1, "b": 2}``: , list two ways you
  can try to get a missing key (like "c") *without* your programming
  crashing.

1) setdefault(key[, default])
2) get(key[, default])

- What is a unit test?
It's a built-in unit test framework.

Tests small components of the program (units) in isolation. For example, you might test each individual function

- What is an integration test?
Integration test that components work together. You write them with unittest framework.

Program units are combined and tested as groups in multiple ways.

- What is the role of web application framework, like Flask?
Flask provides you with tools, libraries, and mechanics that allow you to build a web application but it will not enforce any dependencies or tell you how the project should look like.

A web framework is a software framework that is designed to support the development of web applications including web services, web resources, and web APIs. Web frameworks aim to automate the overhead associated with common activities performed in web development.

Sources: https://dev.to/amigosmaker/what-is-flask-used-for-2do5#:~:text=Flask%20gives%20the%20developer%20varieties,the%20project%20should%20look%20like
https://en.wikipedia.org/wiki/Web_framework

- You can pass information to Flask either as a parameter in a route URL
  (like '/foods/pretzel') or using a URL query param (like
  'foods?type=pretzel'). How might you choose which one is a better fit
  for an application?

Query strings are useful for passing data that does not require the user to take action. You could generate a query string somewhere in your app and append it to a URL so when a user makes a request, the data is automatically passed for them.

With a Python decorator, Flask provides to assign URLS in our app to functions easily. We cam handle multiple routes with a single function by simply stacking additional decorators above any route.

Sources: https://www.digitalocean.com/community/tutorials/processing-incoming-request-data-in-flask

- How do you collect data from a URL placeholder parameter using Flask?
You call flask.request.args.get(key) to retrieve the value of a parameter with the label key. You want a variable URL, which you create by adding <name> placeholders in the URL and accepting corresponding name arguments in the view function.

Sources: https://stackoverflow.com/questions/35188540/get-a-variable-from-the-url-in-a-flask-route

- How do you collect data from the query string using Flask?
In your code you use from flask import request
@app.route('/data')
def data():
# here we want to get the value of the user
  user = request.args.get('user')

  Sources: https://stackoverflow.com/questions/11774265/how-do-you-access-the-query-string-in-flask-routes

- How do you collect data from the body of the request using Flask?
request.get_data()

- What is a cookie and what kinds of things are they commonly used for?
Cookies are text files with small pieces of data that are used to identify your computer as you use a computer network. Data stored in a cookie is created by the server upon your connection.

Sources: https://www.kaspersky.com/resource-center/definitions/cookies

- What is the session object in Flask?
In Flask, a session object is used to track the session data which is a dictionary object that contains a key-value pair of the session variables and their assocaited values.

Sources: https://www.javatpoint.com/flask-session#:~:text=In%20the%20flask%2C%20a%20session,specific%20value%20on%20the%20server.


- What does Flask's `jsonify()` do?
It returns a Response object with the application/json mimetype set

Sources: https://www.kite.com/python/docs/flask.jsonify

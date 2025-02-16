#1 flask install

#2 best practices

#3 virtual env create

#4 make database using schema

#5 deploy in Heroku

#6 searched flask python in google and saw the docuementation

#7 opened vs code

#8 install vscode

#9 python download from python.org

#10 pip install virtualenv (it install virtual environment)

#11 virtualenv env (creating virtual env)

#12 Set-ExecutionPolicy unrestricted ( run this code in administrator windows powershell, set it as administrator .if scripts doesn't executes run this command it's not that important)

#13 .\env\Scripts\activate.ps1 (we do it to work on the same env. use tab to autocomplete)

#14 pip install flask

#15 make a file named app.py

#16 we can use multiple terminals in vs code. 
# first terminal will be used for install all the packages.
# second terminal will be used to run the application of mine.

#17 writing flask minimal app in google 

#18 python a likhe tap dile pyton .\app.py create hoye jabe

#19   app.run(debug=True,port= 8000) (changing the port here)

#20  create two directories static and templates

#21 static files are used to serve files. in static directory we store static files

#22 templates: in templates we will start will index.html

#23 just used ! and  enter and the boiler plate code of html all came.

#24 imported render_template in app.py to return template in python. render_template is used to return
#    @app.route("/")
# def hello_world():
#     return render_template("index.html")


#25 bootstrap: search https://getbootstrap.com/ and we will use templates form here-> 
# we will start from get started portion of it. and use the code in index.html. and run the project we will see Hello World displayed.

# 26 we can use bootstrap components from here https://getbootstrap.com/docs/5.0/getting-started/introduction/ we will just copy paste and modify

#27 take navbar component from there and paste it inside  the body tag

#28 we will work with form and search for it in getbootstrap.com

#29 we will wrap form in  <div class="container"> (container is used to contain its items)
#if we use container-fluid it wil take full width. Or if we use container it will have beautiful padding

#30 i want to add item in my todo list and the item witch i insert it will be added in my database.

#31 we will search table in the searchbar and copy bootstrap table component and paste it inside body in index.html

#32 if you write div.container it will make div tag with container class and inside it will paste the table

#33 we gave heading above table using <h2>Your Todos</h2> h2 tag

#33 khara te margin dile y use korbo r lete te margin dile x use korbo
# we will need margin above our heading h2 tag
# <div class="container  my-3">

#34  <div class="container  mb-3"> if you want bottom margin use mb-3

#35 ModuleNotFoundError: No module named 'flask' -> this error comes because of env not activated
# .\env\Scripts\activate.ps1 
# (press e than use tab witch will generate env)
# (press s than use tab witch will generate Scripts)
# (press a than use tab witch will generate active.ps1)

#36 changing the input id name of inputfield and the label for name same to same.

#37 first check if the env is activate then run command. do create database we need flask-sqlalchemy.
# we are installing it in our environment, it is an orm mapper. we will use python and change the database using it.
# flask install flask-sqlalchemy

#38 first we will import it.
# from flask_sqlalchemy import SQLAlchemy  ==> importing it 

#39 initialize it and check what sqlalchemy version did you installed
# app.config["SQLALCHEMY_DATABASE_URI"] ==> search SQLALCHEMY_DATABASE_URI on google and see how they configure it
# if you want to configure it for sqllite the configuration will be like this: sqlite:///todo.db
#sqlite:///todo.db (for sqllite database uri)
# Here are some example connection strings:

# # SQLite, relative to Flask instance path
# sqlite:///project.db

# # PostgreSQL
# postgresql://scott:tiger@localhost/project

# # MySQL / MariaDB
# mysql://scott:tiger@localhost/project


#40 Now we will set db like this:
# db = SQLAlchemy(app)

#41 SQLALCHEMY_TRACK_MODIFICATIONS add significant overhead and will be disabled by default in the future.
# Set it to true or false to suppress this warning
# app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

#42 now make db class 
# class Todo(db.Model):
#     sno = db.Column(db.Integer, primary_key=True)
#     title = db.Column(db.String(200), nullable=False)
#     desc = db.Column(db.String(500), nullable=False)
#     data_created = db.Column(db.DateTime, default = datetime.utcnow)

#43 from datetime import datetime

#45 the __repr__ method will print string of the database obj of todo
 # def __repr__(self) -> str:
 #    return f"{self.sno} - {self.title}"

#46 database create using terminal commands write 
# python (1st) (in shell)

# (2nd command start from here) (db in the instance folder)
# from app import db, app 

# with app.app_context():
#     db.create_all()
#     print("✅ Database tables created successfully!")
# (2nd command start end here)


# python

# (inside interpreter run the below code):


# print("Database created successfully!")

# ---------------------------
# Todo.db will get created inside instance folder!!


#47 search sqllite viewer on google or go to this website
# https://inloop.github.io/sqlite-viewer/

#48 command to exit from python terminal to powershell 
# exit() (command)


#49 after database create what should we do now?

#50 flask sqlalchemy te query the data likhe search korbo
# https://flask-sqlalchemy.palletsprojects.com/en/stable/quickstart/ (data kivabe query kore add korbo seta dekhbo) (nicher code e data add kore commit korse)
#  if request.method == "POST":
#         todo = Todo(title= "First Todo", desc = "Start investing in Stock Market"
#         db.session.add(user) 
#         db.session.commit()


#51 Jinja2 Snippet Kit extension download so that we could use jinja templating easily

#52 sqlalchemy query database methods below: => model.query.all()
# CRUD
# SQLAlchemy’s Session object manages all persistence operations for ORM objects.

# The following session method performs CRUD operations:

# # Inserts records into a mapping table
# db.session.add (model object)
# # delete records from a table
# db.session.delete (model object)
# # retrieves all records (corresponding to SELECT queries) from the table.
# model.query.all ()
# You can apply filters to the retrieved record set by using the filter attribute.For example, to retrieve records for city = ‘Tokyo’ in student tables, use the following statement:

# students.query.filter_by(city = ’Tokyo’).all()


# #53 this is how we printed all todos from query method of db (Todo.query.all())
# @app.route("/show")
# def products():
#     allTodo = Todo.query.all()
#     print(allTodo)
#     return "<p>This is my products!</p>"


#54 passing allTodo in index.html
    # allTodo = Todo.query.all()
    # print(allTodo)
    # return render_template("index.html",allTodo = allTodo)


#55 type jfor and use jijia 2 template extension for for loops.
# {% for todo in allTodo %}
#               <tr>
#                 <th scope="row">{{todo.sno}}</th>
#                 <td>{{todo.title}}</td>
#                 <td>{{todo.desc}}</td>
#                 <td>{{todo.data_created}}</td>
#               </tr> 
#               {% endfor %}


#56 write how to use incremental number in jinja2 in google (using loop.index)
# {% for i in p %}
# {{ loop.index }}
# {% endfor %}


#57 index.html e post korte form e action="/" method = "POST" dite hobe
# <form action="/" method = "Post">


#58 when you want to post or get you need to pass list of argument in app.py (methods = ["GET","POST"])
# @app.route("/", methods = ["GET","POST"])
# def hello_world():
#     if request.method == "POST":
#         print("post")

# and also you have to do the same in jinja template. here we passed the route in action and the method name in method = "POST"
#  <form action="/" method = "Post">


#59 we need to pass the db column in jinja index.html so that we can receive the data from there when we submit 
# <input type="text" class="form-control" name = "title" id="title" aria-describedby="emailHelp">
# <input type="text" class="form-control" name = "desc" id="desc">
# example:    name = "title" &     name = "desc"  

#60 we received the send data from input field using request method
# if request.method == "POST":
#     print(request.form['title'])


#61 when anyone clicks on todo i want to refresh it
# href = "/" means it is going to initial route 

#62 using achor tag and also taking button from bottstrap -->
# <a href="/delete/{{ todo.sno }}">
#                      <button type="button" class="btn btn-danger btn-sm">Delete</button>
#</a> 

#63 using btn-sm to small the button
# mx-1 means left and right 4x margin in buttons


#64 we also made update button
#                 <a href="/update/{{ todo.sno }}">
#                    <button type="button" class="btn btn-outline-dark btn-sm mx-1">Update</button>
#               </a>


#65 in app.py we will delete our todo (todo = Todo.query.filter_by(sno=sno).first()) and we will take first todo witch will match the sno
# @app.route("/delete/<int:sno>", methods= ["Delete"])
# def delete(sno):
#    todo = Todo.query.filter_by(sno=sno).first()
#    db.session.delete(todo)
#    db.session.commit()

#66 and after deleting the todo on the ref of sno we will redirect the init route page
# tarpor import korbo redirect and init route redirect kore dibo 
# return redirect("/")


#67 using | in jinja to get the length of the list. if list is empty show msg or else show the list
#             {% if allTodo|length==0 %}
#             no record
#            {% else %}
#           {% for todo in allTodo %}


#68 showing alert from bootstrap
#              <div class="alert alert-dark" role="alert">
#                No Todos found. Add your first todo now!
#              </div>


#69 template inheritance=> it's a concept of using same design in all the places where if i change in one page it will reflect it in all pages. just like custom widget in flutter. so we need to make base.html file for it. the thing witch is common we will store it in base.html file
# example: header, footer, navigation bar
# from doctype html to <body> tag it's common mainly in all the webpages
# and in the end we will cut the </body> and </html> tag also
#  </body>
<#/html>

#70 we will write jblock and it will come from the jinja extension
#{% block body %}
# inside here the body content will be different for all the pages    
#{% endblock body %}


#71 first we made body block in base.html 
# then we will inherit it in our index.html file using the same block of jinja code
# and it will in inside the block of jinja code


#72 we will extend the base html file in the top of index.html file.
# by writing jextend command of jinja extension it will give us the boilerplate code to extend the base.html file. then we will in the end write the parent file name witch will need to extend.
# {% extends 'base.html' %}

# also changed the tile using jblock
#{% block title %}
#  Home
#{% endblock title %}


#we also update the todo by taking the sno 
<!-- @app.route("/update/<int:sno>",methods=["Get","POST"])
def update(sno):
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo.query.filter_by(sno=sno).first()
        # todo = Todo(title = title, desc= desc)
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")      
    
    todo = Todo.query.filter_by(sno=sno).first()
    return render_template("update.html",todo = todo) -->


#73 we will use heroku to serve our website
# and we will download heroku cli to make things easy
# making it ready for heorku website serve all the commands down here

#74 pip install gunicorn (multiple threads e application serve kora jabe)
#75 pip freeze > requirements.txt (inside requirements.txt file all the project requirements will be there)
#76 Now create Procfile (Heroku use procfile deploy the application)
#77 web:gunicorn app:app (write this command inside the Procfile, this command is telling to execute the app.py file) 








# we can also make js file in static folder
# this script is written in base.html from there we are calling the js file witch in inside the static folder/js folder
# <script src="{{ url_for('static', filename='js/test.js') }}"></script>

# we can use jurl for jinja url shortcut from our extension


# we also made css file in static folder and it has been called from base.html file
# <link rel="stylesheet" href="{{ url_for('static', filename='css/style.css') }}"> 
# also made the style.css file in css folder witch is inside static folder

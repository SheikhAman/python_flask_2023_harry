from flask import Flask, render_template, request
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime


app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///todo.db"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False # for SQLALCHEMY_TRACK_MODIFICATIONS issue
db = SQLAlchemy(app)


class Todo(db.Model):
    sno = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200), nullable=False)
    desc = db.Column(db.String(500), nullable=False)
    data_created = db.Column(db.DateTime, default = datetime.utcnow)

    def __repr__(self) -> str:
        return f"{self.sno} - {self.title}"



@app.route("/", methods = ["GET","POST"])
def hello_world():
    if request.method == "POST":
        title = request.form['title']
        desc = request.form['desc']
        todo = Todo(title = title,desc= desc)
        print(request.form['title'])
    # return "<p>Hello, World!</p>"
    # todo = Todo(title= "First Todo", desc = "Start investing in Stock Market") # we used it to insert dummy data in todo
    db.session.add(todo)
    db.session.commit()
    allTodo = Todo.query.all()
    # print(allTodo)
    return render_template("index.html",allTodo = allTodo)

@app.route("/show")
def products():
    allTodo = Todo.query.all()
    print(allTodo)
    return "<p>This is my products!</p>"


if __name__ == "__main__":
    app.run(debug=True,port= 8000)
# from multiprocessing import current_process
# from typing import ByteString
from flask import Flask, render_template, request, redirect
from flask_sqlalchemy import SQLAlchemy
from datetime import datetime, timedelta

app = Flask(__name__)

# app.secret_key = "hello"
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///test.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
# app.permanent_session_lifetime = timedelta(days=1)


db = SQLAlchemy(app)


class Todo(db.Model):
    SNo = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String[200], nullable=False)
    desc = db.Column(db.String[1000], nullable=False)
    date_created = db.Column(db.DateTime, default=datetime.utcnow)


with app.app_context():
    db.create_all()


def __repr__(self) -> str:
    return f"{self.SNo}-{self.title}"


@app.route("/", methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo(title=title, desc=desc)
        db.session.add(todo)
        db.session.commit()
    allTodo = Todo.query.all()
    # print(allTodo)
    return render_template("index.html", allTodo=allTodo)


# return 'Hello, World!'


@app.route("/update/<int:SNo>", methods=["GET", "POST"])
def update(SNo):
    if request.method == "POST":
        title = request.form["title"]
        desc = request.form["desc"]
        todo = Todo.query.filter_by(SNo=SNo).first()
        todo.title = title
        todo.desc = desc
        db.session.add(todo)
        db.session.commit()
        return redirect("/")

    todo = Todo.query.filter_by(SNo=SNo).first()
    return render_template("update.html", todo=todo)


@app.route("/delete/<int:SNo>")
def delete(SNo):
    todo = Todo.query.filter_by(SNo=SNo).first()
    db.session.delete(todo)
    db.session.commit()
    return redirect("/")


@app.route("/deleteall")
def deleteAll():
    Todo.query.delete()
    db.session.commit()
    return redirect("/")


if __name__ == "__main__":
    app.run(debug=True, port=8000)
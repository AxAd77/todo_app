from flask import Flask, render_template, request, redirect, url_for
from storage.storage_csv import log
from config.db_sqlite import get_db, Todo

app = Flask(__name__)
db = get_db(app)
Todo = Todo(db)


@app.route("/")
def index():
    todo_list = Todo.todo.query.all()
    log("Index route accessed")
    return render_template("index.html", todo_list=todo_list)


@app.route("/add", methods=["POST"])
def add():
    title = request.form.get("title")
    new_todo = Todo.todo(title=title, complete=False)
    db.session.add(new_todo)
    db.session.commit()
    log("New Todo item added: " + title)
    return redirect(url_for("index"))


@app.route("/complete/<string:todo_id>")
def complete(todo_id):
    todo = Todo.todo.query.filter_by(id=todo_id).first()
    todo.complete = not todo.complete
    db.session.commit()
    log("Todo item " + todo_id + " completed")
    return redirect(url_for("index"))


@app.route("/delete/<string:todo_id>")
def delete(todo_id):
    todo = Todo.todo.query.filter_by(id=todo_id).first()
    db.session.delete(todo)
    db.session.commit()
    log("Todo item " + todo_id + " deleted")
    return redirect(url_for("index"))


if __name__ == "__main__":
    db.create_all()
    app.run(debug=True)

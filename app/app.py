from flask import Flask, render_template, request, redirect
from app import repository
# cSpell:disable

app = Flask(__name__)


@app.route('/')
def hello():
    return redirect("/students", code = 302)


@app.route("/students")
def index():
    names_list = repository.get_all_names()
    return render_template("index.html", name_list=names_list, get_name=False)


@app.route("/students/one", methods=["POST"])
def get_one():
    if request.method == "POST":
        request_name = request.form.get('SearchName')
        if request_name == '' or request_name == None:
            return redirect("/students", code = 302)
        name = repository.get_one_name(request_name)
        name = [] if name == None else [name[0]]
        return render_template("index.html", name_list=name, get_name=True)


@app.route("/students/new", methods=["POST"])
def insert_name():
    if request.method == "POST":
        name = request.form.get('CreateName')
        if name == '' or name == None:
            return redirect("/students", code = 302)
        repository.insert_name(name)
        return redirect("/students", code = 302)
    

@app.route("/students/delete", methods=["POST"])
def delete_name():
    if request.method == "POST":
        request_name = request.form.get('DeleteName')
        repository.delete_name(request_name)
        return redirect("/students", code = 302)


@app.route("/students/update", methods=["POST"])
def update_name():
    if request.method == "POST":
        request_old_name = request.form.get('UpdateOldName')
        request_new_name = request.form.get('UpdateNewName')
        print(request_old_name, request_new_name)
        repository.update_name(request_old_name, request_new_name)
        return redirect("/students", code = 302)



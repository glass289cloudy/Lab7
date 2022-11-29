from flask import Flask, render_template, request
import json


app = Flask(__name__)


@app.route("/")
def home():
    return render_template("home.html")


@app.route("/students_list")
def students_list():
    f = open('base/students_list.json', encoding="utf8")
    ld = json.load(f)
    lst = ld["students"]
    return render_template('students_list.html', students=lst)


@app.route("/create")
def create():
    if request.method == 'POST':
        return render_template('create.html')
    if request.method == 'GET':
        return render_template('create.html')


students = [
    { "name" : "Анна",
      "group": "ИБМ7",
      "avmark": 5
    },
    { "name" : "Макс",
      "group": "ИБМ5",
      "avmark": 3.3
    },
    { "name" : "Андрей",
      "group": "ИБМ7-22",
      "avmark": 4.2
    }
]


@app.route("/new_std")
def new_std():
    name = request.args.get('name')
    group = request.args.get('group')
    marks_str = request.args.get('marks')
    students.append({
        "name":name,
        "group":group,
        "avmark":marks_str
    })
    return render_template('students_list.html', students = students)


@app.route("/student/<student_name>/")
def student(student_name):
    for student in students:
        if student["name"] == student_name:
            return render_template("student.html",
                name = student["name"],
                group = student["group"],
                avmark = student["avmark"])
    return "Нет студента с данным именем"


if __name__ == "__main__":
    app.run()
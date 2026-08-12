from flask import Flask, render_template, request, redirect
import mysql.connector
import time

app = Flask(__name__)

db = None

while db is None:
    try:
        db = mysql.connector.connect(
            host="mysql",
            user="student",
            password="student123",
            database="student_db"
        )
    except:
        print("Waiting for MySQL...")
        time.sleep(5)

cursor = db.cursor()

@app.route("/")
def home():
    cursor.execute("SELECT * FROM students")
    students = cursor.fetchall()
    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add_student():

    name = request.form["name"]
    roll = request.form["roll"]
    student_class = request.form["student_class"]
    school = request.form["school"]
    email = request.form["email"]
    Phone = request.form["Phone"]

    sql = """
    INSERT INTO students
    (name, roll_number, class, school, email, Phone)
    VALUES (%s,%s,%s,%s,%s,%s)
    """

    values = (name, roll, student_class, school, email, Phone)

    cursor.execute(sql, values)
    db.commit()

    return redirect("/")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)

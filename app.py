from flask import Flask, render_template, request
import mysql.connector

app = Flask(__name__)

# MySQL connection
db = mysql.connector.connect(
    host="localhost",
    user="root",
    password="your_password",
    database="InternshipDB"
)

cursor = db.cursor()

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/register', methods=['POST'])
def register():
    student_name = request.form['student_name']
    email = request.form['email']
    phone = request.form['phone']
    course = request.form['course']
    domain = request.form['domain']

    query = """
    INSERT INTO internship_registrations 
    (student_name, email, phone, course, domain)
    VALUES (%s, %s, %s, %s, %s)
    """

    values = (student_name, email, phone, course, domain)

    cursor.execute(query, values)
    db.commit()

    return "Registration Successful"

if __name__ == '__main__':
    app.run(debug=True)

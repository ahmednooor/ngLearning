
### Imports
from flask import Flask, flash, redirect, render_template, request, session, url_for, jsonify, g
import sqlalchemy
from cs50 import SQL
import os

class SQL(object):
    """Wrap SQLAlchemy to provide a simple SQL API."""

    def __init__(self, url):
        """
        Create instance of sqlalchemy.engine.Engine.

        URL should be a string that indicates database dialect and connection arguments.

        http://docs.sqlalchemy.org/en/latest/core/engines.html#sqlalchemy.create_engine
        """
        try:
            self.engine = sqlalchemy.create_engine(url)
        except Exception as e:
            raise RuntimeError(e)

    def execute(self, text, *multiparams, **params):
        """
        Execute a SQL statement.
        """
        try:

            # bind parameters before statement reaches database, so that bound parameters appear in exceptions
            # http://docs.sqlalchemy.org/en/latest/core/sqlelement.html#sqlalchemy.sql.expression.text
            # https://groups.google.com/forum/#!topic/sqlalchemy/FfLwKT1yQlg
            # http://docs.sqlalchemy.org/en/latest/core/connections.html#sqlalchemy.engine.Engine.execute
            # http://docs.sqlalchemy.org/en/latest/faq/sqlexpressions.html#how-do-i-render-sql-expressions-as-strings-possibly-with-bound-parameters-inlined
            statement = sqlalchemy.text(text).bindparams(*multiparams, **params)
            result = self.engine.execute(str(statement.compile(compile_kwargs={"literal_binds": True})))

            # if SELECT (or INSERT with RETURNING), return result set as list of dict objects
            if result.returns_rows:
                rows = result.fetchall()
                return [dict(row) for row in rows]

            # if INSERT, return primary key value for a newly inserted row
            elif result.lastrowid is not None:
                return result.lastrowid

            # if DELETE or UPDATE (or INSERT without RETURNING), return number of rows matched
            else:
                return result.rowcount

        # if constraint violated, return None
        except sqlalchemy.exc.IntegrityError:
            return None

        # else raise error
        except Exception as e:
            raise RuntimeError(e)


### configure flask
app = Flask(__name__)

### configure CS50 Library to use SQLite database
THIS_FOLDER_G = os.path.dirname(os.path.abspath(__file__))
db = SQL("sqlite:///" + THIS_FOLDER_G + "/db/system.db")


@app.route('/')
def home():
    return render_template("index.html")


@app.route('/getemployees')
def getemployees():
    employees = db.execute("SELECT * FROM employees")
    return jsonify(employees)


@app.route('/getemployee/<id>')
def getemployee(id):
    employees = db.execute("SELECT * FROM employees WHERE id=:id", id=int(id))
    return jsonify(employees)


@app.route('/addemployee', methods=['POST'])
def addemployee():
    if request.method == 'POST':
        name = request.json['name']
        designation = request.json['designation']
        email = request.json['email']
        contact = request.json['contact']
        address = request.json['address']
        salary = request.json['salary']
        if name == "" or designation == "" or email == "" or contact == "" or address == "" or salary == "":
            return jsonify([{"status": "error", "msg": "Incomplete Details"}])    
        else:
            db.execute("INSERT INTO employees (name, designation, email, contact, address, salary) VALUES (:name, :designation, :email, :contact, :address, :salary)", name=name, designation=designation, email=email, contact=contact, address=address, salary=int(salary))
        return jsonify([{"status": "success", "msg": "Employee Added"}])
    else:
        return jsonify([{"status": "error", "msg": "Error"}])


@app.route('/saveemployee', methods=['POST'])
def saveemployee():
    if request.method == 'POST':
        id = request.json['id']
        name = request.json['name']
        designation = request.json['designation']
        email = request.json['email']
        contact = request.json['contact']
        address = request.json['address']
        salary = request.json['salary']
        if name == "" or designation == "" or email == "" or contact == "" or address == "" or salary == "":
            return jsonify([{"status": "error", "msg": "Incomplete Details"}])    
        else:
            db.execute("UPDATE employees SET name=:name, designation=:designation, email=:email, contact=:contact, address=:address, salary=:salary WHERE id=:id", name=name, designation=designation, email=email, contact=contact, address=address, salary=int(salary), id=int(id))
        return jsonify([{"status": "success", "msg": "Employee Updated"}])
    else:
        return jsonify([{"status": "error", "msg": "Error"}])


@app.route('/deleteemployee/<id>', methods=['POST'])
def deleteemployee(id):
    if request.method == 'POST':
        db.execute("DELETE FROM employees WHERE id=:id", id=int(id))
        return jsonify([{"status": "success", "msg": "Employee Deleted"}])
    else:
        return jsonify([{"status": "error", "msg": "Error"}])


if __name__ == '__main__':
    app.run()
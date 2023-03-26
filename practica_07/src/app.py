from flask import Flask, render_template, request, redirect, url_for    # pip install flask
import os
import database as db                       # pip install mysql-connector-python
from contextlib import closing, suppress

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__))) # path to the parent directory of the current file
template_dir = os.path.join(template_dir, "src", "templates")  # path to the templates directory

app = Flask(__name__, template_folder=template_dir) 

# Rutas de la aplicacion
@app.route("/")
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM users")
    myresult = cursor.fetchall()
    
    # Convertir el resultado de la consulta a un diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record))) 
    cursor.close()
    return render_template("index.html", data=insertObject)

#? OTRA FORMA USANDO "supress" y "closing" --------------------------------------
    # @app.route("/")
    # def home():
    #     with suppress(Exception), closing(db.database.cursor()) as cursor:
    #             cursor.execute("SELECT * FROM users")
    #             myresult = cursor.fetchall()

    #             # Convertir el resultado de la consulta a un diccionario
    #             insertObject = []
    #             columnNames = [column[0] for column in cursor.description]
    #             for record in myresult:
    #                 insertObject.append(dict(zip(columnNames, record))) 
    #             cursor.close()
    #             return render_template("index.html", data=insertObject)
#? ------------------------------------------------------------------------------

#Ruta para guardar usuarios en la BD
@app.route("/user", methods=['POST'])
def addUser():
    username = request.form["username"]
    name = request.form["name"]
    password = request.form["password"]

    if username and name and password:
        cursor = db.database.cursor()
        sql = "INSERT INTO users (username, name, password) VALUES (%s, %s, %s)"
        data = (username, name, password)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

#Ruta para eliminar usuarios de la BD
@app.route("/delete/<string:id>")
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM users WHERE id = %s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

#Ruta para actualizar usuarios de la BD
@app.route("/edit/<string:id>", methods=['POST'])
def update(id):
    username = request.form["username"]
    name = request.form["name"]
    password = request.form["password"]

    if username and name and password:
        cursor = db.database.cursor()
        sql = "UPDATE users SET username = %s, name = %s, password = %s WHERE id = %s"
        data = (username, name, password, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == "__main__":              # si el archivo se ejecuta directamente 
    app.run(debug=True, port=4000)      # ejecuta la aplicacion
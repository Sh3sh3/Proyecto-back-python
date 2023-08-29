from flask import Flask, render_template, request, redirect, url_for
import os
import database as db

template_dir = os.path.dirname(os.path.abspath(os.path.dirname(__file__)))
template_dir = os.path.join(template_dir, 'src', 'templates')

app = Flask(__name__, template_folder = template_dir)

#Rutas de la aplicación
@app.route('/')
def home():
    cursor = db.database.cursor()
    cursor.execute("SELECT * FROM Peliculas")
    myresult = cursor.fetchall()
    #Convertir los datos a diccionario
    insertObject = []
    columnNames = [column[0] for column in cursor.description]
    for record in myresult:
        insertObject.append(dict(zip(columnNames, record)))
    cursor.close()
    return render_template('index.html', data=insertObject)

#Ruta para guardar Peliculas en la bdd
@app.route('/user', methods=['POST'])
def addUser():
    pelicula = request.form['pelicula']
    categoria = request.form['categoria']
    anio = request.form['anio']

    if pelicula and categoria and anio:
        cursor = db.database.cursor()
        sql = "INSERT INTO Peliculas (username, name, password) VALUES (%s, %s, %s)"
        data = (pelicula, categoria, anio)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

@app.route('/delete/<string:id>')
def delete(id):
    cursor = db.database.cursor()
    sql = "DELETE FROM Peliculas WHERE id=%s"
    data = (id,)
    cursor.execute(sql, data)
    db.database.commit()
    return redirect(url_for('home'))

@app.route('/edit/<string:id>', methods=['POST'])
def edit(id):
    pelicula = request.form['pelicula']
    categoria = request.form['categoria']
    anio = request.form['anio']

    if pelicula and categoria and anio:
        cursor = db.database.cursor()
        sql = "UPDATE Peliculas SET pelicula = %s, categoria = %s, anio = %s WHERE id = %s"
        data = (pelicula, categoria, anio, id)
        cursor.execute(sql, data)
        db.database.commit()
    return redirect(url_for('home'))

if __name__ == '__main__':
    app.run(debug=True)


#importing libraries
import os
import flask
from flask import Flask, render_template, request
from flask_mysqldb import MySQL
import MySQLdb.cursors

app=flask.Flask(__name__)

# Enter your database connection details below
app.config['MYSQL_HOST'] = 'remotemysql.com'
app.config['MYSQL_USER'] = 'vXbjh1p4zd'
app.config['MYSQL_PASSWORD'] = 'wa2gJh7dKr'
app.config['MYSQL_DB'] = 'vXbjh1p4zd'

# Intialize MySQL
mysql = MySQL(app)


#to tell flask what url shoud trigger the function index()
@app.route('/')

@app.route('/index/')
def index():
    cursor_daftaruser = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
    cursor_daftaruser.execute('SELECT Nama.id as ID, Nama.name as Name, Work.name as Work, Kategori.salary as Salary FROM Nama JOIN Work ON Nama.id_work = Work.id JOIN Kategori ON Nama.id_salary = Kategori.id')
    daftaruser = cursor_daftaruser.fetchall()
    return flask.render_template('index.html', data = daftaruser)

@app.route('/add',methods = ['GET', 'POST'])
def add():
    if request.method == 'POST':
        Name = request.form['Name']
        Work = request.form['Work']
        Salary = request.form['Salary']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('INSERT INTO Nama VALUES (NULL, %s, %s, %s)', (Name, Work, Salary))
        mysql.connection.commit()
        cursor_daftaruser = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor_daftaruser.execute('SELECT Nama.id as ID, Nama.name as Name, Work.name as Work, Kategori.salary as Salary FROM Nama JOIN Work ON Nama.id_work = Work.id JOIN Kategori ON Nama.id_salary = Kategori.id')
        daftaruser = cursor_daftaruser.fetchall()
        return render_template("index.html", data=daftaruser)

@app.route('/edit',methods = ['GET', 'POST'])
def edit():
    if request.method == 'POST':
        Name = request.form['Name']
        Work = request.form['Work']
        Salary = request.form['Salary']
        ID = request.form['ID']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('UPDATE Nama SET name=%s, id_work=%s, id_salary=%s WHERE id = %s', (Name, Work, Salary, ID))
        mysql.connection.commit()
        cursor_daftaruser = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor_daftaruser.execute('SELECT Nama.id as ID, Nama.name as Name, Work.name as Work, Kategori.salary as Salary FROM Nama JOIN Work ON Nama.id_work = Work.id JOIN Kategori ON Nama.id_salary = Kategori.id')
        daftaruser = cursor_daftaruser.fetchall()
        return render_template("index.html", data=daftaruser)

@app.route('/delete',methods = ['GET', 'POST'])
def delete():
    if request.method == 'POST':
        ID = request.form['ID']
        Name = request.form['Name']
        cursor = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor.execute('DELETE from Nama WHERE id = %s', (ID))
        mysql.connection.commit()
        cursor_daftaruser = mysql.connection.cursor(MySQLdb.cursors.DictCursor)
        cursor_daftaruser.execute('SELECT Nama.id as ID, Nama.name as Name, Work.name as Work, Kategori.salary as Salary FROM Nama JOIN Work ON Nama.id_work = Work.id JOIN Kategori ON Nama.id_salary = Kategori.id')
        daftaruser = cursor_daftaruser.fetchall()
        msghapus = 1
        return render_template("index.html", data=daftaruser, datahapus=Name, msghapus=msghapus)

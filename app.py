from flask import Flask, render_template, request
from data_object import DataUser 

app=Flask(__name__)

@app.route("/")
def index():
    return render_template("inicioSesion.html")

@app.route("/inicioSesion")
def inicioSesion():
    return render_template("inicioSesion.html")

@app.route("/registro")
def registro():
    return render_template("registro.html")

@app.route("/hoteles")
def hoteles():
    return render_template("hoteles.html")

@app.route("/reservacion")
def reservacion():
    return render_template("reservaciones.html")

@app.route("/contacto")
def contacto():
    return render_template("contactos.html")


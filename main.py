from flask import Flask, render_template


#inicializar la variable app con flask
app = Flask(__name__)


#inicializar parametros para el servidor de flask
#en mac: 
#export FLASK_APP=mail.py
#en windows
#set FLASK_APP·main·run

@app.route("/calculador/<int:num1>/<int:num2>/<op>")
def operaciones_mates(num1,num2,op):#op suma,resta, multi,divi
    result=""
    if op == "suma":
        result = f"La suma es:{num1{num1+num2}"
    elif op == "resta":
        result = f"La resta es: {num1-num2}"
    elif op == "multi":
        result = f"La multiplicación es: {num1*num2}"
    elif op == "divi":
        result = f"La división es: {num1/num2}"

    return result



@app.route("/html")
def mi_html():
    return render_template('hola.html',variable = "Hola esto es una variable desde metodo",nombre="Rolando")

@app.route("/segunda")
def mi_html_segunda():
    return render_template('segunda.html')


#ejercicio
#al metodo operaciones_mates, agregamos una vista html y mostramos dentro de esta
#su resultado y los numeros y la operacion ejemplo: 10 + 5 = 15,
#si el usuario no pasa una operacion mostrar un mensaje 
#que diga debe ingresar la operacion : suma,resta,multi,divi

@app.route("/calculadora/<int:num1>/<int:num2>/<op>")
def operaciones_mates_tarea(num1,num2,op):#op suma,resta, multi,divi
    result=""
    if op == "suma":
        result = f"La suma es: {num1} + {num2} = {num1+num2}"
    elif op == "resta":
        result = f"La resta es: {num1} - {num2} ={num1-num2}"
    elif op == "multi":
        result = f"La multiplicación es: {num1} * {num2} = {num1*num2}"
    elif op == "divi":
        result = f"La división es: {num1} / {num2} = {num1/num2}"
    else:
        result = "debe ingresar la operacion : suma,resta,multi,divi"
        
    return render_template('tarea.html', resultado = result)
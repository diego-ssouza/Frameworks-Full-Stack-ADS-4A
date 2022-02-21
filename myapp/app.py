from asyncio.windows_events import NULL
from flask import Flask,render_template, request
 
app = Flask(__name__)

@app.route("/",methods =["POST","GET"])
def calculate():
    resultado =""
    if request.method == "POST":
        var1 =float(request.form.get("var1"))
        var2 =float(request.form.get("var2"))
        operacao = str(request.form.get("operacao"))
        if operacao =="soma":
            resultado = round(var1+var2)
        elif operacao =="subtracao":
            resultado = round(var1-var2)
        elif operacao == "divisao":
            resultado =round(var1/var2)
        elif operacao == "multiplicacao":
            resultado = round(var1*var2)
    if resultado == 0 or resultado == NULL:
        resultado = str(0)
    return render_template("index.html",resultado = resultado)

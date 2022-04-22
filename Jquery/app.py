
from flask import Flask, jsonify,render_template, request
 
app = Flask(__name__)

@app.route("/index",methods =["GET"])
def index():
    return render_template("index.html")
    

@app.route("/api/retorno",methods =["post"])
def api():
    json = request.get_json()
    a = json['nome_aluno']
    a = a.upper()
    b =json['email']
    b = b.upper()
    json['nome_aluno'] = a 
    json['email'] = b 
    json['concatena'] = json['nome_aluno']+ json['email']
    return jsonify(json)
    
if __name__ == '__main__':
   app.run(debug=True, host='localhost', port=5000)
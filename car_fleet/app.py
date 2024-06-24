from flask import Flask, request, jsonify, render_template, redirect, url_for
import couchdb

app = Flask(__name__)

# Conectar ao CouchDB
couch = couchdb.Server('http://Admin:91190559@127.0.0.1:5984/')
db_name = 'carros'
try:
    db = couch.create(db_name)
except couchdb.http.PreconditionFailed:
    db = couch[db_name]

# Rota principal
@app.route('/')
def index():
    carros = [db[doc_id] for doc_id in db]
    return render_template('index.html', carros=carros)

# Formulário para adicionar/editar carro
@app.route('/carros/form/', methods=['GET', 'POST'])
@app.route('/carros/form/<id>', methods=['GET', 'POST'])
def form_carro(id=None):
    if request.method == 'POST':
        carro = request.form.to_dict()
        if id:
            carro_atual = db[id]
            carro['_id'] = id
            carro['_rev'] = carro_atual['_rev']
        db.save(carro)
        return redirect(url_for('index'))
    carro = db.get(id) if id else {}
    return render_template('form.html', carro=carro)


# Deletar um carro
@app.route('/carros/delete/<id>', methods=['POST'])
def deletar_carro(id):
    try:
        carro = db[id]
        db.delete(carro)
        return redirect(url_for('index'))
    except couchdb.http.ResourceNotFound:
        return jsonify({'error': 'Carro não encontrado'}), 404

if __name__ == '__main__':
    app.run(debug=True)
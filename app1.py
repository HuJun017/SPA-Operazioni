from flask import Flask, render_template, request, jsonify
app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template('homepage1.html')

@app.route('/calcola', methods=['GET'])
def calcola():
    # Prendi i dati dalla query string
    num1 = request.args.get('num1', type=float)
    num2 = request.args.get('num2', type=float)
    operazione = request.args.get('operazione')


    # Esegui l'operazione richiesta
    if operazione == 'addizione':
        risultato = num1 + num2
    elif operazione == 'sottrazione':
        risultato = num1 - num2
    elif operazione == 'moltiplicazione':
        risultato = num1 * num2
    elif operazione == 'divisione':
        if num2 != 0:
            risultato = num1 / num2
        else:
            return jsonify(risultato="Errore: divisione per zero")
    else:
        return jsonify(risultato="Operazione non valida")

    # Restituisci il risultato al front-end
    return jsonify(risultato=risultato)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=3245, debug=True)

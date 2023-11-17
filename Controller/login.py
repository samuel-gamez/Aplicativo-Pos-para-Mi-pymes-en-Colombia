from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from Models.Login import Usuario

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        usu_correo = request.form['correo']
        usu_pass = request.form['passwd']

        usuario_model = Usuario()
        resultado = usuario_model.login(usu_correo, usu_pass)

        if resultado:
            session['usu_id'] = resultado['usu_id']
            session['usu_correo'] = resultado['usu_correo']
            return redirect(url_for('home')) 
        else:
            return jsonify({'error': 'Invalid credentials. Please try again.'})

    return render_template('Index.html')


from flask import Flask, render_template, request, redirect, url_for, session, jsonify
from Models.Login import Usuario

app = Flask(__name__)
app.secret_key = 'random'

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
            return jsonify({'redirect': url_for('Inicio')})
        else:
            return jsonify({'error': 'Invalid credentials. Please try again.'})

    return render_template('Index.html')


@app.route('/Registro')
def Registro():
    return render_template('Registro.html')

@app.route('/404')
def Error():
    return render_template('404.html')

@app.route('/Inicio')
def Inicio():
    if 'usu_id' in session:
        return render_template('Inicio.html')
    else:
        return redirect(url_for('login'))

if __name__ == '__main__':
    app.run(debug=True)




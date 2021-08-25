from flask import render_template
from app import app

@app.route('/')
@app.route('/index')
def index():
    return render_template('index.html', nome="Pedroa", sobrenome="Felipe")
@app.route('/outro')       
def outro():
    return '''
    <html>
        <body>
            <h1>outro</h1>
        </body>
    </html>
    '''       
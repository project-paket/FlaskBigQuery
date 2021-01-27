from flask import Flask, request
from flask import render_template

app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])
def contanct():
    if request.method == 'POST':
        if request.form['submit_button'] == 'Click me':
            pass
    elif request.method == 'GET':
        return render_template('main.html')

if __name__ == '__main__':
    app.run()
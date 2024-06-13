from flask import Flask, render_template, request, redirect, send_file
from parser_tinkoff import parser_tinkoff

app = Flask(__name__)

@app.route("/", methods = ['POST','GET'])
def index():
    if request.method == 'POST':
        start = request.form['start_date']
        end = request.form['end_date']
        parser_tinkoff(start, end)
        return send_file('tinkoff_index.xlsx')
    else:
        return render_template('index.html')

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000)
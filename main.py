from flask import Flask, render_template, request

app = Flask(__name__)

@app.route('/')
def home():
  return render_template('home.html')

@app.route('/rlg')
def rlg():
  return render_template('rlg.html')


app.run(host='0.0.0.0', port=8020)
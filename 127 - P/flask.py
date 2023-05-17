from flask import Flask, jsonify
from interpreting import df

app = Flask(__name__)

@app.route('/stars')
def get_stars():
    return jsonify(df)

app.run()

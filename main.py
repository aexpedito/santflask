from app import app
from flask import render_template, send_file
import sys

@app.route('/', methods=['GET'])
@app.route('/index', methods=['GET'])
@app.route('/index.html', methods=['GET'])
def main():
    return render_template('index.html')


@app.route('/logo.jpg', methods=['GET'])
def logo():
    return send_file('logo.jpg')

if __name__ == "__main__":
    port = sys.argv[1]
    app.run(host="0.0.0.0", port=port, debug=False)
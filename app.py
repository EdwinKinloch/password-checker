from flask import Flask, request, jsonify, render_template
from passwordcheck import pwned_api_check
import getpass

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/check_password', methods=['POST'])
def check_password():
    password = request.form.get('password')
    count = pwned_api_check(password)
    return jsonify({"count": count})

if __name__ == '__main__':
    app.run(debug=True)

from flask import Flask
from flask import request
import hashlib
import json
app = Flask(__name__)

stored_files = {}


@app.route('/', methods=['GET'])
def get_dummy_files():
    return "Returned dummy files\n"


@app.route('/<int:id>', methods=['GET'])
def get_file(id):
    if id in stored_files:
        return stored_files[id]
    else:
        return "No such file\n"


@app.route('/', methods=['POST'])
def upload_file():
    data = json.loads(request.data)
    uploaded_file = data['uploaded_file']
    salt = data['salt']
    id = hashlib.md5(uploaded_file.encode()).hexdigest()
    stored_files[id] = (uploaded_file, salt)
    return "File stored\n"


if __name__ == "__main__":
    app.run()

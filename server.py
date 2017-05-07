from flask import Flask
from flask import request
import flask
import hashlib
import json
import gzip
app = Flask(__name__)

stored_files = {}


@app.route('/profile/<type>', methods=['GET'])
def get_dummy_files(type):
    if type == 'lawyer':
        pass
    elif type == 'doctor:':
        pass
    elif type == 'female':
        pass
    elif type == 'male':
        pass
    else:
        return "No files here\n"

    return "Sent files\n"


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
    id = hashlib.sha256(uploaded_file.encode()).hexdigest()
    stored_files[id] = (uploaded_file, salt)
    return "File stored\n"


if __name__ == "__main__":
    app.run()

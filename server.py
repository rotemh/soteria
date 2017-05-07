from flask import Flask
from flask import request
import hashlib
import json
app = Flask(__name__)

stored_files = {}


@app.route('/profile/<type>', methods=['GET'])
def get_dummy_files(type):
    if type == 'lawyer':
        gzip_address = './zipfiles/doc.tar.gz'
    elif type == 'doctor:':
        gzip_address = './zipfiles/doc.tar.gz'
    elif type == 'female':
        gzip_address = './zipfiles/doc.tar.gz'
    elif type == 'male':
        gzip_address = './zipfiles/doc.tar.gz'
    else:
        return "No files here\n"

    gzip_file = open(gzip_address).read()
    return bytearray(gzip_file)


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

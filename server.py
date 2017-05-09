from flask import Flask
from flask import request
import hashlib
import json
import base64
app = Flask(__name__)

stored_files = {}


@app.route('/profile/<type>', methods=['GET'])
def get_dummy_files(type):
    print(type)
    if type == 'lawyer':
        zip_address = 'zipfiles/SC_Cases.zip'
    elif type == 'doctor':
        zip_address = 'zipfiles/Forms.zip'
    elif type == 'female':
        zip_address = 'zipfiles/FamilyVacation.zip'
    elif type == 'male':
        zip_address = 'zipfiles/PuppyPics.zip'
    else:
        return "No files here\n"

    with open(zip_address, "rb") as f:
        x = f.read()
        return base64.b64encode(x)


@app.route('/<f_id>', methods=['GET'])
def get_file(f_id):
    if f_id in stored_files:
        return ','.join(stored_files[f_id])
    else:
        return "No such file\n"


@app.route('/', methods=['POST'])
def upload_file():
    data = json.loads(request.data)
    uploaded_file = data['_file']
    salt = data['salt']
    id = hashlib.sha256(uploaded_file.encode()).hexdigest()
    stored_files[id] = (uploaded_file, salt)
    return id


if __name__ == "__main__":
    app.run()

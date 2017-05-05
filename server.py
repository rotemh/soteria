from flask import Flask
from flask import request
app = Flask(__name__)

stored_files = []

@app.route('/<int:id_num>', methods=['GET'])
def get_file(id_num):
    return stored_files[id_num]


@app.route('/', methods=['POST'])
def upload_file():
    data = request.args
    new_file = data['uploaded_file']
    stored_files.append(new_file)
    return "File stored"



if __name__ == "__main__":
    app.run()

import os
from io import BytesIO
import zipfile
import requests
import base64
import json

SERVER_ADDRESS = 'http://127.0.0.1:5000/'

class InMemoryZip(object):
    """
    Adopted from -
    http://stackoverflow.com/questions/2463770/python-in-memory-zip-library
    """
    def __init__(self):
        # Create the in-memory file-like object
        self.in_memory_zip = BytesIO()

    def append(self, filename_in_zip, file_contents):
        '''Appends a file with name filename_in_zip and contents of
        file_contents to the in-memory zip.'''
        # Get a handle to the in-memory zip in append mode
        zf = zipfile.ZipFile(self.in_memory_zip, "a", zipfile.ZIP_DEFLATED, False)

        # Write the file to the in-memory zip
        zf.writestr(filename_in_zip, file_contents)

        # Mark the files as having been created on Windows so that
        # Unix permissions are not inferred as 0000
        for zfile in zf.filelist:
            zfile.create_system = 0

        return self

    def read(self):
        '''Returns a byte array with the contents of the in-memory zip.'''
        self.in_memory_zip.seek(0)
        return self.in_memory_zip.read()

    def writetofile(self, filename):
        '''Writes the in-memory zip to a file.'''
        f = file(filename, "w")
        f.write(self.read())
        f.close()



def zip_dir(dir_path):
    """
    Gets a dir path and returns a bytearray with the directory's zipped content
    :param dir_path:
    :return:
    """
    imz = InMemoryZip()

    for root, dirs, files in os.walk(dir_path):
        for file in files:
            with open(os.path.join(root, file), 'rb') as f:
                imz.append(os.path.join(root, file), f.read())

    return imz.read()


def unzip(data, dir_path):
    """
    Gets a a zipped file byte array and uncompress the data into a the dir_path
    :param data:
    :return:
    """

    if not os.path.exists(dir_path):
        os.makedirs(dir_path)

    with open(dir_path + '/content.zip', "wb") as f:
        f.write(data)

    zip_ref = zipfile.ZipFile(dir_path + '/content.zip', 'r')
    zip_ref.extractall(dir_path)
    zip_ref.close()
    os.remove(dir_path + '/content.zip')


def post_request(url, payload):
    """
    Gets a url and  arguments (key, value) and creates and submits a POST request
    :param url: string
    :param payload: python dict
    :return: post request object
    """
    return requests.post(url, data=payload)

def post_encrypted_file(url, enc_data, salt):
    """
    Post the encrypted data to the server
    :param url:
    :param enc_data:
    :param salt:
    :return:
    """
    b64 = lambda x: base64.b64encode(bytes(x))
    return post_request(url, json.dumps({'_file': b64(enc_data), 'salt':b64(salt)})).text

def get_encrypted_file(hash_id):
    """
    Given HashID, returns a tuple of <bytes, salt>
    :param id:
    :return:
    """

    b64 = lambda x: base64.b64decode(x)
    ans = get_request(SERVER_ADDRESS + hash_id).split(',')
    return b64(ans[0]), b64(ans[1])

def get_request(url):
    """
    Gets a url and creates and submits a GET request
    :param url: string
    :return: bytearray
    """
    req = requests.get(url)
    return req.text

def self_destruct():
    """
    This function deletes the file is running from ! BE CAREFUL WHEN USING!!!!!
    :return:
    """
    import sys, os
    dir_path = os.path.dirname(os.path.realpath(__file__))
    os.system("python -c \"import os, time; time.sleep(2); os.remove('{}/{}');\"".format(dir_path, sys.argv[0]))
    exit(0)

if __name__ == '__main__':
    x = zip_dir('/Users/rotemhemo/Desktop/time_capsule')
    print post_encrypted_file("http://127.0.0.1:5000", x, "lksdhbglkdfhgb")
    # unzip(x, '/Users/rotemhemo/Desktop/time_capsule/test')
    pass


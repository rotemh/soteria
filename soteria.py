import crypto
import utils

def main():
    key, salt = crypto.key_gen("123456")
    x  = utils.zip_dir('/Users/rotemhemo/Desktop/time_capsule')
    r  = utils.post_encrypted_file('http://127.0.0.1:5000/', crypto.encrypt(x, key), salt)
    print "Your id is - ", r
    print utils.get_request('http://127.0.0.1:5000/'+r)
if __name__ == '__main__':
    main()
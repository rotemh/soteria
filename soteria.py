import crypto
import utils

def main():
    key, salt = crypto.key_gen("123456")
    x  = utils.zip_dir('/Users/rotemhemo/Desktop/time_capsule')
    r  = utils.post_encrypted_file(utils.SERVER_ADDRESS, crypto.encrypt(x, key), salt)
    print "Your id is - ", r

    # From the server
    enc_data, salt = utils.get_encrypted_file(r)
    key, salt = crypto.key_gen("123456", salt)
    utils.unzip(crypto.decrypt(enc_data, key), '/Users/rotemhemo/Desktop/time_capsule/test')


if __name__ == '__main__':
    main()
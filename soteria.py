import crypto
import utils
import fake
import sys
import hashlib

def main():


    #encr = raw_input("Are you encrypting or decrypting files? \n\
     				#Enter \'e\' for encrypt or \'d\' for decrypt: ")
    args = sys.argv
    encr = args[1]
    # job = args[2]
    # sex = args[3]
    # out_folder = args[4]

    key, passphrase, salt = crypto.key_gen()

    if encr == "-e":
        x = utils.zip_dir('/Users/rotemhemo/Desktop/time_capsule')
        r = utils.post_encrypted_file(utils.SERVER_ADDRESS, crypto.encrypt(x, key), ''.join(passphrase[:2]), salt)
        print("Your passphrase is (Don't losr it!!!- ", passphrase)

        prof = fake.Profile('Doctor', 'Female', '/Users/rotemhemo/Desktop/time_capsule')
        prof.get_files()
        prof.extract_files()
    elif encr == "-d":
        # From the server
        print "Please Enter your pass phrase - "
        passphrase = raw_input()
        enc_data, salt = utils.get_encrypted_file(hashlib.sha256(passphrase[:2]).hexdigest())
        key, salt = crypto.key_gen(passphrase, salt)
        utils.unzip(crypto.decrypt(enc_data, key), '/Users/rotemhemo/Desktop/time_capsule/test')


if __name__ == '__main__':
    main()
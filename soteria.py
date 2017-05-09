import crypto
import utils
import fake
import hashlib
import argparse
import time
import sys

FOLDER = '/Users/rotemhemo/Desktop/demo'

verbose = True

def main():

    parser = argparse.ArgumentParser()
    parser.add_argument('-enc', help='Encrypt the file ', action="store_true")
    parser.add_argument('-dec', help='Decrypt the file ', action="store_true")

    parser.add_argument('-p', help='User\'s profession', type = str)
    parser.add_argument('-s', help='User\'s sex', type = str)


    args = parser.parse_args()

    if args.enc:
        if not args.p or not args.s:
            print "Please specify your profession and sex"
            exit()
        if verbose:
            print "Generating keys..."
        key, passphrase, salt = crypto.key_gen()

        print "Your passphrase is (Don't lose it!!!) - \n %s"%(passphrase)

        if verbose:
            print "Encrypting your files..."
        x = utils.zip_dir(FOLDER)
        if verbose:
            print "Uploading your files to the server..."
        time.sleep(1)
        r = utils.post_encrypted_file(utils.SERVER_ADDRESS, crypto.encrypt(x, key), ''.join(passphrase[:2]), salt)
        if verbose:
            print "Deleting your files..."
        utils.clean_folder(FOLDER)

        if verbose:
            print "Placing fake files..."
        prof = fake.Profile(args.p, args.s, FOLDER)
        prof.get_files()
        prof.extract_files()

        if verbose:
            sys.stdout.write("Executing self destruction in ")
            for i in range(3):
                time.sleep(1)
                sys.stdout.write(' ' + str(3 - i))
                sys.stdout.flush()

            print "\nHave a safe flight! Bye Bye!"

        utils.self_destruct()


    elif args.dec:
        # From the server
        print "Please Enter your pass phrase - "
        passphrase = raw_input()

        if verbose:
            print "Getting your files from the server..."
        time.sleep(1)
        enc_data, salt = utils.get_encrypted_file(hashlib.sha256(passphrase[:2]).hexdigest())
        key, salt = crypto.key_gen(passphrase, salt)

        if verbose:
            print "Cleaning fake files..."
        utils.clean_folder(FOLDER)

        if verbose:
            print "Decrypting your files..."
        utils.unzip(crypto.decrypt(enc_data, key), FOLDER)

        if verbose:
            print "Placing the decrypted files back... Done!\n Enjoy your freedom!"


if __name__ == '__main__':
    main()
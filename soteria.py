import crypto
import utils
import fake
import hashlib
import argparse

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
        r = utils.post_encrypted_file(utils.SERVER_ADDRESS, crypto.encrypt(x, key), ''.join(passphrase[:2]), salt)
        if verbose:
            print "deleting your files..."
        utils.clean_folder(FOLDER)

        prof = fake.Profile(args.p, args.s, FOLDER)
        prof.get_files()
        prof.extract_files()

    elif args.dec:
        # From the server
        print "Please Enter your pass phrase - "
        passphrase = raw_input()

        if verbose:
            print "Getting your files from the server..."
        enc_data, salt = utils.get_encrypted_file(hashlib.sha256(passphrase[:2]).hexdigest())
        key, salt = crypto.key_gen(passphrase, salt)

        if verbose:
            print "Cleaning fake files..."
        utils.clean_folder(FOLDER)

        if verbose:
            print "Decrypting your files..."
        utils.unzip(crypto.decrypt(enc_data, key), FOLDER)


if __name__ == '__main__':
    main()
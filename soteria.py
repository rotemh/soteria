import crypto
import utils
import fake
import sys

def main():


    #encr = raw_input("Are you encrypting or decrypting files? \n\
     				#Enter \'e\' for encrypt or \'d\' for decrypt: ")
    args = sys.argv
    encr = args[1]
    job = args[2]
    sex = args[3]


    if encr == "-e":
        key, salt = crypto.key_gen("123456")
        x = utils.zip_dir('/Users/rotemhemo/Desktop/time_capsule')
        r = utils.post_encrypted_file(utils.SERVER_ADDRESS, crypto.encrypt(x, key), salt)
        print("Your id is - ", r)
        # print("The following set of questions will help us determine fake files to download to your computer.")
        # first = raw_input("Please type your first name: ")
        # last = raw_input("Please type your last name: ")
        # sex = raw_input("Please type your sex: ")
        # job = raw_input("Please type your profession: ")
        # out_folder = raw_input("Please enter the folder path for where you want the fake files to go: ")
        # print("Thank you. Your files will download shortly.")
        prof = fake.Profile(job, sex, out_folder)
        prof.get_files()
        prof.extract_files()
    elif encr == "-d":
        # From the server
        enc_data, salt = utils.get_encrypted_file(r)
        key, salt = crypto.key_gen("123456", salt)
        utils.unzip(crypto.decrypt(enc_data, key), '/Users/rotemhemo/Desktop/time_capsule/test')


if __name__ == '__main__':
    main()
from crypto import *
from utils import *
def main():

    key, salt = key_gen("123456")
    x  = zip_dir('/Users/rotemhemo/Desktop/time_capsule')
    assert x == decrypt(encrypt(x, key), key), "Same text Encrytpion failed"

if __name__ == '__main__':
    main()
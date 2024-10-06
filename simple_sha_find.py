import sys

from colors import *

from sha256 import *

from sha512 import *

def which_hash():
    sha256_or_sha512 = input("Which hash do you want to calculate: sha256 or sha512? \n")
    if sha256_or_sha512 == "sha256":
        get_hash_sha256()
        verify_checksum_sha256()
    elif sha256_or_sha512 == "sha512":
        get_hash_sha512()
        verify_checksum_sha512()
    else:
        print("Type either sha256 or sha512. If you type anything else the program will close...like this.")
        sys.exit()

if __name__ == "__main__":
    which_hash()
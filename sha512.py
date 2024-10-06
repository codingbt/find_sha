import sys

import hashlib

from results import *

from colors import *

sha512_hash = ''

def get_hash_sha512():
    global sha512_hash
    filename = input("Enter the file name: ")
    sha512_hash = hashlib.sha512()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha512_hash.update(byte_block)
#       print("sha512 valule: \n" + Color.GREEN + sha512_hash.hexdigest())
        print(Color.DARKCYAN + "sha512 value has been calculated")
        color_reset()

def verify_checksum_sha512():
    """Function for comparing calcuated hash with hash provided by developer"""
    print("Enter Checksum Provided by Authorized Distrubutor or Developer...")
    given_checksum = input()
    print(Color.PURPLE + "You entered: " + given_checksum + Color.END)
    print("Calculated : " + Color.GREEN + sha512_hash.hexdigest() + Color.END)
    if given_checksum == sha512_hash.hexdigest():
        safe_results()
    else:
        bad_results()
import sys

import hashlib

from results import *

from colors import *

sha256_hash = ''

def get_hash_sha256():
    global sha256_hash
    filename = input("Enter the file name: ")
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
#       print("sha256 valule: \n" + Color.GREEN + sha256_hash.hexdigest())
        print(Color.DARKCYAN + "sha256 value has been calculated")
        color_reset()

def verify_checksum_sha256():
    """Function for comparing calcuated hash with hash provided by developer"""
    print("Enter Checksum Provided by Authorized Distrubutor or Developer...")
    given_checksum = input()
    print(Color.PURPLE + "You entered: " + given_checksum + Color.END)
    print("Calculated : " + Color.GREEN + sha256_hash.hexdigest())
    if given_checksum == sha256_hash.hexdigest():
        safe_results()
    else:
        bad_results()
import sys

import hashlib

from colors import *

sha512_hash = ''

def color_reset():
    print(Color.END)

def get_hash_sha512():
    global sha512_hash
    filename = input("Enter the file name: ")
    sha512_hash = hashlib.sha512()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha512_hash.update(byte_block)
        print(Color.GREEN + "sha512 valule = " + sha512_hash.hexdigest())
        print(Color.DARKCYAN + "sha512 value has been calculated")
        color_reset()


def verify_checksum_sha512():
    """Function for comparing calcuated hash with hash provided by developer"""
    print("Enter Checksum Provided by Authorized Distrubutor or Developer...")
    given_checksum = input()
    print(Color.PURPLE + "You entered: " + given_checksum)
#    print(Color.GREEN + "Calculated : " + sha512_hash.hexdigest())
    if given_checksum == sha512_hash.hexdigest():
        safe_result = (Color.BOLD + Color.GREEN + "Checksum Verfied! File is OK.")
        print(safe_result)
        color_reset()
    else:
        bad_result = (Color.BOLD + Color.RED + "WARNING!!! Checksum is NOT verified. Verify checksum entry with the checuksum source. Verifiy correct file or package. This is a potentially harmful file or package! Do not proceed! Notify developer or distributor if correct software is being checked and teh calculated checksum continues to not match checksum from developer or distributor.")
        print(bad_result)
        color_reset()
        sys.exit()
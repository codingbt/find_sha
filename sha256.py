import hashlib

from colors import *

sha256_hash = ''

def color_reset():
    print(Color.END)

def get_hash_sha256():
    global sha256_hash
    filename = input("Enter the file name: ")
    sha256_hash = hashlib.sha256()
    with open(filename, "rb") as f:
        for byte_block in iter(lambda: f.read(4096),b""):
            sha256_hash.update(byte_block)
#       print(Color.GREEN + "sha256 valule = " + sha256_hash.hexdigest())
        print(Color.DARKCYAN + "sha256 value has been calculated")
        color_reset()

def verify_checksum_sha256():
    """Function for comparing calcuated hash with hash provided by developer"""
    print("Enter Checksum Provided by Authorized Distrubutor or Developer...")
    given_checksum = input()
    print(Color.PURPLE + "You entered: " + given_checksum)
#    print(Color.GREEN + "Calculated : " + sha256_hash.hexdigest())
    if given_checksum == sha256_hash.hexdigest():
        safe_result = (Color.BOLD + Color.GREEN + "Checksum Verfied! File is OK.")
        print(safe_result)
        color_reset()
    else:
        bad_result = (Color.BOLD + Color.RED + "WARNING!!! Checksum is NOT verified. Verify checksum entry with the checuksum source. Verifiy correct file or package. This is a potentially harmful file or package! Do not proceed! Notify developer or distributor if correct software is being checked and teh calculated checksum continues to not match checksum from developer or distributor.")
        print(bad_result)
        color_reset()
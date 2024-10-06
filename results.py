import sys

from colors import *

def safe_results():
    safe_result = (Color.BOLD + Color.GREEN + "Checksum Verfied! File is OK.")
    print(safe_result)
    color_reset()
    sys.exit()
def bad_results():
    bad_result = (Color.BOLD + Color.RED + "WARNING!!! Checksum is NOT verified. Verify checksum entry with the checuksum source. Verify correct file or package. This is a potentially harmful file or package! Do not proceed! Notify developer or distributor if correct software is being checked and teh calculated checksum continues to not match checksum from developer or distributor.")
    print(bad_result)
    color_reset()
    sys.exit()
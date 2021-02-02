"""
Author: Aleksa Zatezalo
Date: Feb 2, 2021
Description: A simple excersise to
get an intuitive understanding of BTC mining.
"""

from hashlib import sha256
print(sha256("ABC".encode("ascii")).hexdigest())
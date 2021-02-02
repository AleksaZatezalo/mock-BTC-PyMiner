"""
Author: Aleksa Zatezalo
Date: Feb 2, 2021
Description: A simple excersise to
get an intuitive understanding of BTC mining.
"""

from hashlib import sha256

print("Example hash by SHA256 of 'ABC'")
print(sha256("ABC".encode("ascii")).hexdigest())

def SHA256(text):
    return sha256(text.encode("ascii")).hexdigest()


import hashlib
import os
import random
import sys
from string import ascii_lowercase, digits, printable

SYMBOLS = printable[62:]

def handle(req):
    return sbh()

def cc(rot, plaintext):
    plaintext = plaintext.replace(' ', '')
    encrypted = ''

    for c in plaintext:
        if c.isalpha():
            encrypted += ascii_lowercase[(ascii_lowercase.index(c.lower()) + rot) % len(ascii_lowercase)]
        elif c.isdigit():
            encrypted += digits[(digits.index(c) + rot) % len(digits)]
        else:
            encrypted += SYMBOLS[(SYMBOLS.index(c) + rot) % len(SYMBOLS)]
    return hashlib.sha256(bytes(encrypted, 'UTF-8')).hexdigest()

def sbh():
    query = os.getenv('Http_Query').split(',')
    plaintext = query[0].split('=')[1]
    nrots = int(query[1].split('=')[1])
    seed = int(query[2].split('=')[1])

    random.seed(seed)
    text = cc(random.randint(1, sys.maxsize), plaintext)
    for _ in range(1, nrots):
        rot = random.randint(1, sys.maxsize)
        text = cc(rot, text)

    return text
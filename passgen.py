import sys

if len(sys.argv) != 2 or sys.argv[1] == '-h':
    print("Usage: python3 passgen.py [password_length]")
    exit(1)

import random
lower = "abcdefghijklmnñopqrstvwxyz"
upper = "ABCDEFGHIJKLMNÑOPQRSTVWXYZ"
numbers = "0123456789"
symbols = "[]{}*;/,._-+";
all = lower + upper + numbers + symbols;
password = "".join(random.sample(all,int(sys.argv[1])))
print(password)

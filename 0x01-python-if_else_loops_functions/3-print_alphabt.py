#!/usr/bin/python3
for i in range(97, 123):
    alphabet = chr(i)
    if alphabet != 'q' and alphabet != 'e':
        print("{}".format(alphabet), end='')
